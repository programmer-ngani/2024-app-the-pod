System Configuration

A. User Guide for Developer
0) Download and Install
0.1) Raspberry Pi Pico Tools (Pico and Pico W)
0.1.1) Thonny IDE
0.1.2) Postman (Optional)
0.2) Raspberry Pi Zero Tools (Zero W and Zero 2W)
0.2.1) Angry IP Scanner or Advanced IP Scanner
0.2.2) Termius or Putty SSH
0.2.3) TigerVNC (Optional)
1) Using Thonny IDE
1.1) Change wifi credentials.
1.2) Create or edit <secrets.py>, add the ff:
WIFI_SSID = "wifi-name"
WIFI_PASSWORD = "wifi-password"
1.3) Edit <main.py>,
1.3.1) Modify:
# From
MY_DEVICE_UID = "mduid-x"
# To
MY_DEVICE_UID = "mduid-1"
# Or
MY_DEVICE_UID = "mduid-2"
1.3.2) Set static IP address using:
# Check your current network configuration (ipconfig)
# TO-DO: add code here
2) Troubleshooting Tips (Pico)
2.1) Using Thonny IDE, monitor messages on Shell.
2.1.1) IP Address will be shown on Thonny IDE Shell.
2.2) Using IP Scanner, scan network to discover devices.
2.2.1) Connected devices and IP Address will be shown.
3) Remote Access Zero (Headless)
3.1) Using Termius, enter
ssh pi@ip-address -p 22
# ip-address from result of IP Scanner
3.2) SSH settings in Termius or Putty,
username: pi
password: raspberry
hostname: ip-address
port: 22
# Read for TigerVNC: picockpit.com/raspberry-pi/tigervnc-and-realvnc-on-raspberry-pi-bookworm-os/ 
3.3) Configure TigerVNC on Zero, enter
sudo apt update && sudo apt upgrade
sudo apt install tigervnc-standalone-server
3.4) Edit settings, enter
sudo nano /etc/tigervnc/vncserver-config-mandatory
3.4.1) Find and change content to:
# $localhost should the TigerVNC server only listen on localhost for
#            incoming VNC connections
#
# $localhost = "yes";
$localhost = "no";
3.4.2) Press CTRL+X, then Y, to save.
3.4.3) Set password, enter
sudo tigervncpasswd
3.4.4) Set view-only password, type n.
3.4.5) Run, enter
tigervncserver
3.4.6) Get the server port (typically something like 5901).
3.5) In another device (computer), download, install, and open TigerVNC.
3.5.1) Type in vncserver:
ip-address:5901
# ip-address from result of IP Scanner
3.5.2) Desktop of Raspberry Pi will be shown.
3.5.3) If not successful, skip.
3.5.4) To disconnect tigervnc, press:
ALT+F8
# Read for NMCLI: jeffgeerling.com/blog/2023/nmcli-wifi-on-raspberry-pi-os-12-bookworm
4) Using nmcli, connecting Zero to a new network.
4.1) Turn off Zero.
4.2) Turn on new network (wireless router).
4.3) Connect device (laptop) on previous network.
4.4) Turn on Zero and wait to connect to previous network.
4.5) Remote access Zero using Termius.
4.6) Using nmcli command in Termius,
4.6.1) Type the following:
sudo nmcli d wifi connect "new_wifi_ssid_here" password "new_wifi_password_here" ifname wlan0
4.6.2) Exit Termius.
4.7) Connect device (laptop) on new network.
4.8) Scan network to discover devices.
4.9) Take note of the new IP address of Zero.
4.10) Remote access Zero with new IP address.
5) Debug main python program using Terminal Commands.
5.1) Stop python program, type:
sudo pkill -f main.py
5.2) Start python program, type:
python main.py
5.3) Cancel program, press:
CTRL-C.
5.4) View program, type:
nano main.py
5.5) Edit program, type:
sudo nano main.py
5.6) Other terminal commands.
# For showing the present working directory 
pwd
# For listing sub-directories and files in the current directory
ls
# For creating a file with any file extension
touch <filename.extension> 
# For editing or creating a file
sudo nano <filename.extension>
# For reboot
sudo reboot
# For shutdown
sudo shutdown -h now
