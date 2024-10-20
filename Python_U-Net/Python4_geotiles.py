# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 01:58:35 2022

@author: silam
"""
import PIL
import os
#from os import glob
import pathlib
import rasterio as rio
import numpy as np
from skimage.io import imsave, imread

#EscritaGeotiff

result_dir_test="D:/Mestrado/DRMicro/ProjetoFinal/ClipsFinal/2022Results/2022tile32.tif"
originals="D:/Mestrado/DRMicro/ProjetoFinal/ClipsFinal/20221126/2022tile32.tif"


src = originals
img = result_dir_test

src1 =  rio.open(src)

img1 =  imread(img)
#naip_data2 = np.moveaxis(img.squeeze(),-1,0)


with rio.open("D:/Mestrado/DRMicro/ProjetoFinal/ClipsFinal/2022Results/2022tile32g.tif",
                                                'w',
                                                driver='GTiff',
                                                height=256,
                                                width=256,
                                                count=1,
                                                dtype= rio.uint8,
                                                crs=src1.crs,
                                                transform=src1.transform,
                                                nodata=None) as dst:
                                dst.write(img1,1)
                                
                        