import pandas as pd
import numpy as np
from PIL import Image




q1_df = pd.read_csv('/Users/johanketkar/Projects/stock-valuation-project/data/SF1/AAPL/2005/AAPL_Q1_2005.csv').fillna(0)
y_df = pd.read_csv('/Users/johanketkar/Projects/stock-valuation-project/data/SF1/AAPL/2005/AAPL_fy_2005.csv').fillna(0)

mrq = q1_df.loc[q1_df['dimension'] == 'MRQ'].to_numpy()[0]
mrt = q1_df.loc[q1_df['dimension'] == 'MRT'].to_numpy()[0]
mry = y_df.loc[y_df['dimension'] == 'MRY'].to_numpy()[0]

mrq = mrq[7:]
mrt = mrt[7:]
mry = mry[7:]

mrq = mrq.reshape(15,7)
mrt = mrt.reshape(15,7)
mry = mry.reshape(15,7)
zeros = np.zeros((15,7), 'uint8')
print(mrq)
print(len(mrt))
print(len(mry))

rgb = np.dstack((mrq, mrt, mry)).astype('uint8')


img = Image.fromarray(rgb, mode='RGB')

img.show()


