import keras,os
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D , Flatten
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import constants

base_dir = constants.IMAGE_PATH

train_dir = base_dir+'/train'
train_ex_overvalued_dir = train_dir+'/extremely_overvalued'
train_overvalued_dir = train_dir+'/overvalued'
train_neutral_dir = train_dir+'/neutral'
train_undervalued_dir = train_dir+'/undervalued'
train_ex_undervalued_dir = train_dir+'/extremely_undervalued'

test_dir = base_dir+'/test'
test_ex_overvalued_dir = test_dir+'/extremely_overvalued'
test_overvalued_dir = test_dir+'/overvalued'
test_neutral_dir = test_dir+'/neutral'
test_undervalued_dir = test_dir+'/undervalued'
test_ex_undervalued_dir = test_dir+'/extremely_undervalued'

num_ex_overvalued_train = len(os.listdir(train_ex_overvalued_dir))
num_overvalued_train = len(os.listdir(train_overvalued_dir))
num_neutral_train = len(os.listdir(train_neutral_dir))
num_undervalued_train = len(os.listdir(train_undervalued_dir))
num_ex_undervalued_train = len(os.listdir(train_ex_undervalued_dir))
total_train = num_ex_overvalued_train+num_overvalued_train+num_neutral_train+num_undervalued_train+num_ex_undervalued_train

num_ex_overvalued_test = len(os.listdir(test_ex_overvalued_dir))
num_overvalued_test = len(os.listdir(test_overvalued_dir))
num_neutral_test = len(os.listdir(test_neutral_dir))
num_undervalued_test = len(os.listdir(test_undervalued_dir))
num_ex_undervalued_test = len(os.listdir(test_ex_undervalued_dir))
total_test = num_ex_overvalued_test+num_overvalued_test+num_neutral_test+num_undervalued_test+num_ex_undervalued_test

print("# of Training extremely overvalued images: ", num_ex_overvalued_train)
print("# of Training overvalued images: ", num_overvalued_train)
print("# of Training neutral images: ", num_neutral_train)
print("# of Training undervalued images: ", num_undervalued_train)
print("# of Training extremely undervalued images: ", num_ex_undervalued_train)
print("TOTAl Training images: ", total_train)

print("--")

print("# of Testing extremely overvalued images: ", num_ex_overvalued_test)
print("# of Testing overvalued images: ", num_overvalued_test)
print("# of Testing neutral images: ", num_neutral_test)
print("# of Testing undervalued images: ", num_undervalued_test)
print("# of Testing extremely undervalued images: ", num_ex_undervalued_test)
print("TOTAl Testing images: ", total_test)



image_gen_train = ImageDataGenerator(rescale=1./255)
train_data_gen = image_gen_train.flow_from_directory(batch_size=constants.BATCH_SIZE,

directory=train_dir,

shuffle=True,

target_size=(constants.IMG_SHAPE, constants.IMG_SHAPE),

class_mode='categorical')


model = Sequential()
model.add(Conv2D(input_shape=(32,32,3),filters=64,kernel_size=(3,3),padding="same", activation="relu"))
model.add(Conv2D(filters=64,kernel_size=(3,3),padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=128, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=256, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(Conv2D(filters=512, kernel_size=(3,3), padding="same", activation="relu"))
model.add(MaxPool2D(pool_size=(2,2),strides=(2,2)))

model.add(Flatten())
model.add(Dense(units=4096,activation="relu"))
model.add(Dense(units=4096,activation="relu"))
model.add(Dense(units=5, activation="softmax"))

model.compile(optimizer='rmsprop', loss=keras.losses.categorical_crossentropy, metrics=['acc', 'mse'])
train_history = model.fit(train_data_gen, steps_per_epoch=(total_train//constants.BATCH_SIZE), epochs = 5, verbose=1)
