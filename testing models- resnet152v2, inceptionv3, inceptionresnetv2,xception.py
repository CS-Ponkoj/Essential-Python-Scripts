#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow.keras.layers import Flatten, Dense, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.applications.resnet_v2 import ResNet152V2
from tensorflow.keras import applications
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow import device
from matplotlib import pyplot
from PIL import ImageFile
import sys
from keras_preprocessing.image import ImageDataGenerator
import os


# In[2]:


def min_image_count():
    root = "D:/Image Classifier/feature_images/"
    datasets = ["train/", "test/"]
    features = ["bathroom/", "bedroom/", "dining_room/", "exterior/", "kitchen/", "living_room/"]

    train_count = None
    test_count = None

    for i, dataset in enumerate(datasets):

        val = 1000000
        for feature in features:
            dir_path = root + dataset + feature
            files = os.listdir(dir_path)
            image_count = len(files)
            print(dataset, feature, image_count)

            if image_count < val:
                val = image_count - 1

        if i == 0:
            train_count = val
        elif i == 1:
            test_count = val

    return [train_count, test_count]


# In[3]:


min_image_count()


# In[4]:


def get_generators(shuffle):
    train_datagen = ImageDataGenerator(rescale=1.0 / 255.0)
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    if shuffle:
        train_datagen = ImageDataGenerator(rescale=1.0/255.0, width_shift_range=0.1,
                                           height_shift_range=0.1, horizontal_flip=True)

    train_it = train_datagen.flow_from_directory("D:/Image Classifier/feature_images/train", class_mode="categorical",
                                                 batch_size=32, target_size=(128, 128), shuffle=shuffle)

    test_it = test_datagen.flow_from_directory("D:/Image Classifier/feature_images/test", class_mode="categorical", batch_size=32,
                                               target_size=(128, 128), shuffle=shuffle)

    return train_it, test_it


# In[5]:


train_it,test_it = get_generators(shuffle=True)


# In[ ]:


train_it


# In[ ]:


test_it


# # ResNet152V2

# In[ ]:


model = ResNet152V2(include_top=False, input_shape=(128, 128, 3))
for layer in model.layers:
    layer.trainable = False

dropout = Dropout(0.1)(model.layers[-1].output)
flat = Flatten()(dropout)
dense = Dense(128, activation="relu", kernel_initializer="he_uniform")(flat)
dropout = Dropout(0.05)(dense)
dense = Dense(64)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(48)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(36)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(24)(dropout)
dense = Dense(12)(dense)
output = Dense(6, activation="softmax")(dense)

model = Model(inputs=model.inputs, outputs=output)
model.compile(optimizer="nadam", loss="categorical_crossentropy", metrics="accuracy")





ImageFile.LOAD_TRUNCATED_IMAGES = True



es = EarlyStopping(monitor="val_accuracy", min_delta=0.005, verbose=1, patience=2, restore_best_weights=True)

train_it, test_it = get_generators(True)

history = model.fit(train_it, steps_per_epoch=len(train_it), callbacks=[es],
                    validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=1)

_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)

model.save("models/ImageClassifier.h5")
print("Finished training")
print('> %.3f' % (acc * 100.0))


# # InceptionV3

# In[ ]:




model = applications.inception_v3.InceptionV3(include_top=False, input_shape=(128, 128, 3))
for layer in model.layers:
    layer.trainable = False

dropout = Dropout(0.1)(model.layers[-1].output)
flat = Flatten()(dropout)
dense = Dense(128, activation="relu", kernel_initializer="he_uniform")(flat)
dropout = Dropout(0.05)(dense)
dense = Dense(64)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(48)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(36)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(24)(dropout)
dense = Dense(12)(dense)
output = Dense(6, activation="softmax")(dense)

model = Model(inputs=model.inputs, outputs=output)
model.compile(optimizer="nadam", loss="categorical_crossentropy", metrics="accuracy")




ImageFile.LOAD_TRUNCATED_IMAGES = True


es = EarlyStopping(monitor="val_accuracy", min_delta=0.005, verbose=1, patience=2, restore_best_weights=True)

train_it, test_it = get_generators(True)

history = model.fit(train_it, steps_per_epoch=len(train_it), callbacks=[es],
                    validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=1)

_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)

model.save("models/ImageClassifier.h5")
print("Finished training")
print('> %.3f' % (acc * 100.0))



# # InceptionResNetV2

# In[7]:


model = applications.InceptionResNetV2(include_top=False, input_shape=(128, 128, 3))
for layer in model.layers:
    layer.trainable = False

dropout = Dropout(0.1)(model.layers[-1].output)
flat = Flatten()(dropout)
dense = Dense(128, activation="relu", kernel_initializer="he_uniform")(flat)
dropout = Dropout(0.05)(dense)
dense = Dense(64)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(48)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(36)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(24)(dropout)
dense = Dense(12)(dense)
output = Dense(6, activation="softmax")(dense)

model = Model(inputs=model.inputs, outputs=output)
model.compile(optimizer="nadam", loss="categorical_crossentropy", metrics="accuracy")




ImageFile.LOAD_TRUNCATED_IMAGES = True


es = EarlyStopping(monitor="val_accuracy", min_delta=0.005, verbose=1, patience=2, restore_best_weights=True)

train_it, test_it = get_generators(True)

history = model.fit(train_it, steps_per_epoch=len(train_it), callbacks=[es],
                    validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=1)

_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)

model.save("models/ImageClassifier.h5")
print("Finished training")
print('> %.3f' % (acc * 100.0))


# # Xception

# In[ ]:


model = applications.Xception(include_top=False, input_shape=(128, 128, 3))
for layer in model.layers:
    layer.trainable = False

dropout = Dropout(0.1)(model.layers[-1].output)
flat = Flatten()(dropout)
dense = Dense(128, activation="relu", kernel_initializer="he_uniform")(flat)
dropout = Dropout(0.05)(dense)
dense = Dense(64)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(48)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(36)(dropout)
dropout = Dropout(0.05)(dense)
dense = Dense(24)(dropout)
dense = Dense(12)(dense)
output = Dense(6, activation="softmax")(dense)

model = Model(inputs=model.inputs, outputs=output)
model.compile(optimizer="nadam", loss="categorical_crossentropy", metrics="accuracy")




ImageFile.LOAD_TRUNCATED_IMAGES = True


es = EarlyStopping(monitor="val_accuracy", min_delta=0.005, verbose=1, patience=2, restore_best_weights=True)

train_it, test_it = get_generators(True)

history = model.fit(train_it, steps_per_epoch=len(train_it), callbacks=[es],
                    validation_data=test_it, validation_steps=len(test_it), epochs=10, verbose=1)

_, acc = model.evaluate(test_it, steps=len(test_it), verbose=0)

model.save("models/ImageClassifier.h5")
print("Finished training")
print('> %.3f' % (acc * 100.0))

