from PIL import Image
import pandas as pd
import os
import constants
import numpy as np

# helper function to get calendardate 2 quarters from given date


def in_two_quarters_date(date):
    all_quarter_dates = constants.QUARTERLY_REPORT_DATES
    current_index = all_quarter_dates.index(date)
    in_two_quarters_index = current_index+2
    if (in_two_quarters_index > (len(all_quarter_dates) - 1)):
        return False
    else:
        return all_quarter_dates[in_two_quarters_index]


# helper function to take two dates and coverage_df and return true if date has MRT and MRQ for both dates
def has_data_for_testing(date, coverage_df):
    has_MRQ = ((coverage_df['dimension'] == 'MRQ')
               & coverage_df[date] == 1).any()
    has_MRT = ((coverage_df['dimension'] == 'MRT')
               & coverage_df[date] == 1).any()
    comparison_date = in_two_quarters_date(date)
    if (not comparison_date):
        return False

    has_comparison_MRQ = ((coverage_df['dimension'] == 'MRQ')
                          & coverage_df[comparison_date] == 1).any()
    has_comparison_MRT = ((coverage_df['dimension'] == 'MRT')
                          & coverage_df[comparison_date] == 1).any()

    if(has_MRQ and has_MRT and has_comparison_MRQ and has_comparison_MRT):
        return True
    else:
        return False

# helper function to get percent change in price given starting date, and mr_df


def percent_price_change(date_0, df):
    row_0 = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date_0))]
    price_0 = row_0['price'].item()

    date_1 = in_two_quarters_date(date_0)
    row_1 = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date_1))]
    price_1 = row_1['price'].item()

    difference = price_1-price_0
    percent_difference = difference/price_0
    return percent_difference
# helper function to create image from row of dataframe


def mrq_mrt_image(date, df, filename):
    mrq_row = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date))]
    mrt_row = df[((df['dimension'] == 'MRT') & (df['calendardate'] == date))]
    mrq_good_row = mrq_row[constants.SF1_GOOD_INDICATORS]
    mrt_good_row = mrt_row[constants.SF1_GOOD_INDICATORS]
    isna_mrq = mrq_good_row.isna().sum().sum()
    isna_mrt = mrt_good_row.isna().sum().sum()
    mrq_arr = mrq_good_row.to_numpy()[0]
    mrt_arr = mrt_good_row.to_numpy()[0]

    # mrq_arr = mrq_arr.reshape(17, 5)
    # mrt_arr = mrt_arr.reshape(17, 5)

    mrq_arr = mrq_arr.reshape(9, 9)
    mrt_arr = mrt_arr.reshape(9, 9)

    # zeros = np.zeros((17, 5), 'uint8')

    zeros = np.zeros((9, 9), 'uint8')

    rgb = np.dstack((mrq_arr, mrt_arr, zeros))

    img = Image.fromarray(rgb, mode='RGB')
    img.save(constants.PROJECT_PATH+'/images_81_pixels/'+filename, "PNG")
    return (isna_mrq+isna_mrt)


# for every ticker
images_df = pd.DataFrame(
    # columns=['image-filename', 'percent-price-change', 'missing-values', 'label', 'train'])
    columns = ['image-filename', 'percent-price-change', 'missing-values'])
for ticker in os.listdir(constants.DATA_PATH+'/SF1'):
    this_path = os.path.join(constants.DATA_PATH, 'SF1/'+ticker)
    if(os.path.isfile(this_path)):
        continue
    mr_csv_filename = ticker+'_mr.csv'
    coverage_csv_filename = ticker+'_coverage.csv'
    mr_df = pd.read_csv(constants.DATA_PATH+'/SF1/'+ticker+'/'+mr_csv_filename)
    coverage_df = pd.read_csv(
        constants.DATA_PATH+'/SF1/'+ticker+'/'+coverage_csv_filename)
    # for every date with MRQ and MRT reported check if they are covered 6 months later
    for date in constants.QUARTERLY_REPORT_DATES:
        # check if MRT and MRQ exist.
        if(not has_data_for_testing(date, coverage_df)):
            continue

        image_filename = ticker+'_'+date+'.png'
        # calculate percent change in price
        price_change = percent_price_change(date, mr_df)
        # create image
        total_isna = mrq_mrt_image(date, mr_df, image_filename)
        images_df = images_df.append(
            # {'image-filename': image_filename, 'percent-price-change': price_change, 'missing-values': total_isna, 'label': 0, 'train': 0}, ignore_index=True)
            {'image-filename': image_filename, 'percent-price-change': price_change, 'missing-values': total_isna}, ignore_index=True)

        # store percent change and image filename in dataframe

images_df.to_csv(constants.PROJECT_PATH+'/image_data_81_pixels.csv')
# fit stored percent changes in price to normal curve and report statistics
