B. Control a GPIO pin to Blink an LED.

Pre-requisite:
A. Headless Remote Access for Raspberry Pi (Zero W, Zero 2W, 3 to 5)

Steps:
4) Use Terminal Commands
4.1) <pwd> for showing the present working directory
4.2) <ls> or <ls -a> for listing sub-directories and files in the current directory
4.3) touch <led.py> for creating a python file
4.4) sudo nano <led.py> for editing or creating a file

5) LED Script (https://www.hackster.io/rajeshjiet/led-blink-using-raspberry-pi-b38dbe)
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 18 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(18, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(18, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second

5.1) <Ctrl+X> to exit editing.
5.2) Optional to rename file.
5.3) Type <Y> of <N> to save or cancel.

Next:
C. Monitor an Input Switch to Control an LED.
