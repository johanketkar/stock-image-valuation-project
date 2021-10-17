from datetime import date
import pandas as pd
import quandl
import numpy as np
import os

quandl.ApiConfig.api_key = "guVoWEQKcUx8-R9JxKbp"

'''
df = quandl.get_table('SHARADAR/SP500', date={'gte': '1998-01-01', 'lte': '2021-10-15'}, paginate=True)
sp500 = pd.DataFrame(df['ticker'].unique())
sp500.columns = ["ticker"]
sp500 = sp500.sort_values(by='ticker').reset_index(drop=True)
sp500.to_csv("SP500_all_constituents.csv")
'''

sp500 = pd.read_csv("C:/Users/nssco/OneDrive/Documents/Nick/stock-valuation-cnn/SP500_all_constituents.csv")
sp500.columns = ["index", "ticker"]
sp500.pop("index")

# sp500 = pd.DataFrame(columns=['ticker'])
# sp500.ticker = ['A', 'AAL', 'AAMRQ', 'AAP', 'BBI1', 'AAPL']

coverage = sp500
coverage["Begin Date"] = np.nan
coverage["End Date"] = np.nan

coverage["ARY_start"] = np.nan
coverage["ARY_end"] = np.nan
coverage["ARY_count"] = np.nan
coverage["ARY_exp_count"] = np.nan

coverage["MRY_start"] = np.nan
coverage["MRY_end"] = np.nan
coverage["MRY_count"] = np.nan
coverage["MRY_exp_count"] = np.nan

coverage["ARQ_start"] = np.nan
coverage["ARQ_end"] = np.nan
coverage["ARQ_count"] = np.nan
coverage["ARQ_exp_count"] = np.nan

coverage["MRQ_start"] = np.nan
coverage["MRQ_end"] = np.nan
coverage["MRQ_count"] = np.nan
coverage["MRQ_exp_count"] = np.nan

coverage["ART_start"] = np.nan
coverage["ART_end"] = np.nan
coverage["ART_count"] = np.nan
coverage["ART_exp_count"] = np.nan

coverage["MRT_start"] = np.nan
coverage["MRT_end"] = np.nan
coverage["MRT_count"] = np.nan
coverage["MRT_exp_count"] = np.nan

coverage["1998_Missing"] = np.nan
coverage["1999_Missing"] = np.nan
coverage["2000_Missing"] = np.nan
coverage["2000_Missing"] = np.nan
coverage["2001_Missing"] = np.nan
coverage["2002_Missing"] = np.nan
coverage["2003_Missing"] = np.nan
coverage["2004_Missing"] = np.nan
coverage["2005_Missing"] = np.nan
coverage["2006Missing"] = np.nan
coverage["2007_Missing"] = np.nan
coverage["2008_Missing"] = np.nan
coverage["2009_Missing"] = np.nan
coverage["2011_Missing"] = np.nan
coverage["2012_Missing"] = np.nan
coverage["2013_Missing"] = np.nan
coverage["2014_Missing"] = np.nan
coverage["2015_Missing"] = np.nan
coverage["2016_Missing"] = np.nan
coverage["2017_Missing"] = np.nan
coverage["2018_Missing"] = np.nan
coverage["2019_Missing"] = np.nan
coverage["2020_Missing"] = np.nan


# df = quandl.get_table('SHARADAR/SF1', ticker='BBI1', calendardate={'gte': '1998-01-01', 'lte': '2020-12-31'})
# print(df.empty)
# start_year = df.calendardate.min().date()
# end_year = df.calendardate.max().year
# year_df = df[df.calendardate.dt.year == 2019]
# fy_df = year_df[(year_df.dimension == 'MRY') | (year_df.dimension == 'ARY')].reset_index(drop=True)
# q1_df = year_df[df.calendardate.dt.month == 3].reset_index(drop=True)
# q2_df = year_df[df.calendardate.dt.month == 6].reset_index(drop=True)
# q3_df = year_df[df.calendardate.dt.month == 9].reset_index(drop=True)
# q4_df = year_df[(df.calendardate.dt.month == 12) & ((year_df.dimension != 'MRY') & (year_df.dimension != 'ARY'))].reset_index(drop=True)
# print(year_df)
# print(fy_df)
# print(q1_df)
# print(q2_df)
# print(q3_df)
# print(q4_df)

# test_list = ['A', 'AAL', 'AAMRQ', 'AAP', 'AAPL']

# coverage.loc[[0], ['2020_Missing']].append(("test", "test23"))

# print(coverage.head)
# print(coverage.loc[[0], ['2020_Missing']])


