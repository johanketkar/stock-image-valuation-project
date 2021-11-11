import pandas as pd
import os
import constants

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


def mrq_mrt_image(date, df):

    return 0


# for every ticker
usable_data = 0
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

        image_filename = ticker+'_'+date
        # calculate percent change in price
        price_change = percent_price_change(date, mr_df)
        # create image
        image = mrq_mrt_image(date, mr_df)

        print(ticker, date, price_change, image_filename)
        usable_data += 1
        # store percent change and image filename in dataframe

print(usable_data)
# fit stored percent changes in price to normal curve and report statistics
