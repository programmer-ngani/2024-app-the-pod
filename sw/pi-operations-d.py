D. Control a Relay Module using Raspberry Pi

Pre-requisite:
A. Headless Remote Access for Raspberry Pi (Zero W, Zero 2W, 3 to 5)
B. Control a GPIO pin to Blink an LED.
C. Monitor an Input Switch to Control an LED.

Steps:
8) Use Terminal Commands
8.1) <pwd> for showing the present working directory
8.2) <ls> or <ls -a> for listing sub-directories and files in the current directory
8.3) touch <rly.py> for creating a python file
8.4) sudo nano <rly.py> for editing or creating a file

9) Relay Module 8-Channel Datasheet (https://www.wellpcb.com/blog/components/8-channel-relay/)

9.1) Pin Connection (Relay)
Raspberry Pi	Relay
Board	Label	Module
17	3.3V	VCC
2	5.0V	JDVCC
39	GND	GND
37		IN1

9.2) Pin Connection (Button)
Raspberry Pi	Limit
Board	Label	Switch
30	GND	GND
32		LS-D1

9.3) Relay Module is active low.
9.3.1) Sending logic high to IN1 or 3.3V deactivates the relay coil.
9.3.2) Sending logic low to IN1 or GND activates the relay coil.

9.4) Button (limit switch) is pulled high by internal pull up resistors on the Pi GPIO.
9.4.1) Default state is logic high.
9.4.2) Pressing the button sends logic low signal to Pi GPIO.

10) Relay Script
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

# Initialize constant and variable
MY_BUTTON = 32
MY_RELAY = 37
TEST_DELAY = 1

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(MY_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(MY_RELAY, GPIO.OUT, initial=GPIO.HIGH) # Set pin MY_RELAY to be an output pin and set initial value to high (on)

while True:
    if GPIO.input(MY_BUTTON) == GPIO.LOW:
        print("Button was pushed!")
        GPIO.output(MY_RELAY, GPIO.LOW) # Turn on
    else:
        GPIO.output(MY_RELAY, GPIO.HIGH) # Turn off
    sleep(TEST_DELAY) # Sleep for TEST_DELAY second

10.1) <Ctrl+X> to exit editing.
10.2) Optional to rename file.
10.3) Type <Y> of <N> to save or cancel.

Next:
E. Raspberry Pi Pico Setup
