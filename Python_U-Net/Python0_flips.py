# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 03:09:07 2022

@author: silam
"""

import cv2
import os
import numpy as np


directory='D:\\Mestrado\\DRMicro\\ProjetoFinal\\ClipsTreino\\'

for filename in os.listdir(directory):
    print(os.path.join(directory,filename))
    image=os.path.join(directory,filename)
    image_path=image[:-4]
    Sat_band=cv2.imread(image,cv2.IMREAD_ANYDEPTH)
    #Imagem original + 3 rotacoes  
    rot1=np.rot90(Sat_band,1)
    cv2.imwrite(image_path+'90.tif',rot1)
    rot2=np.rot90(Sat_band,2)
    cv2.imwrite(image_path+'180.tif',rot2)
    rot3=np.rot90(Sat_band,3)
    cv2.imwrite(image_path+'270.tif',rot3)
    
    #flip esq dir + 3 rotacoes 
    flippedimage1= np.fliplr(Sat_band)
    cv2.imwrite(image_path+'hor.tif',flippedimage1)
    rot1=np.rot90(flippedimage1,1)
    cv2.imwrite(image_path+'hor90.tif',rot1)
    rot2=np.rot90(flippedimage1,2)
    cv2.imwrite(image_path+'hor180.tif',rot2)
    rot3=np.rot90(flippedimage1,3)
    cv2.imwrite(image_path+'hor270.tif',rot3)
    
    # #flip up down + 3 rotacoes
    # flippedimage2= np.flipud(Sat_band)
    # cv2.imwrite(image_path+'vert.tif',flippedimage2)
    # rot1=np.rot90(flippedimage2,1)
    # cv2.imwrite(image_path+'vert90.tif',rot1)
    # rot2=np.rot90(flippedimage2,2)
    # cv2.imwrite(image_path+'vert180.tif',rot2)
    # rot3=np.rot90(flippedimage2,3)
    # cv2.imwrite(image_path+'vert270.tif',rot3)   
    
    # #flip updown leftright + 3 rotacoes
    # flippedimage3= np.flipud(Sat_band)
    # flippedimage3= np.fliplr(flippedimage3)
    # cv2.imwrite(image_path+'both.tif',flippedimage3)
    # rot1=np.rot90(flippedimage3,1)
    # cv2.imwrite(image_path+'both90.tif',rot1)
    # rot2=np.rot90(flippedimage3,2)
    # cv2.imwrite(image_path+'both180.tif',rot2)
    # rot3=np.rot90(flippedimage3,3)
    # cv2.imwrite(image_path+'both270.tif',rot3)
