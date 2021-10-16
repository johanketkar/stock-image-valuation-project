import pandas as pd
import quandl
import numpy

quandl.ApiConfig.api_key = "guVoWEQKcUx8-R9JxKbp"

tickers = pd.read_csv("ticker_list.csv")

count = 1
for ticker in tickers["ticker"]:
    data = quandl.get_table("SHARADAR/SF1", qopts={"columns": ["ticker", "datekey", "price"]}, ticker=ticker)
    data.to_csv("Daily Tables/" + ticker + ".csv")
    print(ticker + " complete.\n" + str(count) + " of" + str(len(tickers)) + " complete.\n" + str(round(count / len(tickers) * 100)) + "omplete.")
    count+=1

