import quandl
import os
import pandas as pd

# directory paths
PROJECT_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
CODE_PATH = os.path.join(PROJECT_PATH, 'code')

# quandl api key
#API_KEY = "guVoWEQKcUx8-R9JxKbp"
#quandl.ApiConfig.api_key = API_KEY

# dimensions
AR_DIMENSIONS = ['ARY', 'ARQ', 'ART']
MR_DIMENSIONS = ['MRY', 'MRQ', 'MRT']

# dates
ALL_YEARS = [1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
             2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
Q1_REPORT_MONTH_DAY_STRING = '03-31'
Q2_REPORT_MONTH_DAY_STRING = '06-30'
Q3_REPORT_MONTH_DAY_STRING = '09-30'
Q4_REPORT_MONTH_DAY_STRING = '12-31'
ANNUAL_REPORT_MONTH_DAY_STRING = '12-31'

# ticker list
sp500 = pd.read_csv(os.path.join(DATA_PATH, 'SP500_all_constituents.csv'))
sp500.columns = ["index", "ticker"]
sp500.pop("index")
SP500_TICKERS = sp500['ticker']

# SF1 indicator list
indicator_coverage_df = pd.read_csv(DATA_PATH+'/SF1/indicator_coverage.csv')
all_indicators_list = indicator_coverage_df.columns.tolist()
all_indicators_list.pop(0)
SF1_INDICATORS = all_indicators_list
good_indicator_list = []

for indicator in all_indicators_list:
    percent_covered = indicator_coverage_df[indicator][0]
    if percent_covered > .90:
        good_indicator_list.append(indicator)


SF1_GOOD_INDICATORS = good_indicator_list
