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
print("\tUsage (POST): ", ip + "/api/set-control-data")
print('\tBody (Raw>JSON): {"controlData": "X", "controlCover": "OPEN", }')
print('\tBody (Raw>JSON): {"controlData": "X", "controlCover": "CLOSE", }')

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

@server.route("/api/get-sensor-reading", methods=["GET"])
def sensorReading(request):
    temperature = getSensorReading()
    temperature = "%.2f" % round(temperature, 2)
    sensorDict = dict()
    sensorDict["temperature"] = str(temperature) + " degree Celsius"
    return json.dumps(sensorDict), 200, {"Content-Type": "application/json"}

@server.route("/api/set-control-data", methods=["POST"])
def ledControl(request):
    try:
        controlDataValue = request.data["controlData"]
        controlCoverValue = request.data["controlCover"]
        if(controlDataValue == "F"):
            print('C1 State:', 'Occupied')
            led_internal.value(1)
        elif(controlDataValue == "T"):
            print('C1 State:', 'Available')
            led_internal.value(0)
        elif(controlDataValue == "X"):
            print('C1 State:', 'Service Mode')
            led_internal.value(0)
            controlOutput(controlDataValue, controlCoverValue)
        #print("controlDataStatus: ", controlDataValue)
        return json.dumps({"message" : "Command sent successfully!"}), 200, {"Content-Type": "application/json"}
    except:
        pass

@server.catchall()
def catchall(request):
    return json.dumps({"message" : "URL not found!"}), 404, {"Content-Type": "application/json"}

def controlOutput(u, d):
    if(u == "X"):
        if(d == "OPEN"):
            print("MSG:", "Opening...")
            coverControl("FORWARD")
        elif(d == "CLOSE"):
            print("MSG:", "Closing...")
            coverControl("REVERSE")

def coverControl(c):
    if(c == "FORWARD"):
        print("MSG:", "Motor Forward.")
        relay_pin1.value(1)
        relay_pin2.value(1)
        relay_pin3.value(0)
        while (limit_switch_top_l.value() == 1 and limit_switch_top_r.value() == 1):
            pass
        relay_pin3.value(1)
        print("MSG:", "Motor OFF.")
    elif(c == "REVERSE"):
        print("MSG:", "Motor Reverse.")
        relay_pin1.value(0)
        relay_pin2.value(0)
        relay_pin3.value(0)
        while(limit_switch_btm_l.value() == 1 and limit_switch_btm_r.value() == 1):
            pass
        relay_pin1.value(1)
        relay_pin2.value(1)
        relay_pin3.value(1)
        print("MSG:", "Motor OFF.")

server.run()
