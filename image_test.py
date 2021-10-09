import numpy as np
from PIL import Image as im
import pandas as pd
import quandl


#Set API Key
quandl.ApiConfig.api_key = "guVoWEQKcUx8-R9JxKbp"

first_year = 1998
last_year = 2021

"""
for year in range(first_year, last_year + 1):
    data = quandl.get_table('SHARADAR/SF1', calendardate={'gte': str(year)+'-01-01','lte':str(year)+'-12-31'}, paginate=True)
    data.to_csv('/Users/johanketkar/Projects/stock-valuation-project/'+str(year)+'_SF1.csv')
"""

data = quandl.get_table('SHARADAR/SF1', calendardate={'gte': '1998-01-01','lte': '1998-12-31'}, paginate=True)
grouped_by_ticker = data.groupby('ticker')

for ticker, df in grouped_by_ticker:
    df.to_csv('/Users/johanketkar/Projects/stock-valuation-project/data/1998_SF1/1998_'+ticker+'.csv')
    



"""
print(data)

price_earnings_ratio = 27.69
price_book_ratio = 36.39
price = 141.50
dividend_yield = 0.62
free_cash_flow_quarterly = 75976
volume = 94590757
debt_asset_ratio = 0.36
peg = 2.03
earnings_per_share = 5.11


row = np.array([price_earnings_ratio, price_book_ratio, price, dividend_yield, free_cash_flow_quarterly, volume, debt_asset_ratio, peg, earnings_per_share])

rows = np.array([row, row, row, row, row, row, row, row])
#rows *= (255.0/rows.max())

#print(rows.max())

img = im.fromarray(rows) 
img = img.resize((8,24))
img = img.convert("RGBA")

#img.show()
"""