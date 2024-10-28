System Configuration

A. Developer
0) Download and Install
0.1) Raspberry Pi Pico Tools (Pico and Pico W)
0.1.1) Thonny IDE
0.1.2) Postman (Optional)
0.2) Raspberry Pi Zero Tools (Zero W and Zero 2W)
0.2.1) Angry IP Scanner or Advanced IP Scanner
0.2.2) Termius or Putty SSH
0.2.3) TigerVNC
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
2) Troubleshooting Tips (Pico)
2.1) Using Thonny IDE, monitor messages on Shell.
2.1.1) IP Address will be shown on Thonny IDE Shell.
2.2) Using IP Scanner, scan network to discover devices.
2.2.1) Connected devices and IP Address will be shown.
3) Remote Access Zero
3.1) Using Termius, type
ssh pi@ip-address -p 22
3.2) Settings,
username: pi
password: raspberry
hostname: ip-address
port: 22
3.3) Install TigerVNC on Zero, type
sudo apt update && sudo apt upgrade
sudo apt install tigervnc-standalone-server
# ref: https://picockpit.com/raspberry-pi/tigervnc-and-realvnc-on-raspberry-pi-bookworm-os/
3.4) Edit settings, type
sudo nano /etc/tigervnc/vncserver-config-mandatory
3.4.1) Find and change content to:
# $localhost should the TigerVNC server only listen on localhost for
#            incoming VNC connections
#
# $localhost = "yes";
$localhost = "no";
3.5) In another device, open TigerVNC
3.5.1) Type in vncserver:
ip-address:5901
3.5.2) To disconnect tigervnc,
ALT+F8


B. Owner
0) The whole system is powered off.
1) First, turn on the wireless router (network).
2) Then, turn on the Raspberry Pi Pico W one-by-one.
2.1) LED is on after startup.
2.2) LED is off once connected to network.
3) Lastly, turn on the Raspberry Pi Zero 2W.
3.1) LED is blinking after startup.
3.2) LED is on once connected to network.
