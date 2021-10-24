from datetime import date
import pandas as pd
import quandl
import numpy as np
import os
import constants

sp500 = pd.read_csv(os.path.join(constants.DATA_PATH,'SP500_all_constituents.csv'))
sp500.columns = ["index", "ticker"]
sp500.pop("index")


for t in sp500['ticker']:
    df = quandl.get_table("SHARADAR/SF1", ticker=t, calendardate={'gte': '1998-01-01', 'lte': '2020-12-31'})

    if df.empty:
        continue

    ticker_path = os.path.join(constants.DATA_PATH, 'SF1/'+t)
    os.mkdir(ticker_path)

    ar = pd.DataFrame()
    mr = pd.DataFrame()

    for d in constants.AR_DIMENSIONS:
        df =  quandl.get_table("SHARADAR/SF1", ticker=t, dimension=d, paginate=True)
        ar = ar.append(df)
        
    for d in constants.MR_DIMENSIONS:
        df =  quandl.get_table("SHARADAR/SF1", ticker=t, dimension=d, paginate=True)
        mr = mr.append(df)


    mr.to_csv(ticker_path+'/'+t+'_mr.csv')
    ar.to_csv(ticker_path+'/'+t+'_ar.csv')