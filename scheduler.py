from datetime import datetime, timedelta
import pandas as pd
# import ifttt_request
# import random
# import sched, time
#
# sleep_time = 1
# delay_time = 5
# start_time = datetime.now()
# print start_time
# threshold = 0.3
# event = 'washer_stopped_sms'

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
    # print result_df
    return result_df


def determine_mean(sleep_time, delay_time, df):
    number_points = int(delay_time / sleep_time)
    df = df.tail(number_points)
    horizontal_avg = df['horizontal'].mean()
    vertical_avg = df['vertical'].mean()
    print ('Horizontal: {0}, Vertical: {1}'.format(horizontal_avg, vertical_avg))
    return horizontal_avg, vertical_avg


# washer_state = True
# horizontal_df, vertical_df = define_df()
# while washer_state:
#     horizontal_state = random.randint(0, 1)
#     vertical_state = random.randint(0, 1)
#     horizontal_df, vertical_df = current_df(horizontal_df, horizontal_state, vertical_df, vertical_state)
#
#     if (datetime.now() - start_time) > timedelta(seconds=delay_time):
#         start_time = datetime.now()
#         merge_df = merge_csv(horizontal_df, vertical_df)
#         horizontal_avg, vertical_avg = determine_mean(sleep_time, delay_time, merge_df)
#         if horizontal_avg < threshold and vertical_avg < threshold:
#             print 'Washer has turned off'
#             # ifttt_request.send_ifttt_request(event)
#             # washer_state = False
#
#     time.sleep(sleep_time)