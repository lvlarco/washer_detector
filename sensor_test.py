import RPi.GPIO as GPIO
import time
import scheduler
from datetime import datetime, timedelta

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

start_time = datetime.now()
print start_time
sleep_time = 0.5
delay_time = 15
threshold = 0.05
event = 'washer_stopped_sms'

# Input pins
horizontal_sensor = 18
vertical_sensor = 24
# Output pins
horizontal_led = 17
vertical_led = 4

GPIO.setup(horizontal_sensor, GPIO.IN)
GPIO.setup(vertical_sensor, GPIO.IN)
GPIO.setup(horizontal_led, GPIO.OUT)
GPIO.setup(vertical_led, GPIO.OUT)

washer_state = True
while washer_state:
    GPIO.output(horizontal_led, False)
    GPIO.output(vertical_led, False)
    print ('Sensors state: horizontal: {0}, vertical: {1}'.format(horizontal_state, vertical_state))

    if horizontal_state# or vertical_state:
        GPIO.output(horizontal_led, True)
    if vertical_state:
        GPIO.output(vertical_led, True)

    washer_state = False
    time.sleep(sleep_time)

GPIO.cleanup()
