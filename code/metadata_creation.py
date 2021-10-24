import constants

print(constants.CODE_PATH)

df = quandl.get_table("SHARADAR/SF1", ticker='AAPL', calendardate={'gte': '2019-01-01', 'lte': '2020-12-31'})

print(df)

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