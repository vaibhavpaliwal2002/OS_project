import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

from tensorflow.keras.layers import Conv3D 

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

from tensorflow.keras.layers import Conv3D , MaxPooling3D , ZeroPadding3D , Dense , Dropout , Flatten


def py_slowfast():
    inp_slow = tf.keras.layers.Input(shape = (4, 160, 160, 3))
    inp_fast = tf.keras.layers.Input(shape = (32, 160, 160, 3))
    
    
    # 1st layer group
    fast = Conv3D(16,(3, 3, 3), activation='relu',
                            padding='same', name='conv1',
                            strides=(1, 1, 1))(inp_fast)
    
    fast = MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2),
                                   padding='valid', name='pool1')(fast)
    
    slow = Conv3D(16,(3, 3, 3), activation='sigmoid',
                            padding='same', name='conv1s',
                            strides=(1, 1, 1))(inp_slow)
    
    slow = MaxPooling3D(pool_size=(1, 2, 2), strides=(1, 2, 2),
                                   padding='valid', name='pool1s')(slow)
    
    
    # 2nd layer group
    fast = Conv3D(16, (3, 3, 3), activation='relu',
                             padding='same', name='conv2',
                             strides=(1, 1, 1))(fast)
    fast = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool2')(fast)
    
    slow = Conv3D(16, (3, 3, 3), activation='sigmoid',
                             padding='same', name='conv2s',
                             strides=(1, 1, 1))(slow)
    slow = MaxPooling3D(pool_size=(2, 2, 2), strides=(1, 2, 2),
                                   padding='valid', name='pool2s')(slow)
    
    
    # 3rd layer group
    fast = Conv3D(32, (3, 3, 3), activation='relu',
                             padding='same', name='conv3a',
                             strides=(1, 1, 1))(fast)
    
    fast = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool3')(fast)
    
    slow = Conv3D(32, (3, 3, 3), activation='sigmoid',
                             padding='same', name='conv3as',
                             strides=(1, 1, 1))(slow)
    
    slow = MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool3s')(slow)
    
    model = tf.keras.layers.concatenate([fast, slow], axis = 1)
    
    model= ZeroPadding3D(padding=(0, 1, 1))(model)
    model= MaxPooling3D(pool_size=(2, 2, 2), strides=(2, 2, 2),
                                   padding='valid', name='pool5')(model)
    
    
    
    model = Flatten()(model)
    
    # FC layers group
    model= Dense(1024, activation='relu', name='fc6')(model)
    model= Dropout(0.5)(model)
    model= Dense(1024, activation='relu', name='fc8')(model)
    model= Dropout(0.5)(model)
    model= Dense(8, activation='softmax')(model)
    
    model = tf.keras.models.Model(inputs = [inp_fast,inp_slow], outputs = [model])
    
    return model