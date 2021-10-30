import constants
import pandas as pd
import os

indicator_total_null_dict ={}
total_reports = 0
for indicator in constants.SF1_INDICATORS:
    indicator_total_null_dict[indicator] = 0

quarter_report_dates = []
yearly_report_dates = []
for year in constants.ALL_YEARS:
    q1 = str(year)+ '-' + constants.Q1_REPORT_MONTH_DAY_STRING
    q2 = str(year)+ '-' +constants.Q2_REPORT_MONTH_DAY_STRING
    q3 = str(year)+ '-' +constants.Q3_REPORT_MONTH_DAY_STRING
    q4 = str(year)+ '-' +constants.Q4_REPORT_MONTH_DAY_STRING
    yearly = str(year)+ '-' +constants.ANNUAL_REPORT_MONTH_DAY_STRING
    quarter_report_dates.append(q1)
    quarter_report_dates.append(q2)
    quarter_report_dates.append(q3)
    quarter_report_dates.append(q4)
    yearly_report_dates.append(yearly)

for t in constants.SP500_TICKERS:
    mrq_coverage = {}
    mrq_coverage['dimension'] = 'MRQ'
    mry_coverage = {}
    mry_coverage['dimension'] = 'MRY'
    mrt_coverage = {}
    mrt_coverage['dimension'] = 'MRT'

    mr_file_name = 'SF1/'+t+'/'+t+'_mr.csv'
    coverage_file_name = 'SF1/'+t+'/'+t+'_coverage.csv'
    try:
        mr_df = pd.read_csv(os.path.join(constants.DATA_PATH, mr_file_name))
    except FileNotFoundError:
        continue

    for indicator in constants.SF1_INDICATORS:
        indicator_total_null_dict[indicator] += mr_df[indicator].isna().sum()

    for date in quarter_report_dates:
        if ((mr_df['dimension'] == 'MRQ') & (mr_df['calendardate'] == date)).any():
            total_reports += 1
            mrq_coverage[date] = 1
        else:
            mrq_coverage[date] = 0
        
        if ((mr_df['dimension'] == 'MRY') & (mr_df['calendardate'] == date)).any():
            total_reports += 1
            mry_coverage[date] = 1
        else:
            mry_coverage[date] = 0
        
        if ((mr_df['dimension'] == 'MRT') & (mr_df['calendardate'] == date)).any():
            total_reports += 1
            mrt_coverage[date] = 1
        else:
            mrt_coverage[date] = 0

    mrq_coverage_df = pd.DataFrame(mrq_coverage, index = [0])
    mry_coverage_df = pd.DataFrame(mry_coverage, index = [0])
    mrt_coverage_df = pd.DataFrame(mrt_coverage, index = [0])
 
    coverage_df = mrq_coverage_df.append(mry_coverage_df).append(mrt_coverage_df)
    coverage_df.to_csv(os.path.join(constants.DATA_PATH, coverage_file_name))

indicator_percent_covered_dict = {}
for indicator in indicator_total_null_dict:
    indicator_percent_covered_dict[indicator] = 1 - indicator_total_null_dict[indicator] / total_reports

indicator_coverage_df = pd.DataFrame(indicator_percent_covered_dict, index = [0])
indicator_coverage_file_name = 'SF1/indicator_coverage.csv'
indicator_coverage_df.to_csv(os.path.join(constants.DATA_PATH), indicator_coverage_df)


    





    