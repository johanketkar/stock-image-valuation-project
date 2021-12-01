import os
import constants
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report


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

print(classification_report(y_test, y_pred))



