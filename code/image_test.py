import os
import pandas as pd
import numpy as np
import constants
from PIL import Image

date = '2005-06-30'
mr_df = pd.read_csv(constants.DATA_PATH+'/SF1/AAPL/AAPL_mr.csv')
filename = 'AAPL_2005-06-30.png'


def mrq_mrt_image(date, df, filename):
    mrq_row = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date))]
    mrt_row = df[((df['dimension'] == 'MRT') & (df['calendardate'] == date))]
    mrq_good_row = mrq_row[constants.SF1_GOOD_INDICATORS]
    mrt_good_row = mrt_row[constants.SF1_GOOD_INDICATORS]
    mrq_arr = mrq_good_row.to_numpy()[0]
    mrt_arr = mrt_good_row.to_numpy()[0]

    mrq_arr = mrq_arr.reshape(17, 5)
    mrt_arr = mrt_arr.reshape(17, 5)

    zeros = np.zeros((17, 5), 'uint8')

    rgb = np.dstack((mrq_arr, mrt_arr, zeros))

    img = Image.fromarray(rgb, mode='RGB')
    img.save(constants.PROJECT_PATH+'/images/'+filename, "PNG")

    return 1


img = mrq_mrt_image(date, mr_df, filename)

img.show()
