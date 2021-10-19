import pandas
import quandl
import pandas as pd

quandl.ApiConfig.api_key = "guVoWEQKcUx8-R9JxKbp"

df = quandl.get_table('SHARADAR/SP500', date={'gte': '1998-01-01', 'lte': '2021-10-15'}, paginate=True)
sp500 = pd.DataFrame(df['ticker'].unique())
sp500.columns = ["ticker"]
sp500 = sp500.sort_values(by='ticker').reset_index(drop=True)
sp500.to_csv("SP500_all_constituents.csv")