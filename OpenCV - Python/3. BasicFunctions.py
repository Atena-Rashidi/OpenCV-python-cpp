import cv2 as cv

path = r"D:\Extra Courses\OpenCV\Python\elephent.jpg"
img = cv.imread(path)
cv.imshow("Image", img)


# 1. Convert BGR image to gray scale image
#---------------------------------------------------------------------
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img_gray', img_gray)


# 2. Conver to Blur image
#---------------------------------------------------------------------
# it removes some of the noises that exist in an image
# lik some problems with bad lighting or camera sensors
# the first solution is usng Gaussian filter  
# in Gaussian filter nearby pixels are considered while filtering. 
# # It doesn't consider whether pixels have almost the same intensity. 
# It doesn't consider whether a pixel is an edge pixel or not. 
# So it blurs the edges also, which we don't want to do
img_blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('img_blur', img_blur)
# if we want to make the image more blurred, we should change the Kernel Size
moreBlur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('img_blur_more', moreBlur)

# 2. Edge Cascade
#---------------------------------------------------------------------
# to find the edges in an image, we can use canny filter
# we path an image and two threshold 
img_canny = cv.Canny(img, 125, 175)
cv.imshow('img_Canny', img_canny) 
# we can pass blur image to have less edges
canny_less_edge = cv.Canny(moreBlur, 125, 175)
cv.imshow("Less_Edge", canny_less_edge)


# 3. Erosion of images
#---------------------------------------------------------------------
# Erodes away the boundaries of the foreground object
# Used to diminish the features of an image.

#img_erosion = cv.erode(img, (5,5), iterations = 1)
img_erosion = cv.erode(img_canny, (5,5), iterations = 1)

cv.imshow('img_erosion', img_erosion)

# 4. Dilation of images
#---------------------------------------------------------------------
# Increases the object area
# Used to accentuate features
#img_dilation = cv.dilate(img, (5,5), iterations = 1)
img_dilation = cv.dilate(img_canny, (5,5), iterations = 1)

cv.imshow('img_dilation', img_dilation)

# 5. Resize
#---------------------------------------------------------------------
# Resizing an image means changing the dimensions of it
# Interpolation is the way the extra pixels in the new image is calculated. 
# If the original image is smaller, then a larger rescaled image has extra pixels 
# which is not exactly the same as a nearby pixels. 
# The value of the extra pixel depends on the technique used.
#print(img.shape)
# (683, 1024, 3) --> (height, width, channel)
img_resized = cv.resize(img, (500, 300), interpolation = cv.INTER_NEAREST)
cv.imshow("img_resized", img_resized)

# 5. Cropped
#---------------------------------------------------------------------
img_crroped = img[300:500, 400:700]
cv.imshow('img_crroped', img_crroped)
cv.waitKey(0) 
