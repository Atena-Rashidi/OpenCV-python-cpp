''' Color Spaces:
    Color spaces are a way to represent the color channels present in the image that gives 
    the image that particular hue. There are several different color spaces and each has 
    its own significance. Some of the popular color spaces are RGB (Red, Green, Blue), 
    CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value), etc'''

import cv2 as cv
import matplotlib.pyplot as plt 

# Convert an image to gray scale.
img = cv.imread(r"D:\GitHub\OpenCV\OpenCV - Python\Images\elephent.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img_gray', img_gray)

''' ______________________________________________________________________ '''
# BGR to HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('img_hsv', img_hsv)

''' ______________________________________________________________________ '''
# BGR to L+a+b
img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('img_lab', img_lab) 

# OpenCV reads and shows images in BGR format
# but, other libraries read and show based on RGB format
# like matplotlib.pyplot, we can see inversion of color 
# by running the following code, we see a RBG picture in Figure 1
''' plt.imshow(img)
plt.show() '''

''' ______________________________________________________________________ '''
# BGR to RGB
img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('img_RGB', img_RGB)

''' ______________________________________________________________________ '''
# we can inverse all we did up in here!
# like, Gray to BGR, HSV to BGR, LAB to BGR, RGB to BGR
# We cannot directly conver Gray to HSV, for this forst we should convert
# Gray to BGR and then to HSV

''' ______________________________________________________________________ '''
# HSV to BGR
img_hsv2bgr = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR) 
cv.imshow('img_hsv2bgr', img_hsv2bgr)

''' ______________________________________________________________________ '''
# LAB to BGR
img_lab2bgr = cv.cvtColor(img_lab, cv.COLOR_LAB2BGR) 
cv.imshow('img_lab2bgr', img_lab2bgr)

cv.waitKey(0)