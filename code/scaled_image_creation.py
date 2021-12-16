import matplotlib.image as img
import pandas as pd
import os

from pandas.core.frame import DataFrame
import constants
import numpy as np
import matplotlib.pyplot as plt

def get_price_changes(dates, df):
    price_changes = []
    current_date = dates.pop(1)
    dates.pop(0)
    current_row = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == current_date))]
    current_price = current_row['price'].item()
    for date in dates:
        row = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date))]
        price = row['price'].item()
        difference = current_price-price
        percent_difference = difference/current_price
        price_changes.append(percent_difference)
    
    return price_changes

def get_dates(date):
    all_q_dates = constants.QUARTERLY_REPORT_DATES
    current_index = all_q_dates.index(date)

    one_q_past_index = current_index-1
    two_q_future_index = current_index+2
    three_q_future_index = current_index+3
    four_q_future_index = current_index+4
    num_q_dates = len(all_q_dates) - 1
    if (one_q_past_index < 0 or two_q_future_index > num_q_dates or three_q_future_index > num_q_dates or four_q_future_index > num_q_dates):
        return False
    else:
        one_quarter_past = all_q_dates[one_q_past_index]
        two_quarter_future = all_q_dates[two_q_future_index]
        three_quarter_future = all_q_dates[three_q_future_index]
        four_quarter_future = all_q_dates[four_q_future_index]
        dates = [one_quarter_past, date, two_quarter_future, three_quarter_future, four_quarter_future]
        return dates

def quarter_is_usable(coverage_df, date):
    dates = get_dates(date)
    if(dates):
        MRQ_past = ((coverage_df['dimension'] == 'MRQ') & coverage_df[dates[0]] == 1).any()
        MRQ_current = ((coverage_df['dimension'] == 'MRQ') & coverage_df[dates[1]] == 1).any()
        MRT_current = ((coverage_df['dimension'] == 'MRT')& coverage_df[dates[1]] == 1).any()
        price_2_q_future = ((coverage_df['dimension'] == 'MRQ') & coverage_df[date[2]] == 1).any()
        price_3_q_future = ((coverage_df['dimension'] == 'MRQ') & coverage_df[date[3]] == 1).any()
        price_4_q_future = ((coverage_df['dimension'] == 'MRQ') & coverage_df[date[4]] == 1).any()

        if(MRQ_past and MRQ_current and price_2_q_future and price_3_q_future and price_4_q_future):
            return dates
        else:
            return False
    else:
        return False


images_df = pd.DataFrame(
    columns = ['image-filename', 'percent-price-change_6month', 'percent-price-change_9month', 'percent-price-change_12month'])


def mrq_mrt_image(dates, df, filename):
    mrq_past = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == dates[0]))]
    mrq_current = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == dates[1]))]
    mrt = df[((df['dimension'] == 'MRT') & (df['calendardate'] == dates[1]))]

    mrq_past = mrq_past[constants.SF1_GOOD_INDICATORS]
    mrq_current = mrq_past[constants.SF1_GOOD_INDICATORS]
    mrt = mrt[constants.SF1_GOOD_INDICATORS]
    
    mrq_past = mrq_past.to_numpy()[0]
    mrq_current = mrq_current.to_numpy()[0]
    mrt = mrt.to_numpy()[0]

    mrq_past = mrq_past.reshape(9, 9)
    mrq_current = mrq_current.reshape(9, 9)
    mrt = mrt.reshape(9,9)

    zeros = np.zeros((9, 9), np.float64)
    ones = zeros+1

    rgb = np.dstack((mrq_past, mrq_current, mrt, ones))
    img.imsave(constants.IMAGE_PATH+'/'+filename+'.png', rgb)
    return 0


for csv in os.listdir(constants.DATA_PATH+'/SF1_scaled'):
    if(csv == ".DS_Store"):
        continue
    split = csv.split('_')
    ticker = split[0]
    mr_df = pd.read_csv(constants.DATA_PATH+'/SF1_scaled/'+csv)
    coverage_df = pd.read_csv(constants.DATA_PATH+'/SF1/'+ticker+'/'+ticker+'_coverage.csv')
  
    for date in constants.QUARTERLY_REPORT_DATES:
        dates = quarter_is_usable(coverage_df, date)
        if(dates):
            filename = date+'-'+ticker
            price_changes = get_price_changes(dates, mr_df)
            mrq_mrt_image(dates, mr_df, filename)
        else:
            continue
        
