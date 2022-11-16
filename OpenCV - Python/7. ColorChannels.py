''' Color Channels:
There are three channels in an RGB image- red, green and blue. The color space where
red, green and blue channels represent images is called RGB color space. In OpenCV, 
BGR sequence is used instead of RGB. This means the first channel is blue, the second
channel is green, and the third channel is red. '''

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

# Convert an image to gray scale.
img = cv.imread(r"D:\GitHub\OpenCV\OpenCV - Python\Images\logo.png")
cv.imshow('img', img)

''' ______________________________________________________________________ '''
# Splitting Channels with OpenCV
b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
print(img.shape)    # (249, 202, 3) colored image --> 3 channel
print(b.shape)      # (249, 202)    gray image --> 2 channel
print(g.shape)
print(r.shape)

''' ______________________________________________________________________ '''
# Merging Channels with OpenCV
# cv2.merge takes single channel images and combines them to make a multi-channel image.
img_merged = cv.merge([b, g, r])
cv.imshow('img_merged', img_merged)

''' ______________________________________________________________________ '''
# If we want to show the split channel separately, we should make a black image 
# and merge it with each split channel.
# We should creat a blank file with a list of zeros from np.zeros and with the 
# same shape of the original image. We don't need the channel, so we only use 
# height and with of it .shape[:2]
# blank_image = np.zeros(height, width, dtype=np.uint8)
img_blank = np.zeros(img.shape[:2], dtype=np.uint8) 

blue_mrg_blank = cv.merge([b, img_blank, img_blank])
green_mrg_blank = cv.merge([img_blank, g, img_blank])
red_mrg_blank = cv.merge([img_blank, img_blank, r])

cv.imshow('blue_mrg_blank', blue_mrg_blank)
cv.imshow('green_mrg_blank', green_mrg_blank)
cv.imshow('red_mrg_blank', red_mrg_blank)


cv.waitKey(0)
