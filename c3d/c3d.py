import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tensorflow import keras

from tensorflow.keras.layers import Conv3D,BatchNormalization,Add,MaxPooling3D,ZeroPadding3D,Dense,Flatten,Dropout


def c3d():
    model = keras.models.Sequential()
    
    # 1st layer group
    model.add(Conv3D(16,(3, 3, 3), activation='relu',
                            padding='same', name='conv1',
                            strides=(1, 1, 1),
                            input_shape=[32,160,160,3]))
    
    model.add(MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2),
                                   padding='valid', name='pool1'))
    # 2nd layer group
    model.add(Conv3D(16, (3, 3, 3), activation='relu',
                             padding='same', name='conv2',
                             strides=(1, 1, 1)))
    model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool2'))
    # 3rd layer group
    model.add(Conv3D(32, (3, 3, 3), activation='relu',
                             padding='same', name='conv3a',
                             strides=(1, 1, 1)))
    model.add(Conv3D(32, (3, 3, 3), activation='relu',
                             padding='same', name='conv3b',
                             strides=(1, 1, 1)))
    model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool3'))
    
    model.add(ZeroPadding3D(padding=(0, 1, 1)))
    model.add(MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool5'))
    model.add(Flatten())
    
    # FC layers group
    model.add(Dense(1024, activation='relu', name='fc6'))
    model.add(Dropout(0.5))
    model.add(Dense(1024, activation='relu', name='fc8'))
    model.add(Dropout(0.5))
    model.add(Dense(8, activation='softmax'))