for t in sp500['ticker']:
    df = quandl.get_table("SHARADAR/SF1", ticker=t, calendardate={'gte': '1998-01-01', 'lte': '2020-12-31'})

    if df.empty:
        continue

    ticker_path = os.path.join('C:/Users/nssco/OneDrive/Documents/Nick/stock-valuation-cnn/data/SF1', t)
    os.mkdir(ticker_path)

    coverage.loc[[list(sp500['ticker']).index(t)], ['Begin Date']] = df.calendardate.min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['End Date']] = df.calendardate.max().date()

    coverage.loc[[list(sp500['ticker']).index(t)], ['ARY_start']] = df.calendardate[df.dimension == 'ARY'].min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRY_start']] = df.calendardate[df.dimension == 'MRY'].min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['ARQ_start']] = df.calendardate[df.dimension == 'ARQ'].min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRQ_start']] = df.calendardate[df.dimension == 'MRQ'].min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['ART_start']] = df.calendardate[df.dimension == 'ART'].min().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRT_start']] = df.calendardate[df.dimension == 'MRT'].min().date()

    coverage.loc[[list(sp500['ticker']).index(t)], ['ARY_end']] = df.calendardate[df.dimension == 'ARY'].max().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRY_end']] = df.calendardate[df.dimension == 'MRY'].max().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['ARQ_end']] = df.calendardate[df.dimension == 'ARQ'].max().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRQ_end']] = df.calendardate[df.dimension == 'MRQ'].max().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['ART_end']] = df.calendardate[df.dimension == 'ART'].max().date()
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRT_end']] = df.calendardate[df.dimension == 'MRT'].max().date()

    coverage.loc[[list(sp500['ticker']).index(t)], ['ARY_count']] = len(df[df.dimension == 'ARY'])
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRY_count']] = len(df[df.dimension == 'MRY'])
    coverage.loc[[list(sp500['ticker']).index(t)], ['ARQ_count']] = len(df[df.dimension == 'ARQ'])
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRQ_count']] = len(df[df.dimension == 'MRQ'])
    coverage.loc[[list(sp500['ticker']).index(t)], ['ART_count']] = len(df[df.dimension == 'ART'])
    coverage.loc[[list(sp500['ticker']).index(t)], ['MRT_count']] = len(df[df.dimension == 'MRT'])

    start_year = df.calendardate.min().year
    end_year = df.calendardate.max().year
    years = list(range(start_year, end_year+1, 1))

    for y in years:
        ticker_year_path = os.path.join(ticker_path, str(y))
        os.mkdir(ticker_year_path)

        year_df = df[df.calendardate.dt.year == y]
        fy_df = year_df[(year_df.dimension == 'MRY') | (year_df.dimension == 'ARY')].reset_index(drop=True)
        q1_df = year_df[df.calendardate.dt.month == 3].reset_index(drop=True)
        q2_df = year_df[df.calendardate.dt.month == 6].reset_index(drop=True)
        q3_df = year_df[df.calendardate.dt.month == 9].reset_index(drop=True)
        q4_df = year_df[(df.calendardate.dt.month == 12) & ((year_df.dimension != 'MRY') & (year_df.dimension != 'ARY'))].reset_index(drop=True)

        missing = ""
        coverage_string = str(y) + "_Missing"

        if fy_df.empty:
            missing = missing + '_FY'
        if q1_df.empty:
            mmissing = missing + '_Q1'
        if q2_df.empty:
            missing = missing + '_Q2'
        if q3_df.empty:
            missing = missing + '_Q3'
        if q4_df.empty:
            missing = missing + '_Q4'

        fy_df.to_csv(ticker_year_path + '/' + t + '_fy_' + str(y) + '.csv')
        q1_df.to_csv(ticker_year_path + '/' + t + '_Q1_' + str(y) + '.csv')
        q2_df.to_csv(ticker_year_path + '/' + t + '_Q2_' + str(y) + '.csv')
        q3_df.to_csv(ticker_year_path + '/' + t + '_Q3_' + str(y) + '.csv')
        q4_df.to_csv(ticker_year_path + '/' + t + '_Q4_' + str(y) + '.csv')

        coverage.loc[[list(sp500['ticker']).index(t)], [coverage_string]] = missing

    print(t + " finished " + str(len(list(sp500['ticker'])) - list(sp500['ticker']).index(t) - 1) + " remaining")


coverage.to_csv('C:/Users/nssco/OneDrive/Documents/Nick/stock-valuation-cnn/data/coverage_by_ticker.csv')
# print(coverage)

