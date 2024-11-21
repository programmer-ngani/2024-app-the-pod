# Pico Script
from phew import connect_to_wifi, server
from machine import Pin
import network, time, json

import secrets
WIFI_SSID = secrets.WIFI_SSID
WIFI_PASSWORD = secrets.WIFI_PASSWORD
IPV4_ADDRESS = secrets.IPV4_ADDRESS
SUBNET_MASK = secrets.SUBNET_MASK
DEFAULT_GATEWAY = secrets.DEFAULT_GATEWAY
DEFAULT_DNS = secrets.DEFAULT_DNS

MY_DEVICE_UID = "mduid-1"
MINIMUM_DISTANCE = 10

# Define pin numbers for ultrasonic sensor's TRIG and ECHO pins
TRIG = Pin(14, machine.Pin.OUT)  # TRIG pin set as output
ECHO = Pin(15, machine.Pin.IN)  # ECHO pin set as input

led_internal = Pin('LED', Pin.OUT)
led_internal.value(1)

relay_pin1 = Pin(16, Pin.OUT)
relay_pin2 = Pin(17, Pin.OUT)
relay_pin3 = Pin(18, Pin.OUT)
relay_pin4 = Pin(19, Pin.OUT)
relay_pin5 = Pin(20, Pin.OUT)
relay_pin6 = Pin(21, Pin.OUT)
relay_pin1.value(1)
relay_pin2.value(1)
relay_pin3.value(1)
relay_pin4.value(1)
relay_pin5.value(1)
relay_pin6.value(1) 

limit_switch_mtr_u = Pin(2, Pin.IN, Pin.PULL_UP)
limit_switch_top_l = Pin(6, Pin.IN, Pin.PULL_UP)
limit_switch_top_r = Pin(7, Pin.IN, Pin.PULL_UP)
limit_switch_btm_l = Pin(10, Pin.IN, Pin.PULL_UP)
limit_switch_btm_r = Pin(11, Pin.IN, Pin.PULL_UP)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
wlan.ifconfig((IPV4_ADDRESS, SUBNET_MASK, DEFAULT_GATEWAY, DEFAULT_DNS))

# Handle connection error
while wlan.status() != 3:
    print("Reconnecting: Please check network.")
    time.sleep(1)
    led_internal.toggle()

ip = wlan.ifconfig()[0]
print("\nConnected to IP: ", ip)
# Usage 1
print("\nUsage (POST): ", ip + "/api/set-control-data")
# Admin (Service Mode (Yes): Open or close, Service Mode (No): Close only, )
print('\tBody (Raw>JSON): {"controlData": "X", "controlCover": "OPEN", }')
print('\tBody (Raw>JSON): {"controlData": "X", "controlCover": "CLOSE", }')
print('\tBody (Raw>JSON): {"controlData": "T", "controlCover": "CLOSE", }')
# User (Available (No): Open or close,)
print('\tBody (Raw>JSON): {"controlData": "F", "controlCover": "OPEN", }')
print('\tBody (Raw>JSON): {"controlData": "F", "controlCover": "CLOSE", }')
# User (Available (No to Yes): Open then close,)
print('\tBody (Raw>JSON): {"controlData": "T", "controlCover": "NULL", }')
# Usage 2
print("\nUsage (POST): ", ip + "/api/get-pod-state")
print('\tBody (Raw>JSON): {"stateData": "OCCUPIED", }')
print('\tBody (Raw>JSON): {"stateData": "AVAILABLE", }')

led_internal.value(0)

def getSensorReading():
    try:
        # Use ADC pin GP4
        adc = machine.ADC(4)
        # ADC conversion factor
        conversion_factor = 3.3 / (65535)
        sensor_value = adc.read_u16() * conversion_factor
        # Convert sensor value to temperature (formula may vary)
        temperature = 27 - (sensor_value - 0.706) / 0.001721
    except:
        temperature = 0.00
    temperature = "%.2f" % round(temperature, 2)
    print("\nCPU Temp: " + str(temperature) + " degree Celsius\n")
    return float(temperature)

@server.route("/api/get-pod-state", methods=["POST"])
def stateReading(request):
    stateDataValue = request.data["stateData"]
    if(not getStatusDistance()):
        if(limit_switch_mtr_u.value() == 1):
            ledControl("OFF")
        else:
            print("MSG:", "Sensor detected...")
            stateDataValue = "OCCUPIED"
            ledControl("ON")
    else:
        print("MSG:", "Sensor detected...")
        stateDataValue = "OCCUPIED"
        ledControl("ON")
    stateDict = dict()
    stateDict["stateData"] = stateDataValue
    return json.dumps(stateDict), 200, {"Content-Type": "application/json"}

