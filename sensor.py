import RPi.GPIO as GPIO
import sched, time
# from time import sleep, time
from datetime import datetime
import pandas as pd

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

start_time = time.time()
print start_time
sleep_time = 2

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

horizontal_df = pd.DataFrame(columns=['datetime', 'horizontal'])
vertical_df = pd.DataFrame(columns=['datetime', 'vertical'])

s = sched.scheduler(time.time, time.sleep)

def merge_csv(horizontal_df, vertical_df):
    print "Doing stuff..."
    # do your stuff
    # s.enter(10, 1, do_something, (sc,))

while True:
    horizontal_state = GPIO.input(horizontal_sensor)
    vertical_state = GPIO.input(vertical_sensor)
    GPIO.output(horizontal_led, False)
    GPIO.output(vertical_led, False)
    print ('Sensors state: horizontal: {0}, vertical: {1}'.format(horizontal_state, vertical_state))
    time.sleep(sleep_time)
    if horizontal_state:
        GPIO.output(horizontal_led, True)
        horizontal_list = [datetime.now(), horizontal_state]
        horizontal_df.append(horizontal_list)
        time.sleep(sleep_time)
    if vertical_state:
        GPIO.output(vertical_led, True)
        vertical_list = [datetime.now(), vertical_state]
        vertical_df.append(vertical_list)
        time.sleep(sleep_time)

    s.enter(10, 1, merge_csv(horizontal_df, vertical_df), (s,))
    s.run()



