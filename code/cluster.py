import os
from pandas.core.frame import DataFrame
import constants
import os
import numpy as np
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
import pickle
from keras.preprocessing.image import load_img 
from keras.preprocessing.image import img_to_array 
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import VGG16 
from keras.models import Model
import time
import datetime
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

start_time = time.time()

images = []

df = pd.read_csv(constants.PROJECT_PATH + '\image_data.csv')

for idx, row in df.iterrows():
    if row['image-for-training'] == 0:
        images.append(os.path.join(constants.IMAGE_PATH, 'test', row['label'], row['image-filename']))
    else:
        images.append(os.path.join(constants.IMAGE_PATH, 'train', row['label'], row['image-filename']))



model = VGG16()
model = Model(inputs = model.inputs, outputs = model.layers[-2].output)


def extract_features(file, model):
    img = load_img(file, target_size=(224,224))
    img = np.array(img)

    reshaped_image = img.reshape(1,224,224,3)

    imgx = preprocess_input(reshaped_image)

    features = model.predict(imgx, use_multiprocessing=True)

    return features


data = {}
count = 1
len_range = list(range(1, len(images), int(len(images) * 0.05)))

for image in images:
    feat = extract_features(image, model)
    data[image] = feat
    if count in len_range:
        print(str(int(count / len(images) * 100)) + '% complete. ' + str(len(images) - count) + ' remaining. ' + datetime.datetime.now().strftime('%H:%M:%S') + ' - ' + str(round(time.time() - start_time, 2)))
    count += 1

# DataFrame(data).to_csv(constants.PROJECT_PATH + '\extracted_features.csv')

print('Feature extraction complete.')

filenames = np.array(list(data.keys()))

feat = np.array(list(data.values()))

feat = feat.reshape(-1, 4096)

label = df['label'].tolist()
unique_labels = list(set(label))

# pca = PCA(n_components=100, random_state=22)
# pca.fit(feat)
# x = pca.transform(feat)

# kmeans = KMeans(n_clusters=len(unique_labels),n_jobs=-1, random_state=22)
# kmeans.fit(x)

# groups = {}
# for file, cluster in zip(filenames,kmeans.labels_):
#     if cluster not in groups.keys():
#         groups[cluster] = []
#         groups[cluster].append(file)
#     else:
#         groups[cluster].append(file)


# def view_cluster(cluster):
#     plt.figure(figsize = (25,25));
#     files = groups[cluster]
#     if len(files) > 30:
#         print(f"Clipping cluster size from {len(files)} to 30")
#         files = files[:29]
#     for index, file in enumerate(files):
#         plt.subplot(10,10,index+1);
#         img = load_img(file)
#         img = np.array(img)
#         plt.imshow(img)
#         plt.axis('off')


sse = []
list_k = list(range(3, 23))
min_inertia = 999999999999999.9999

groups = {}
labels = []

for k in list_k:
    km = KMeans(n_clusters=k, random_state=22)
    km.fit(feat)
    
    sse.append(km.inertia_)

    # if km.inertia_ < min_inertia:
    #     min_inertia = km.inertia_

    #     labels = km.labels_

    col_name = 'k_number_' + str(k)

    df[col_name] = km.labels_
    
    print('K Means ' + str(k) + ' complete')

print(sse)

df.to_csv(constants.PROJECT_PATH + '\\new_image_data.csv')

# for file, cluster in zip(filenames, labels):
#     if cluster not in groups.keys():
#         groups[cluster] = []
#         groups[cluster].append(file)
#     else:
#         groups[cluster].append(file)


# DataFrame(groups).to_csv(constants.PROJECT_PATH + '\clustering.csv')
# print(groups)


# plt.figure(figsize=(6, 6))
# plt.plot(list_k, sse)
# plt.xlabel(r'Number of clusters *k*')
# plt.ylabel('Sum of squared distance');

