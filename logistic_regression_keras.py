# -*- coding: utf-8 -*-
"""logistic_regression_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f-vL0m-4pEKes_FcusuvJbkW2-p1fajx
"""

import pandas
import numpy
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

from keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()

x_train.shape

plt.imshow(x_train[0]);

num_pixels = x_train.shape[1] * x_train.shape[2]
num_pixels



x_train = x_train.reshape(x_train.shape[0],num_pixels).astype('float32')

x_test = x_test.reshape(x_test.shape[0],num_pixels).astype('float32')

x_train /= 255
x_test /= 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_train.shape

y_test.shape

x_test.shape

x_train.shape

num_classes = y_train.shape[1]
num_classes

model = Sequential()

model.add(Dense(num_pixels,activation="relu",input_shape=(num_pixels,)))
model.add(Dense(100,activation="relu"))
model.add((Dense(num_classes,activation="softmax")))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=10,verbose=2)

score = model.evaluate(x_test,y_test,verbose=0)

print("Accuracy : {}% \n Error : {}".format(score[1],1-score[1]))

model.save('classification_model_keras.h5')

from keras.models import load_model

pre = load_model("classification_model_keras.h5")

