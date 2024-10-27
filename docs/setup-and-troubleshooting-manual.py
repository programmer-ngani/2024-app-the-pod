System Configuration

A. Developer
1) Using Thonny IDE
1.1) Change wifi credentials.
1.2) Create or edit <secrets.py>, add the ff:
WIFI_SSID = "wifi-name"
WIFI_PASSWORD = "wifi-password"
1.3) Edit <main.py>, change:
#from
MY_DEVICE_UID = "mduid-x"
#to
MY_DEVICE_UID = "mduid-1"
#or
MY_DEVICE_UID = "mduid-2"

B. Owner
0) The whole system is powered off.
1) First, turn on the wireless router (network).
2) Then, turn on the Raspberry Pi Pico W one-by-one.
2.1) LED is on after startup.
2.2) LED is off once connected to network.
3) Lastly, turn on the Raspberry Pi Zero 2W.
3.1) LED is blinking after startup.
3.2) LED is on once connected to network.
