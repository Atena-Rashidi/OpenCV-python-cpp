import cv2 as cv
import numpy as np 
path = r"D:\GitHub\OpenCV\OpenCV - Python\Images\elephent.jpg"
img = cv.imread(path)
cv.imshow('Image', img)

# Image Transformation:
# mage Transformations, rotation, resizing, flipping, and cropping

# 1. Translation: 
#------------------------------------
# shifting x and y axis
# Load an image from disk
# Define an affine transformation matrix
# Apply the cv2.warpAffine function to perform the translation

# so, we can shif an image up and down or left and right
# Defining a translation matrix 
# M = | 1 0 t{x} |
#     | 0 1 t{y} |
# for this matrix, we have to make a list with two list in it
# -t_{x} value shifts the image to the left
# t_{x} shifts the image to the right
# -t_{y} shifts the image up
# t_{y} shifts the image down  

def translate(img, x, y):
    TransMtrx = np.float32([[1,0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, TransMtrx, dimentions)

img_translated = translate(img, 100, -200)
cv.imshow('img_translated', img_translated)


# 2. Rotation:
#------------------------------------
# By Image Rotation, the image is rotated about 
# its center by a specified number of degrees
# rotation of an image is a geometric transformation
# We need a rotation matrix M from the cv2.getRotationMatrix2D function
# rotation matrix needs a rotation point and and angle
# then we apply the rotation to our image using the cv2.warpAffine

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMtrx = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)
    return cv.warpAffine(img, rotMtrx, dimentions)

img_rotated = rotate(img, 45, rotPoint= (400, 300))
cv.imshow('img_rotated', img_rotated)

# 3. Resize:
# --------------------------------------
img_resize = cv.resize(img, (300, 300), interpolation = cv.INTER_CUBIC)
cv.imshow('img_resize', img_resize)

# 3. Flipping:
# --------------------------------------
# cv2.cv.flip(src, flipCode[, dst] )
# flip code: A flag to specify how to flip the array; 
# 0 means flipping around the x-axis and positive value
# 1 means flipping around y-axis. Negative value 
# -1 means flipping around both axes.

img_flip = cv.flip(img, -1 )
cv.imshow('img_flip', img_flip)

# 3. Cropping:
# --------------------------------------
img_cropped = img[200:400, 400:1000]
cv.imshow('img_cropped', img_cropped)

cv.waitKey(0)

