''' Bitwise Operationd: AND, OR, XOR, and NOT 
    W use them in Mask a lot.
    '''

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
path  = r"D:\GitHub\OpenCV\OpenCV - Python\Images\Nature.jpg"
img = cv.imread(path)

''' ______________________________________________________________________ '''
# 1. Make a blank file, and draw a rectangle in it and fill out the rectangle


img_blank = np.zeros((400, 400), dtype = 'uint8')
cv.imshow('img_blank', img_blank)

img_rectangle = cv.rectangle(img_blank.copy(), (30, 30), (370, 370), 255, -1)
img_circle = cv.circle(img_blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('img_rectangle', img_rectangle)
cv.imshow('img_circle', img_circle)


# Bitwise AND --> returns intersecting regions
bitwise_or_img = cv.bitwise_or(img_rectangle, img_circle)
cv.imshow('bitwise_or_img', bitwise_or_img)

# Bitwise OR --> put them together and returns intersecting and non-intersecting regions
bitwise_and_img = cv.bitwise_and(img_rectangle, img_circle)
cv.imshow('bitwise_and_img', bitwise_and_img)

# Bitwise XOR  --> returns non-intersecting regions
bitwise_xor_img = cv.bitwise_xor(img_rectangle, img_circle)
cv.imshow('bitwise_xor_img', bitwise_xor_img)

# Bitwise NOT --> inver binary colors
bitwise_not_img = cv.bitwise_not(img_circle)
cv.imshow('bitwise_not_img', bitwise_not_img)


# -----------------------------------------------------------------------------------------
''' Masking:
    Allows us to focus on a certain part of an image  like, focusing onlt on people's 
    faces in an image and remove unwanted parts of the image.  
    Masking is used in Image Processing to output the Region of Interest, or simply the 
    part of the image that we are interested in. We tend to use bitwise operations for 
    masking as it allows us to discard the parts of the image that we do not need '''
# The size of mask has to be the same of the image

# 1. make a blank image
# 2. Draw a circle in the copy of the img_blank_mask to creat a circle mask
# 3. Apply the circle mask on the image using bitwise_and 
 
img_blank_mask = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('img_blank_mask', img_blank_mask)

Mask_circle = cv.circle(img_blank_mask.copy(), (img.shape[1]//2, img.shape[0]//2), 300, 255, -1)
cv.imshow('Mask_circle', Mask_circle)

img_masked = cv.bitwise_and(img.copy(), img, mask = Mask_circle)
cv.imshow('img_masked', img_masked)

''' _____________________________________________________________________ '''

# 1. Draw a rectangle in the copy of the img_blank_mask to creat a rectangle mask
# 2. bitwise_and the circle mask and rectangle mask to creat a Img_crc_rec
# 3. Apply Img_crc_rec as a mask to the img.copy()

Mask_rect = cv.rectangle(img_blank_mask.copy(), (130, 130), (430, 430), 255, -1)
cv.imshow('Mask_rect', Mask_rect)

Img_crc_rec = cv.bitwise_and(Mask_rect, Mask_circle)
cv.imshow('img_masked_crc_rec', Img_crc_rec)

Img_masked_crc_rec = cv.bitwise_and(img.copy(), img, mask = Img_crc_rec)
cv.imshow('Img_masked_crc_rec', Img_masked_crc_rec)


cv.waitKey(0)