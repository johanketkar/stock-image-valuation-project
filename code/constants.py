import quandl
import os
import pandas as pd

# directory paths
PROJECT_PATH = os.path.dirname(os.getcwd())
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
CODE_PATH = os.path.join(PROJECT_PATH, 'code')
IMAGE_PATH = os.path.join(PROJECT_PATH, 'images')
IMAGE_81_PIXEL_PATH = os.path.join(PROJECT_PATH,'images_81_pixels')

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

quarter_report_dates = []
yearly_report_dates = []
for year in ALL_YEARS:
    q1 = str(year) + '-' + Q1_REPORT_MONTH_DAY_STRING
    q2 = str(year) + '-' + Q2_REPORT_MONTH_DAY_STRING
    q3 = str(year) + '-' + Q3_REPORT_MONTH_DAY_STRING
    q4 = str(year) + '-' + Q4_REPORT_MONTH_DAY_STRING
    yearly = str(year) + '-' + ANNUAL_REPORT_MONTH_DAY_STRING
    quarter_report_dates.append(q1)
    quarter_report_dates.append(q2)
    quarter_report_dates.append(q3)
    quarter_report_dates.append(q4)
    yearly_report_dates.append(yearly)

QUARTERLY_REPORT_DATES = quarter_report_dates
YEARLY_REPORT_DATES = yearly_report_dates

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

# good_indicator_list = []

# for indicator in all_indicators_list:
#     percent_covered = indicator_coverage_df[indicator][0]
#     if percent_covered > .90:
#         good_indicator_list.append(indicator)

good_indicator_list = ['dps', 'sharefactor', 'shareswa', 'price', 'divyield',
                       'cor', 'gp', 'opex', 'opinc', 'revenue', 'sgna', 'intexp',
                       'taxexp', 'rnd', 'prefdivis', 'consolinc', 'ebit', 'ebt',
                       'netinc', 'netinccmn', 'netincdis', 'netincnci', 'grossmargin',
                       'netmargin', 'capex', 'ncfbus', 'ncfi', 'ncfinv', 'depamor',
                       'ncfcommon', 'ncfdebt', 'ncfdiv', 'ncff', 'ncfo', 'sbcomp',
                       'fcf', 'ncf', 'ebitda', 'ebitdamargin', 'ncfx', 'eps', 'epsusd',
                       'payoutratio', 'sps', 'fcfps', 'epsdil', 'debt', 'payables',
                       'taxliabilities', 'accoci', 'deferredrev', 'deposits', 'cashneq',
                       'receivables', 'ppnenet', 'taxassets', 'intangibles', 'inventory',
                       'investments', 'equity', 'liabilities', 'assets', 'invcap', 'tangibles',
                       'de', 'bvps', 'tbvps', 'pe1', 'ps1', 'sharesbas', 'marketcap', 'pb', 'ps',
                       'pe', 'retearn', 'ev', 'evebit', 'evebitda', 'investmentsc', 'assetsc', 'debtc']

SF1_GOOD_INDICATORS = good_indicator_list

#transfer learning
IMG_SHAPE = 32
BATCH_SIZE = 32
