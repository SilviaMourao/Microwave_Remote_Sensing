# Microwave Remote Sensing - U-Net Shoreline Detection

**Institution**: Faculdade de Ciências da Universidade de Lisboa  
**Course**: Microwave Remote Sensing  
**Project Date**: 2022  
**Project Language**: English  

## Project Overview

This project focuses on the implementation of a U-Net convolutional neural network for shoreline detection using Sentinel-1 radar images. The aim was to classify land-sea boundaries for shoreline monitoring applications. The implementation involved preprocessing the radar images, training the U-Net model, and evaluating its performance.

## Key Challenges and Results

The U-Net model was successfully implemented but failed to reach the high accuracy and low loss values achieved in the original study due to a significantly smaller dataset and time constraints. The model's performance was lower than expected:
- **Training Accuracy**: 96.1% with a loss of 0.117  
- **Validation Accuracy**: 94.9% with a loss of 0.144  
- **F1 Score**: 54% within 5 pixels of the ground truth shoreline

These results indicate that the current implementation is limited in its application for precise shoreline monitoring.

## Files and Structure

- **Python_U-Net/**: Contains Python scripts implementing the U-Net model and associated tasks for data preprocessing, model training, and evaluation.
- `Python0_flips.py`: Script for augmenting the dataset through image flipping.
- `Python1_rename.py`: Script for renaming and organizing the input data files.
- `Python2_masks.py`: Script for generating binary masks from the input radar data.
- `Python3_UNet.ipynb`: Jupyter notebook implementing the U-Net architecture and training the model.
- `Python4_geotiles.py`: Script for georeferencing and tiling the image data.
- `Python5_confusionmatrices.py`: Script to calculate confusion matrices and evaluate the classification performance.
- `dataResUnet.xlsx`: Results and evaluation data from the U-Net training and validation.
- `model-ResUnet.h5`: Trained model data.
- **Project_U-Net_Classification.pdf**: Project report.

## Limitations and Future Work

- **Training Data**: The limited size of the training dataset hindered the model’s accuracy. A larger and more diverse dataset could potentially improve the results.
- **Labeling Process**: The Otsu's Threshold method used for generating training labels introduced inaccuracies, particularly in areas with imbalanced classes (e.g., small land areas compared to the sea).  
- **Shoreline Detection**: The generated shorelines were less accurate compared to ground truth, limiting the model's effectiveness for fine-scale monitoring of shoreline changes.

## Improvements

- Increasing the dataset size, both in terms of spatial and temporal coverage, would improve model performance.
- Exploring alternative labeling methods, such as hysteresis thresholding, may enhance the quality of the training labels.
- Implementing more advanced variations of U-Net, like the Deep U-Net, could also enhance segmentation accuracy.

## Conclusion

While the U-Net model produced satisfactory results for academic purposes, its current accuracy limits its application in real-world shoreline monitoring. Further enhancements in training data and segmentation techniques are needed to achieve higher precision and scalability.

---
