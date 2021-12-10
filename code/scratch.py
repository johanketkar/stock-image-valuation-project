import os
import pandas as pd 
from PIL import Image
import constants
import numpy as np

image = Image.open(constants.IMAGE_PATH+'/AAPL_test1')

image_sequence = image.getdata()

image_array = np.array(image_sequence)

print(image_array)