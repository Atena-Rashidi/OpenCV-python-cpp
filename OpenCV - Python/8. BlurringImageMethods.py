''' Image Blurring Technique:
1. Averaging Bluring
2. Gaussian Blurring
3. Median Blurring
4. Bilateral Filtering. 
As in one-dimensional signals, images also can be filtered with various low-pass filters 
(LPF), high-pass filters (HPF), etc. LPF helps in removing noise, blurring images.'''

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

# Convert an image to gray scale.
img = cv.imread(r"D:\GitHub\OpenCV\OpenCV - Python\Images\Nature.jpg")
cv.imshow('img', img)

''' ______________________________________________________________________ '''
# 1. Averaging Bluring
# https://machinelearningknowledge.ai/python-opencv-image-smoothing-using-averaging-gaussian-blur-and-median-filter/
# Averaging of the image is done by applying a convolution operation on the image with a normalized box filter. 
# In convolution operation, the filter or kernel is slides across an image and the average of all the pixels is 
# found under the kernel area and replace this average with the central element of the image.
# Note: The smoothing of an image depends upon the kernel size. If Kernel size is large then it removes the small
#  feature of the image. But if the kernel size is too small then it is not able to remove the noise
 
img_averag_blur = cv.blur(img, (3,3))
cv.imshow('img_averag_blur', img_averag_blur)

# 2. Gaussian Blurring
# In the gaussian blur technique, the image is convolved with a gaussian filter instead of a box or normalized filter. 
# In Gaussian filter only nearby pixels are considered while filtering
img_Gasusian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('img_Gasusian_blur', img_Gasusian_blur)

# 3. Median Blurring
''' The median filter technique is very similar to the averaging filtering technique shown above. 
The only difference is cv2.medianBlur() computes the median of all the pixels under the kernel 
window and the central pixel is replaced with this median value instead of the average value.
Note: This is highly effective in removing salt-and-pepper noise. '''
img_Median_blur = cv.medianBlur(img, 3)
cv.imshow('img_Median_blur', img_Median_blur)

# 4. Bilateral Filtering
# A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. 
# It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels.

img_bilateral_blur = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow('img_bilateral_blur', img_bilateral_blur)



cv.waitKey(0)