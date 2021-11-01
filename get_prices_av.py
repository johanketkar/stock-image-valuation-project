from os import error
import time
import pandas as pd
import requests

test_api = 'G4MJUGSFW8X9642T'
api_key1 = '28Q7V6VTJ9UAKHDH'
api_key2 = 'KQ7RFPMQYFBAJCDS'
api_key3 = '7CQPEIQKLFHVDUYL'

sp500 = pd.read_csv('C:/Users/nssco/OneDrive/Documents/Nick/stock-valuation-cnn/SP500_all_constituents.csv')
sp500.columns = ["index", "ticker"]
sp500.pop("index")

errors = []
clock = 0
total_clock = 0
key1_count = 0
key2_count = 0
key3_count = 0
count = 0


def get_prices(ticker, key):
    try:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + ticker + '&outputsize=full&apikey=' + key
        data = requests.get(url).json()
        data = data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(data)
        df = df.transpose()
        df.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Dividend', 'Split Coefficient']
        df.to_csv('C:/Users/nssco/OneDrive/Documents/Nick/stock-valuation-cnn/data/prices/' + ticker + '.csv')
        print(t + ' finished. ' + str(len(sp500['ticker']) - count) + ' remaining. Total time = ' + str(round(total_clock, 2)) + ' seconds')
    except Exception:
        print(ticker + ' encountered an error.')
        errors.append(ticker)


for t in sp500['ticker']:
    start = time.time_ns() / 1000000000

    if clock > 60:
        clock = 0

    if count < 350:
        if clock < 60 and (key1_count % 5 == 0) and key1_count != 0:
            print('Sleeping for: 60 seconds. API key 1 count = ' + str(key1_count))
            time.sleep(60)
            get_prices(t, api_key1)
            count += 1
            key1_count += 1
        else:
            get_prices(t, api_key1)
            count += 1
            key1_count += 1
    
    elif count < 750:
        if clock < 60 and (key2_count % 5 == 0):
            print('Sleeping for: 60 seconds. API key 2 count = ' + str(key2_count))
            time.sleep(60)
            get_prices(t, api_key2)
            count += 1
            key2_count += 1
        else:
            get_prices(t, api_key2)
            count += 1
            key2_count += 1

    elif count <= len(sp500['tickers']):
        if clock < 60 and (key3_count % 5 == 0):
            print('Sleeping for: 60 seconds. API key 3 count = ' + str(key3_count))
            time.sleep(60)
            get_prices(t, api_key3)
            count += 1
            key3_count += 1
        else:
            get_prices(t, api_key3)
            count += 1
            key3_count += 1

    end = time.time_ns() / 1000000000
    duration = end - start
    clock += duration
    total_clock += duration


print(str(len(errors)) + " tickers could not be pulled.")
print('Data for ' + str(1089 - len(errors)) + ' tickers was obtained.')
print(errors)
