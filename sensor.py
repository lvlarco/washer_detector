import RPi.GPIO as GPIO
import time
import scheduler
import ifttt_request
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

hor_cols = ['datetime', 'horizontal']
ver_cols = ['datetime', 'vertical']
horizontal_df, vertical_df = scheduler.define_df()

washer_state = True
while washer_state:
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

    if (datetime.now() - start_time) > timedelta(seconds=delay_time):
        start_time = datetime.now()
        merge_df = scheduler.merge_csv(horizontal_df, vertical_df)
        horizontal_avg, vertical_avg = scheduler.determine_mean(sleep_time, delay_time, merge_df)
        if horizontal_avg < threshold and vertical_avg < threshold:
            print 'Washer has turned off'
            ifttt_request.send_ifttt_request(event)
            washer_state = False
    time.sleep(sleep_time)

GPIO.cleanup()
