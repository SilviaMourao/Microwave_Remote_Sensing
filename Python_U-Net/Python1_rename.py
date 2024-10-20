# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:03:37 2022

@author: gonca
"""

import os

folder = 'D:\\Mestrado\\DRMicro\\ProjetoFinal\\ClipsFinal\\20221126\\'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + "2022tile" + str(count) + ".tif"

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')