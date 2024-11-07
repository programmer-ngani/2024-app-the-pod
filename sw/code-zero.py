# Zero Script
import requests
from threading import Thread
from time import sleep
from firebase import firebase

MY_FB_URL = 'https://capsule-app-738d0-default-rtdb.asia-southeast1.firebasedatabase.app/'
MY_IP_NO_1 = '192.168.1.61'
global_time_counter = 0

print('Turn LED Off here...')
try:
    my_firebase = firebase.FirebaseApplication(MY_FB_URL, None)
    print('Success...')
except:
    print('Warning: Turn LED On here...')

def runCap1(i):
    url = 'http://' + i + '/api/set-control-data'
    while True:
        print('C1 State:', 'Checking...')
        DEVICE_ID = 'a'
        DATA_ID = 'aDataAvailable'
        try:
            result = my_firebase.get('/device-state', DEVICE_ID + '/' + DATA_ID)
            #print('result:', result, '- type:', type(result))
            if(result is not None):
                if(result == 'T'):
                    print('C1 State:', 'Available')
                    myobj = {'controlData': 'T'}
                    try:
                        x = requests.post(url, json = myobj)
                        print(x.json())
                    except:
                        print('C1 Result:', 'Device not found.')
                        pass
                elif(result == 'F'):
                    print('C1 State:', 'Occupied')
                    myobj = {'controlData': 'F'}
                    try:
                        x = requests.post(url, json = myobj)
                        print(x.json())
                    except:
                        print('C1 Result:', 'Device not found.')
                        pass
                elif(result == 'X'):
                    print('C1 State:', 'Service Mode')
                    myobj = {'controlData': 'X'}
                    try:
                        x = requests.post(url, json = myobj)
                        print("Response (Pico):", x.json())
                        done_once_open = False
                        done_once_close = False
                        while True:
                            if not done_once_open:
                                done_once_open = True
                                done_once_close = False
                                myobj = {'controlData': 'X'}
                                myobj["controlCover"] = "open"
                                x = requests.post(url, json = myobj)
                                print("Response (Pico):", x.json())
                            elif not done_once_close:
                                done_once_close = True
                                done_once_open = False
                                myobj = {'controlData': 'X'}
                                myobj["controlCover"] = "close"
                                x = requests.post(url, json = myobj)
                                print("Response (Pico):", x.json())

                            result = my_firebase.get('/device-state', DEVICE_ID + '/' + DATA_ID)
                            #print('result:', result, '- type:', type(result))
                            if(result is not None):
                                if(result == 'T'):
                                try:
                                    x = requests.post(url, json = myobj)
                                    print(x.json())
                                    break
                                except:
                                    print('C1 Result:', 'Device not found.')
                                    pass
                    except:
                        print('C1 Result:', 'Device not found.')
                        pass
                    
        except:
            rint('D1 Result:', 'Database not found.')
            pass
        sleep(5)

def runCap2():
    # dummy process for second device
    global global_time_counter
    local_time_counter = global_time_counter
    while True:
        print('C2 State:', local_time_counter)
        local_time_counter += 1
        if(local_time_counter >= 10):
            local_time_counter = 0
        sleep(1)
        global_time_counter = local_time_counter

capsule1 = Thread(target=runCap1, args=(MY_IP_NO_1, ))
capsule2 = Thread(target=runCap2)
capsule1.start()
capsule2.start()
capsule1.join()
capsule2.join()

#
# Zero Snippets
#

def getDeviceState(i):
    url = 'http://' + i + '/api/get-sensor-reading'
    try:
        x = requests.get(url)
        return x.json()
    except:
        return None

def runCap1():
    while True:
        MY_DEVICE_UID = input("MY_DEVICE_UID: ")
        if(MY_DEVICE_UID == "mduid-1"):
            print(MY_IP_NO_1 + ' response:', getDeviceState(MY_IP_NO_1))
        else:
            print("MY_DEVICE_UID:", MY_DEVICE_UID)
