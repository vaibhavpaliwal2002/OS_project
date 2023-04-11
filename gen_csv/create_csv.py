import os
import torchvision
import torch
import pandas as pd


def to_frames(path, new_dest, cl, file, dr):
    cap = torchvision.io.read_video(path)
    cap = cap[0]
    df = pd.DataFrame(columns=['Filename','Label','Class'])
    index = dr.index(cl)
    for j,i in enumerate(cap):
        i=torch.permute(i,(2, 0, 1))
        filename = os.path.join(new_dest,"{0:4d}.png".format(j))
        torchvision.io.write_png(i, filename)
        df.loc[j] = [filename,index,cl]
        
    file_path = os.path.join('/kaggle/working/info',file[:-4])
    os.makedirs('/kaggle/working/info',exist_ok=True)
    df.to_csv(f'{file_path}.csv')
    
    return 
    

def create_csv():    
    root = '../input/dataset/Dataset'
    new_dest = '/kaggle/working/data'
    os.makedirs(new_dest,exist_ok=True)
    
    dr =[]
    
    for root_,direc,file in os.walk(root):
        if len(direc)!=0:
            dr.extend(direc)
    
    for i in dr:
        path = os.path.join(root,i)
        dest = os.path.join(new_dest,i)
        os.makedirs(dest,exist_ok=True)
        
        
        for root_,direc,file in os.walk(path):
            for j in file:
    
                temp_path = os.path.join(path,j)
                temp_dest_path = os.path.join(dest,j[:-4])
                os.makedirs(temp_dest_path,exist_ok=True)
                
                to_frames(temp_path, temp_dest_path, i, j, dr)
                
    return 
                