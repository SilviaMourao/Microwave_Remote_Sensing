# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:47:21 2022

@author: silam
"""

from skimage.io import imread
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
import numpy as np
import matplotlib.pyplot as plt

flat_lista = []
flat_listb = []

b=imread('D:\\Mestrado\\DRMicro\\ProjetoFinal\\2018predict.tif')
a=imread('D:\\Mestrado\\DRMicro\\ProjetoFinal\\GT10px.tif')

for sublist in a:
    for item in sublist:
        flat_lista.append(item)

for sublist in b:
    for item in sublist:
        flat_listb.append(item)

#confusion_matrix(a,b)
cm=confusion_matrix(flat_lista,flat_listb)
tn, fp, fn, tp = confusion_matrix(flat_lista,flat_listb).ravel()
print(classification_report(flat_lista,flat_listb))
print(cm)
#disp=ConfusionMatrixDisplay(confusion_matrix=cm)
#disp.plot()
#plt.show()