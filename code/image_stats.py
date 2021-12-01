from pandas.core.frame import DataFrame
import constants
import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split

image_data = pd.read_csv(os.path.join(constants.PROJECT_PATH, 'image_data_81_pixels.csv'), index_col=0)
image_data = DataFrame(image_data)
image_data = image_data[image_data['percent-price-change'].isnull() == False]
image_data = image_data[image_data['missing-values'] <= 1]
# image_data = image_data[image_data['percent-price-change'] <= 1.55]

image_data.reset_index(drop=True, inplace=True)

mean = np.mean(image_data['percent-price-change'])
std_dev = np.std(image_data['percent-price-change'])

cutoff_1_2 = mean - 1.5 * std_dev
cutoff_2_3 = mean - 0.5 * std_dev
cutoff_3_4 = mean + 0.5 * std_dev
cutoff_4_5 = mean + 1.5 * std_dev

images_path = os.path.join(constants.PROJECT_PATH, 'images_81_pixels')
files = os.listdir(images_path)

count = 1
for f in files:
    if f not in image_data['image-filename'].values:
        os.remove(os.path.join(images_path, f))
        print(f + ' removed - ' + str(count) + ' total files removed')
        count += 1

os.mkdir(images_path + '/train')
os.mkdir(images_path + '/test')
os.mkdir(images_path + '/train/extremely_undervalued')
os.mkdir(images_path + '/train/undervalued')
os.mkdir(images_path + '/train/neutral')
os.mkdir(images_path + '/train/overvalued')
os.mkdir(images_path + '/train/extremely_overvalued')
os.mkdir(images_path + '/test/extremely_undervalued')
os.mkdir(images_path + '/test/undervalued')
os.mkdir(images_path + '/test/neutral')
os.mkdir(images_path + '/test/overvalued')
os.mkdir(images_path + '/test/extremely_overvalued')

image_train, image_test = train_test_split(image_data, test_size=0.2)

image_data['image-for-training'] = 0
image_data['label'] = ''

def move_image(name, path, value, train_or_test, index):
    if value < cutoff_1_2:
        cat = 'extremely_overvalued'
    elif cutoff_1_2 <= value < cutoff_2_3:
        cat = 'overvalued'
    elif cutoff_2_3 <= value <= cutoff_3_4:
        cat = 'neutral'
    elif cutoff_3_4 < value < cutoff_4_5:
        cat = 'undervalued'
    elif value > cutoff_4_5:
        cat = 'extremely_undervalued'

    image_data.iloc[index, 4] = cat
    new_path = os.path.join(images_path, train_or_test, cat, name)
    os.rename(path, new_path)


for i in range(len(image_data)):
    name = image_data.iloc[i, 0]
    pct_change = image_data.iloc[i, 1]
    current_path = os.path.join(images_path, name)

    if name in image_test['image-filename'].values:
        move_image(name, current_path, pct_change, 'test', i)
    else:
        image_data.iloc[i, 3] = 1
        move_image(name, current_path, pct_change, 'train', i)

    print(str(i) + ' complete')


os.remove(constants.PROJECT_PATH + '/image_data_81_pixels.csv')
image_data.to_csv(constants.PROJECT_PATH+'/image_data_81_pixels.csv')