from PIL import Image
import pandas as pd
import os
import constants
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width', 120)
def mrq_mrt_image(date, df, filename):
    mrq_row = df[((df['dimension'] == 'MRQ') & (df['calendardate'] == date))]
    mrt_row = df[((df['dimension'] == 'MRT') & (df['calendardate'] == date))]
    mrq_good_row = mrq_row[constants.SF1_GOOD_INDICATORS]
    mrt_good_row = mrt_row[constants.SF1_GOOD_INDICATORS]
    isna_mrq = mrq_good_row.isna().sum().sum()
    isna_mrt = mrt_good_row.isna().sum().sum()
    mrq_arr = mrq_good_row.to_numpy()[0]
    mrt_arr = mrt_good_row.to_numpy()[0]

    # mrq_arr = mrq_arr.reshape(17, 5)
    # mrt_arr = mrt_arr.reshape(17, 5)

    mrq_arr = mrq_arr.reshape(9, 9)
    mrt_arr = mrt_arr.reshape(9, 9)

    # zeros = np.zeros((17, 5), 'uint8')

    zeros = np.zeros((9, 9), 'uint8')
    zeros += 50

    rgb = np.dstack((mrq_arr, mrt_arr, zeros))
    print(rgb)

    img = Image.fromarray(rgb, mode='RGB')
    #img = img.resize((32,32))
    img.save(constants.PROJECT_PATH+'/images/'+filename, "PNG")
    plt.imsave('mptest.jpeg', rgb)
    return (isna_mrq+isna_mrt)


#for csv in os.listdir(constants.DATA_PATH+'/SF1_scaled'):
df = pd.read_csv(constants.DATA_PATH+'/SF1_scaled/AAPL_mr_scaled.csv')
date = '2017-03-31'
date2 = '2005-06-30'

mrq_mrt_image(date, df, "AAPL_test1")
#mrq_mrt_image(date2, df, "AAPL_test2")
