import os
import constants
import tensorflow as tf
from PIL import Image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam



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

pre_trained_model = tf.keras.applications.VGG16(input_shape=(224,224,3), include_top=False, weights="imagenet")

for layer in pre_trained_model.layers:
    layer.trainable = False


last_layer = pre_trained_model.get_layer('block5_pool')
last_output = last_layer.output

x = tf.keras.layers.GlobalMaxPooling2D()(last_output)
x = tf.keras.layers.Dense(512, activation='relu')(x)
x = tf.keras.layers.Dropout(0.5)(x)
x = tf.keras.layers.Dense(5, activation='softmax')(x)

model = tf.keras.Model(pre_trained_model.input, x)

model.compile(optimizer='rmsprop', loss=tf.keras.losses.categorical_crossentropy, metrics=['acc', 'mse'])

train_history = model.fit(train_data_gen, steps_per_epoch=(total_train//constants.BATCH_SIZE), epochs = 5, verbose=1)

model.save(constants.PROJECT_PATH+'/mymodel')