# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:05:30 2022

@author: Eow
"""

import os
import numpy as np
from skimage.io import imsave, imread
from skimage.filters import threshold_otsu
from skimage.morphology import erosion, dilation



# list_dir=[]

directory='D:\\Mestrado\\DRMicro\\ProjetoFinal\\ClipsTreino\\'

for filename in os.listdir(directory):
    print(os.path.join(directory,filename))
    image=os.path.join(directory,filename)
    image_path=image[:-4]
    Sat = imread(image)
    m=threshold_otsu(Sat)
    c1=Sat<=m
    ee=np.ones((5,5))
    Er = erosion(c1,ee)
    Dl = dilation(Er,ee)
    os.chdir('D:\\Mestrado\\DRMicro\\ProjetoFinal\\Mascaras\\')
    imsave(filename,Dl)