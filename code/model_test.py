import os
import constants
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report
import numpy as np


model = keras.models.load_model(constants.PROJECT_PATH+'/mymodel')


base_dir = constants.IMAGE_81_PIXEL_PATH

test_dir = base_dir+'/test'

image_gen_test = ImageDataGenerator(rescale=1./255)
test_data_gen = image_gen_test.flow_from_directory(batch_size=constants.BATCH_SIZE,

directory=test_dir,

shuffle=True,

target_size=(constants.IMG_SHAPE, constants.IMG_SHAPE),

class_mode='categorical')
#print(test_data_gen.class_indices)

y_test = test_data_gen.labels

y_pred = model.predict(test_data_gen, verbose=1)

predictions = np.argmax(y_pred, axis = 1)
#print(predictions)
count_0 = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for cat in predictions:
    if cat == 0:
        count_0+=1
    elif cat == 1:
        count_1+=1
    elif cat == 2:
        count_2+=1
    elif cat == 3:
        count_3+=1
    elif cat == 4:
        count_4+=1

print("Count 0", count_0)
print("Count 1", count_1)
print("Count 2", count_2)
print("Count 3", count_3)
print("Count 4", count_4)
     

print(classification_report(y_test, predictions))



