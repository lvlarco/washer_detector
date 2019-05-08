import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Input pins
horizontal_sensor = 18
vertical_sensor = 23

GPIO.setup(horizontal_sensor, GPIO.IN)
GPIO.setup(vertical_sensor, GPIO.IN)

while True:
    horizontal_state = GPIO.input(horizontal_sensor)
    vertical_state = GPIO.input(vertical_sensor)
    # print ('Sensors state: horizontal: {0}, vertical: {1}'.format(horizontal_state, vertical_state))
    sleep(0.5)
    if horizontal_state:
        print 'Horizontal vibration'
    if vertical_state:
        print 'Vertical vibration'
