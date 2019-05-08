import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Input pins
# forward_pin = 12
backward_pin = 18
# turn_right_pin = 13
# turn_left_pin = 19

# GPIO.setup(forward_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(backward_pin, GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(turn_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(turn_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    state = GPIO.input(backward_pin)
    print state
    sleep(1)
    if state == True:
    # forward_state = GPIO.input(forward_pin)
#    backward_state = GPIO.input(backward_pin)
 #   if backward_state == True:
        print 'Vibration detected'
