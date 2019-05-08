from datetime import datetime, timedelta
import pandas as pd
# import random
# import sched, time

start_time = datetime.now()
print start_time
sleep_time = 1

hor_cols = ['datetime', 'horizontal']
ver_cols = ['datetime', 'vertical']


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
    result_df = pd.merge(horizontal_df, vertical_df, on='datetime', how='outer').sort_values(by='datetime')
    # result_df = result_df.sort_values('datetime')
    print result_df

# horizontal_df, vertical_df = define_df()
# while True:
#     horizontal_state = random.randint(0, 1)
#     vertical_state = random.randint(0, 1)
#     horizontal_df, vertical_df = current_df(horizontal_df, horizontal_state, vertical_df, vertical_state)
#
#     if (datetime.now() - start_time) > timedelta(seconds=5):
#         start_time = datetime.now()
#         merge_csv(horizontal_df, vertical_df)
#
#     time.sleep(sleep_time)
#         # s.enter(20, 1, merge_csv(horizontal_df, vertical_df),  (s,))