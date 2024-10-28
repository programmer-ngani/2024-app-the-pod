C. Monitor an Input Switch to Control an LED.

Pre-requisite:
A. Headless Remote Access for Raspberry Pi (Zero W, Zero 2W, 3 to 5)
B. Control a GPIO pin to Blink an LED. 

Steps:
6) Use Terminal Commands
6.1) <pwd> for showing the present working directory
6.2) <ls> or <ls -a> for listing sub-directories and files in the current directory
6.3) touch <btn.py> for creating a python file
6.4) sudo nano <btn.py> for editing or creating a file

7) Button Script (https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/)
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 18 to be an output pin and set initial value to low (off)

while True:
    if GPIO.input(10) == GPIO.LOW:
        print("Button was pushed!")
        GPIO.output(18, GPIO.HIGH) # Turn on
    else:
        GPIO.output(18, GPIO.LOW) # Turn off
    sleep(1) # Sleep for 1 second

7.1) <Ctrl+X> to exit editing.
7.2) Optional to rename file.
7.3) Type <Y> of <N> to save or cancel.

Next:
D. Control a Relay Module using Raspberry Pi
