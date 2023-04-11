import cv2 as cv
import torchvision as tv
import torch
import numpy as np


def data_loader_train(df,batch=32,train_size=0.8):
    df = df.sample(frac=1).reset_index(drop=True)
    while True:
        length = int(len(df.index)*train_size)
        sample = df[:length].sample(n=32)
        address = list(sample['FileAddress'])
        label = list(sample['label'])
        
        cap = np.zeros((batch,32,160,160,3),dtype='float32')
        cat = np.zeros((batch,8),dtype='float32')
        cap_2 = np.zeros((batch,4,160,160,3),dtype='float32')
        
        for j,i in enumerate(address):
            
            cap_temp = tv.io.read_video(i)[0]
            cap_temp = cap_temp.numpy()
            
            temp = np.zeros((32,160,160,3))
            for k,l in enumerate(cap_temp):
                temp[k]=cv.resize(l,(160,160),interpolation = cv.INTER_AREA)
            
            cap[j] = temp
            cap_2[j] = temp[::8]
        
        for j,i in enumerate(label):
            cat[j][i]=1
        
        
        cap = cap/255.
        cap_2 = cap_2/255.
        
        yield ([cap , cap_2],cat)
        del sample

        
def data_loader_valid(df,batch=32,train_size=0.8):
    df = df.sample(frac=1).reset_index(drop=True)
    while True:
        length = int(len(df.index)*(1-train_size))
        sample = df[:length].sample(n=32)
        address = list(sample['FileAddress'])
        label = list(sample['label'])
        
        cap = np.zeros((batch,32,160,160,3),dtype='float32')
        cat = np.zeros((batch,8),dtype='float32')
        cap_2 = np.zeros((batch,4,160,160,3),dtype='float32')

        
        for j,i in enumerate(address):
            
            cap_temp = tv.io.read_video(i)[0]
            cap_temp = cap_temp.numpy()
            temp = np.zeros((32,160,160,3))
            for k,l in enumerate(cap_temp):
                temp[k]=cv.resize(l,(160,160),interpolation = cv2.INTER_AREA)
            
            cap[j]=temp
            cap_2[j] = temp[::8]
        
        for j,i in enumerate(label):
            cat[j][i]=1
        cap = cap/255.
        yield ([cap , cap_2],cat)
        del sample