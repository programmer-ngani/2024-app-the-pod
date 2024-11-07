# Zero Script
import requests, json
from threading import Thread
from time import sleep
from firebase import firebase

MY_FB_URL = 'https://capsule-app-738d0-default-rtdb.asia-southeast1.firebasedatabase.app/'
MY_IP_NO_1 = '192.168.1.71'
MY_IP_NO_2 = '192.168.1.62'
global_time_counter = 0

print('Turn LED Off here...')
try:
    my_firebase = firebase.FirebaseApplication(MY_FB_URL, None)
    print('Success...')
except:
    print('Warning: Turn LED On here...')

def runCap1(ip):
    global my_firebase
    url = 'http://' + ip + '/api/set-control-data'
    while True:
        print('C1 State:', 'Checking...')
        DEVICE_ID = 'a'
        DATA_ID_A = 'aDataAvailable'
        DATA_ID_D = 'dDataControlCoverOpen'
        try:
            result = my_firebase.get('/device-state', DEVICE_ID + '/' + DATA_ID_A)
            #print('result:', result, '- type:', type(result))
            if(result is not None):
                if(result == 'T'):
                    print('C1 State:', 'Available')
                    myobj = {'controlData': 'T'}
                    myobj["controlCover"] = "NULL"
                    try:
                        x = requests.post(url, json = myobj)
                        print(x.json())
                    except:
                        print('C1 Result (T, NULL):', 'Device not found.')
                elif(result == 'F'):
                    print('C1 State:', 'Occupied')
                    myobj = {'controlData': 'F'}
                    myobj["controlCover"] = "NULL"
                    try:
                        x = requests.post(url, json = myobj)
                        print(x.json())
                    except:
                        print('C1 Result (F, NULL):', 'Device not found.')
                elif(result == 'X'):
                    print('C1 State:', 'Service Mode')
                    myobj = {'controlData': 'X'}
                    myobj["controlCover"] = "OPEN"
                    try:
                        x = requests.post(url, json = myobj)
                        sleep(1)
                        print("Response (Pico):", x.json())

                        while True:
                            controlCoverOpen = my_firebase.get('/device-state', DEVICE_ID + '/' + DATA_ID_D)
                            if controlCoverOpen is not None:
                                if(controlCoverOpen == 'T'):
                                    myobj = {'controlData': 'X'}
                                    myobj["controlCover"] = "OPEN"
                                    y = requests.post(url, json = myobj)
                                    sleep(1)
                                    print("Response (Pico - OPEN):", y.json())
                                    if(y.json()['stateData'] == "DONE"):
                                        my_firebase_put = my_firebase.put('/device-state/' + DEVICE_ID, DATA_ID_D, "X")
                                        print("Response (Firebase):", my_firebase_put)
                                elif(controlCoverOpen == 'F'):
                                    myobj = {'controlData': 'X'}
                                    myobj["controlCover"] = "CLOSE"
                                    y = requests.post(url, json = myobj)
                                    sleep(1)
                                    print("Response (Pico - CLOSE):", y.json())
                                    if(y.json()['stateData'] == "DONE"):
                                        my_firebase_put = my_firebase.put('/device-state/' + DEVICE_ID, DATA_ID_D, "X")
                                        print("Response (Firebase):", my_firebase_put)

                            result = my_firebase.get('/device-state', DEVICE_ID + '/' + DATA_ID_A)
                            if(result is not None):
                                if(result == 'T'):
                                    try:
                                        myobj = {'controlData': 'T'}
                                        myobj["controlCover"] = "CLOSE"
                                        z = requests.post(url, json = myobj)
                                        print(z.json())
                                        break
                                    except:
                                        print('C1 Result (T, CLOSE):', 'Device not found.')
                    except:
                        print('C1 Result: (X, OPEN)', 'Device not found.')
        except:
            print('D1 Result:', 'Database not found.')
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
#e
