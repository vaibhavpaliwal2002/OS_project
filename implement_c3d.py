from gen_csv import create_csv
from df import generate_df
from dataloader import data_loader
from c3d import c3d
from c3d import c3d
from tensoorflow import keras
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt


classes = {"Abuse":0,"Arrest":1,'Arson':2,'Assault':3,'Burglary':4,'Explosion':5,'Fighting':6,'Normal':7}

create_csv.create_csv()
df = generate_df.generate_df()


model = c3d.c3d()
model.compile(optimizer='adam', loss='categorical_crossentropy')
model.summary()
keras.utils.plot_model(model)


train = data_loader.data_loader_train(df)
valid = data_loader.data_loader_valid(df)

with tf.device('/GPU:0'):
    model_his = model.fit_generator(train,
                                16,
                                5,
                               validation_data=valid,
                               validation_steps=59)
    

pd.DataFrame(model_his.history).plot()
plt.gca().set_ylim(0,1)
