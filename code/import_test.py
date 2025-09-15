from sklearn.utils import shuffle
import os
from tqdm import tqdm
import numpy as np
import tensorflow as tf
import gc

datalabel="CRC"

def data_label():
    return datalabel

def MCNN_data_load(feature,kind):
    
    path_train_pos = "../dataset/"+feature+"/"+kind+"/Neo/train.npy"
    path_train_neg = "../dataset/"+feature+"/"+kind+"/Oth/train.npy"

    path_test_pos = "../dataset/"+feature+"/"+kind+"/Neo/test.npy"
    path_test_neg = "../dataset/"+feature+"/"+kind+"/Oth/test.npy"
    
    
    x_train,y_train=data_load(path_train_pos,path_train_neg)
    x_test,y_test=data_load(path_test_pos,path_test_neg)
    
    return(x_train,y_train,x_test,y_test)

def data_load(folder1,folder2):
    f1=np.load(folder1)
    f2=np.load(folder2)
    
    label1 = np.ones(f1.shape[0])
    label2 = np.zeros(f2.shape[0])
   
    
    print(label1.shape)
    print(label2.shape)
    
    #print(label1)
    #print(label2)
  
    
    x=np.concatenate([f1,f2], axis=0)
    y=np.concatenate([label1,label2], axis=0)
    y= tf.keras.utils.to_categorical(y,2)
    #y.dtype='float16'
    gc.collect()
    return x ,y