@server.route("/api/set-control-data", methods=["POST"])
def podControl(request):
    global controlCoverResponse
    controlCoverResponse = "NONE"
    try:
        controlDataValue = request.data["controlData"]
        controlCoverValue = request.data["controlCover"]
        if(controlDataValue == "F"):
            print('C1 State:', 'Occupied')
            led_internal.value(1)
            ledControl("ON")
            controlOutput(controlDataValue, controlCoverValue)
        elif(controlDataValue == "T"):
            print('C1 State:', 'Available')
            led_internal.value(0)
            ledControl("OFF")
            controlOutput(controlDataValue, controlCoverValue)
        elif(controlDataValue == "X"):
            print('C1 State:', 'Service Mode')
            led_internal.value(0)
            ledControl("ON")
            controlOutput(controlDataValue, controlCoverValue)
    except:
        pass
    stateDict = dict()
    stateDict["stateData"] = controlCoverResponse
    return json.dumps(stateDict), 200, {"Content-Type": "application/json"}

@server.catchall()
def catchall(request):
    return json.dumps({"message" : "URL not found!"}), 404, {"Content-Type": "application/json"}

def controlOutput(u, d):
    if(u == "X"):
        if(d == "OPEN"):
            if not getLimitTop():
                print("MSG (7):", "Opening...")
                coverControl("FORWARD")
            else:
                print("\tOpen success.")
        elif(d == "CLOSE"):
            if not getLimitBtm():
                print("MSG (7):", "Closing...")
                coverControl("REVERSE")
            else:
                print("\tClose success.")
    elif(u == "T"):
        if(d == "OPEN"):
            if not getLimitTop():
                print("MSG (7):", "Opening...")
                coverControl("FORWARD")
            else:
                print("\tOpen success.")
        elif(d == "CLOSE"):
            if not getLimitBtm():
                print("MSG (7):", "Closing... for release. ")
                coverControl("REVERSE")
            else:
                print("\tClose success.")
        else:
            print("Note:", "Autoclose in set seconds.")  
    elif(u == "F"):
        if(d == "OPEN"):
            if not getLimitTop():
                print("MSG (7):", "Opening...")
                coverControl("FORWARD")
            else:
                print("\tOpen success.")
        elif(d == "CLOSE"):
            if not getLimitBtm():
                print("MSG (7):", "Closing...")
                coverControl("REVERSE")
            else:
                print("\tClose success.")

def getLimitTop():
    global controlCoverResponse
    if not (limit_switch_top_l.value() == 1 and limit_switch_top_r.value() == 1):
        print("MSG (4):", "Motor OFF.")
        relay_pin3.value(1)
        print("MSG (5):", "Solenoid OFF.")
        relay_pin4.value(1)
        print("\tMSG (6):", "Done.")
        controlCoverResponse = "DONE"
        return True
    return False

def getLimitBtm():
    global controlCoverResponse
    if not (limit_switch_btm_l.value() == 1 and limit_switch_btm_r.value() == 1):
        print("MSG (4):", "Motor OFF.")
        relay_pin1.value(1)
        relay_pin2.value(1)
        relay_pin3.value(1)
        print("MSG (5):", "Solenoid OFF.")
        relay_pin4.value(1)
        print("\tMSG (6):", "Done.")
        controlCoverResponse = "DONE"
        return True
    return False

def coverControl(c):
    global controlCoverResponse
    if(c == "FORWARD"):
        print("MSG (1):", "Solenoid ON.")
        relay_pin4.value(0)
        print("MSG (2):", "Light ON.")
        relay_pin5.value(0)
        time.sleep(1)
        print("MSG (3):", "Motor Forward.")
        relay_pin1.value(1)
        relay_pin2.value(1)
        relay_pin3.value(0)
    elif(c == "REVERSE"):
        print("MSG (1):", "Solenoid ON.")
        relay_pin4.value(0)
        print("MSG (2):", "Light OFF.")
        relay_pin5.value(1)
        time.sleep(1)
        print("MSG (3):", "Motor Reverse.")
        relay_pin1.value(0)
        relay_pin2.value(0)
        relay_pin3.value(0)

def ledControl(l):
    if(l == "ON"):
        print("MSG (O):", "Light ON.")
        relay_pin6.value(0)
        print("\tMSG (O):", "Done.")
    elif(l == "OFF"):
        print("MSG (A):", "Light OFF.")
        relay_pin6.value(1)
        print("\tMSG (A):", "Done.")

def checkDistance():
    # Function to calculate distance in centimeters
    TRIG.low()  # Set TRIG low
    time.sleep_us(2)  # Wait for 2 microseconds
    TRIG.high()  # Set TRIG high
    time.sleep_us(10)  # Wait for 10 microseconds
    TRIG.low()  # Set TRIG low again
    # Wait for ECHO pin to go high
    while not ECHO.value():
        pass
    time1 = time.ticks_us()  # Record time when ECHO goes high
    # Wait for ECHO pin to go low
    while ECHO.value():
        pass
    time2 = time.ticks_us()  # Record time when ECHO goes low
    # Calculate the duration of the ECHO pin being high
    during = time.ticks_diff(time2, time1)
    during_cm = during * 340 / 2 / 10000  # Distance in centimeters
    
    # Return the calculated distance (using speed of sound)
    return during_cm

def getStatusDistance():
    distance = checkDistance()
    print("Distance: %.2f cm" % distance)  # Print distance
    if(distance <= MINIMUM_DISTANCE):
        return True
    return False

print("\nMSG:", "Server started.")
server.run()
