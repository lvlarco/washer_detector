import sched, time
# from time import sleep, time
from datetime import datetime, timedelta
import pandas as pd

start_time = datetime.now()
print start_time
sleep_time = 0.5

hor_cols = ['datetime', 'horizontal']
ver_cols = ['datetime', 'vertical']
s = sched.scheduler(time.time, time.sleep)

def define_df():
    horizontal_df = pd.DataFrame(columns=hor_cols)
    vertical_df = pd.DataFrame(columns=ver_cols)
    return horizontal_df, vertical_df


def current_df(horizontal_df, horizontal_state, vertical_df, vertical_state):
    horizontal_list = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), horizontal_state]], columns=hor_cols)
    horizontal_df = horizontal_df.append(horizontal_list)
    vertical_list = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), vertical_state]], columns=ver_cols)
    vertical_df = vertical_df.append(vertical_list)
    return horizontal_df, vertical_df


def merge_csv(horizontal_df, vertical_df):
    result_df = pd.merge(horizontal_df, vertical_df, on='datetime', how='outer')
    print result_df

horizontal_df, vertical_df = define_df()

while True:
    horizontal_state = '0'
    # horizontal_list = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), horizontal_state]], columns=hor_cols)
    # horizontal_df = horizontal_df.append(horizontal_list)
    vertical_state = '1'
    # vertical_list = pd.DataFrame([[datetime.now().strftime('%H:%M:%S'), vertical_state]], columns=ver_cols)
    # vertical_df = vertical_df.append(vertical_list)
    horizontal_df, vertical_df = current_df(horizontal_df, horizontal_state, vertical_df, vertical_state)
    time.sleep(sleep_time)

    if (datetime.now() - start_time) > timedelta(seconds=10):
        start_time = datetime.now()
        merge_csv(horizontal_df, vertical_df)
        # s.enter(20, 1, merge_csv(horizontal_df, vertical_df),  (s,))