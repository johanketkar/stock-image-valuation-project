import os
import pandas as pd 
import constants 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler

#First create one big dataframe with all rows we will use
#Then scale each column 
#Then create new csvs for each ticker

data_dir = constants.DATA_PATH+'/SF1'

all_mr = pd.DataFrame()

for t in constants.SP500_TICKERS:
    try:
        mr = pd.read_csv(data_dir+'/'+t+'/'+t+'_mr.csv')
        all_mr = all_mr.append(mr)
    except FileNotFoundError:
        continue


all_mr_scaled = pd.DataFrame()

all_mr_scaled[['ticker', 'dimension', 'calendardate']] = all_mr[['ticker', 'dimension', 'calendardate']]

scaler = MinMaxScaler(feature_range=(0,1))
for indicator in constants.SF1_GOOD_INDICATORS:
    all_mr_scaled[[indicator]] = scaler.fit_transform(all_mr[[indicator]])


scaled_grouped = all_mr_scaled.groupby('ticker')

for ticker, group in scaled_grouped:
    group.to_csv(constants.DATA_PATH+'/SF1_scaled/'+ticker+'_mr_scaled.csv')


# print(all_mr_scaled[['dps']])
# print(all_mr_scaled['dps'].max())
# print(all_mr_scaled['dps'].mean())
# print(all_mr_scaled['dps'].median())
# print(all_mr_scaled['dps'].min())

# print('--')

# print(all_mr[['dps']])
# print(all_mr['dps'].max())
# print(all_mr['dps'].mean())
# print(all_mr['dps'].median())
# print(all_mr['dps'].min())