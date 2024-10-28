A. Headless Remote Access for Raspberry Pi (Zero W, Zero 2W, 3 to 5)

Pre-requisite:
Raspberry Pi connected to a wireless network with SSH enabled.

Steps:
1) Scan network.
1.1) Use any network scanning tool.
1.2) Take note of the IP Address of the Raspberry Pi.
1.3) Note: ip-address

2) Headless remote access.
2.1) Use any SSH tool like Termius.
2.2) Type in the terminal: ssh user@ip-address -p 22
2.3) Input username and password when asked.

3) Use Terminal Commands
3.1) pwd for showing the present working directory
3.2) ls for listing sub-directories and files in the current directory
3.3) touch <filename.extension> for creating a file with any file extension
3.4) sudo nano <filename.extension> for editing or creating a file

Next:
B. Control a GPIO pin to Blink an LED.
