''' https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, 
    it is set to 0/black, otherwise it is set to a maximum value (255/white). 
    -----------------------------------------------------------
    The function cv.threshold is used to apply the thresholding. 
    - The first argument is the source image, which should be a grayscale image. 
    - The second argument is the threshold value which is used to classify the pixel values. 
    - The third argument is the maximum value which is assigned to pixel values exceeding the threshold.
    * Different types of thresholding 
        - cv.THRESH_BINARY
        - cv.THRESH_BINARY_INV
        - cv.THRESH_TRUNC
        - cv.THRESH_TOZERO
        - cv.THRESH_TOZERO_INV 
    These methods return two outputs:
        1. The threshold that was used 
        2. The thresholded image 
  ----------------------------------
    In the previous section, we used one global value as a threshold. But this might not be good in all cases.
    If an image has different lighting conditions in different areas, an adaptive thresholding can help. 
    Here, the algorithm determines the threshold for a pixel based on a small region around it. 
    So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.
    The adaptiveMethod decides how the threshold value is calculated
    The method cv.adaptiveThreshold takes three input parameters:
        - The first argument is the source image
        - The blockSize determines the size of the neighbourhood area
        - C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.
    cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
    cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
    
    '''
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

path = r"D:\GitHub\OpenCV\OpenCV - Python\Images\Cat.jpg"
img = cv.imread(path)
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv.imshow('img', img)

''' ______________________________________________________________________ '''
# 1. Conver a BGR imag to a grayscale image
# 2. Apply cv.THRESH_BINARY
# 3. Save the image
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img_gray', img_gray)
threshold, threshold_Binary_img = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold_Binary_img', threshold_Binary_img)
cv.imwrite(r"D:\GitHub\OpenCV\OpenCV - Python\Images\threshold_Binary_img.jpg", threshold_Binary_img)

''' ______________________________________________________________________ '''
# Apply cv.THRESH_BINARY_INV
threshold, threshold_Binary_INV_img = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold_Binary_INV_img', threshold_Binary_INV_img)  
cv.imwrite(r"D:\GitHub\OpenCV\OpenCV - Python\Images\threshold_Binary_INV_img.jpg", threshold_Binary_INV_img)

''' ______________________________________________________________________ '''
# Apply cv.ADAPTIVE_THRESH_MEAN_C
# threshold_adaptive_mean_img = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
#             cv.THRESH_BINARY, 11, 3)
threshold_adaptive_mean_img = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
            cv.THRESH_BINARY_INV, 13, 5)
cv.imshow('threshold_adaptive_mean_img', threshold_adaptive_mean_img)  
cv.imwrite(r"D:\GitHub\OpenCV\OpenCV - Python\Images\threshold_adaptive_mean_img.jpg", threshold_adaptive_mean_img)

''' ______________________________________________________________________ '''
# Apply  cv.ADAPTIVE_THRESH_GAUSSIAN_C
# threshold_adaptive_gauss_img = cv.adaptiveThreshold(img_gray, 255,  cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
#             cv.THRESH_BINARY, 11, 3)
threshold_adaptive_gauss_img = cv.adaptiveThreshold(img_gray, 255,  cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv.THRESH_BINARY_INV, 13, 5)
cv.imshow('threshold_adaptive_gauss_img', threshold_adaptive_gauss_img)  
cv.imwrite(r"D:\GitHub\OpenCV\OpenCV - Python\Images\threshold_adaptive_gauss_img.jpg", threshold_adaptive_gauss_img)
cv.waitKey(0)