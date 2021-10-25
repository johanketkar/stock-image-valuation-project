import constants
import quandl
import pandas as pd
import os

df = quandl.get_table("SHARADAR/INDICATORS", table='SF1')
indicator_list = df['indicator'].tolist()
need_to_remove = ['ticker', 'dimension', 'calendardate', 'datekey', 'reportperiod', 'lastupdated']

for x in need_to_remove:
    indicator_list.remove(x)

indicator_list.sort()


#get list of all indicators (columns)

#get list of all quarter report dates (rows for quarterly_coverage)


#get list of all years (rows for yearly_coverage)

#create three dataframes of zeros
    #quarterly_coverage
    #yearly_coverage
    #trailing_coverage

#loop through every ticker and correspodning mr csv 
    #for every row 
        #store dimension and calendardate
        #for every item in row
            #if item is not nan then update corresponding coverage dataframe item to 1
sp500 = pd.read_csv(os.path.join(constants.DATA_PATH,'SP500_all_constituents.csv'))
sp500.columns = ["index", "ticker"]
sp500.pop("index")


for t in sp500['ticker']:
    file_name = 'SF1/'+t+'/'+t+'_mr.csv'
    mr_df = pd.read_csv(os.path.join(constants.DATA_PATH, file_name))
    