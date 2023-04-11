import pandas as pd
import os

def generate_df():
    
    classes = {"Abuse":0,"Arrest":1,'Arson':2,'Assault':3,'Burglary':4,'Explosion':5,'Fighting':6,'Normal':7}
    
    df=pd.DataFrame(columns=['Category','FileAddress','label'])
    root = '../input/dataset/Dataset'
    
    for i,j in enumerate(classes):
        path = os.path.join(root,j)
        for file in os.listdir(path):
            path_new = os.path.join(path,file)
            df.loc[len(df.index)] = [j,path_new,classes[j]]
    
    return df