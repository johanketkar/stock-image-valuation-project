import os
import pandas as pd 
import matplotlib.image as img
from PIL import Image
import constants
import numpy as np

image = img.imread(constants.IMAGE_PATH+'/1998-03-31-LVLT.png')
imag2 = img.imread(constants.IMAGE_PATH+'/2004-12-31-LVLT.png')

imag3 = img.imread(constants.IMAGE_PATH+'/2005-06-30-LVLT.png')


print(image)
print(imag2)
print(imag3)