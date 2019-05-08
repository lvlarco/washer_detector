import RPi.GPIO as GPIO
import sched, time
import scheduler
from datetime import datetime, timedelta
# import pandas as pd

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

start_time = datetime.now()
print start_time
sleep_time = 0.5

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

hor_cols = ['datetime', 'horizontal']
ver_cols = ['datetime', 'vertical']
horizontal_df, vertical_df = scheduler.define_df()

while True:
    horizontal_state = GPIO.input(horizontal_sensor)
    vertical_state = GPIO.input(vertical_sensor)
    GPIO.output(horizontal_led, False)
    GPIO.output(vertical_led, False)
    print ('Sensors state: horizontal: {0}, vertical: {1}'.format(horizontal_state, vertical_state))
    horizontal_df, vertical_df = scheduler.current_df(horizontal_df, horizontal_state, vertical_df, vertical_state)

    if horizontal_state or vertical_state:
        if horizontal_state:
            GPIO.output(horizontal_led, True)
        elif vertical_state:
            GPIO.output(vertical_led, True)

    if (datetime.now() - start_time) > timedelta(seconds=10):
        start_time = datetime.now()
        scheduler.merge_csv(horizontal_df, vertical_df)

    time.sleep(sleep_time)



