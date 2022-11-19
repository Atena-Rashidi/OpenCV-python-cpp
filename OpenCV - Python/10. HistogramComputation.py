''' https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
    Histogram is a graph or plot, which gives the intensity distribution of an image. 
    It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and 
    corresponding number of pixels in the image on Y-axis.
    It is another way of understanding the image by looking at the histogram of an image
    to understand contrast, brightness, intensity distribution '''

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np
# path  = r"D:\GitHub\OpenCV\OpenCV - Python\Images\Nature.jpg"
path = r"D:\GitHub\OpenCV\OpenCV - Python\Images\Cat.jpg"
img = cv.imread(path)
img = cv.resize(img, (400, 400))
cv.imshow('img', img)

''' ______________________________________________________________________ '''
# Convert an image to a gray scale and compute the gray scale histogram
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('img_gray', img_gray)

''' BINS : A histogram shows the number of pixels for every pixel value, ie from 0 to 255. 
    For example you need 256 values to show the histogram. 
    You need to find the number of pixels lying between the interval of 0 to 15, then 16 to 31, ..., 240 to 255. 
    You will need only 16 values to represent the histogram --> (256) / 16 = 16 
    So what you do is simply split the whole histogram to 16 sub-parts and value of each sub-part is the sum of all pixel count in it. 
    This each sub-part is called "BIN". 
    So, the number of bins is only 16. BINS is represented by the term histSize in OpenCV docs.
    '''
# cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# images : it is the source image of type uint8 or float32. it's a list and should be given in square brackets, ie, "[img]".
# channels : it is also a list of channel and given in square brackets. It is the index of channel for which we calculate histogram. 
# For example, if input is grayscale image, its value is [0]. For color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
# mask : mask image. To find histogram of full image, it is given as "None". But if you want to find histogram of particular region of image, you have to create a mask image 
# for that and give it as mask. 
# histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
# ranges : this is our RANGE. Normally, it is [0,256]

''' ______________________________________________________________________'''
'''  GRAYSCALE HISTOGRAM '''
hist_img_gray = cv.calcHist([img_gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Bins')
plt.plot(hist_img_gray)
plt.xlim([0, 256])
plt.show()

# Mask ___________________________________________________________________
# Creat a Mask and compute Histogram on this Mask
# Creat a blank file 
# Creat a circle as Mask on the blank file
# apply the circle as Mask on the grayscale img using bitwise_and
img_blank = np.zeros(img.shape[:2], dtype = 'uint8')
circle = cv.circle(img_blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
cv.imshow('Mask_circle', circle)

Mask = cv.bitwise_and(img_gray.copy(), img_gray, mask = circle)
cv.imshow('img_masked', Mask)

hist_img_gray_masked = cv.calcHist([img_gray], [0], Mask, [256], [0, 256])
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Bins')
plt.plot(hist_img_gray)
plt.xlim([0, 256])
plt.show()


''' ______________________________________________________________________'''
'''  COLORSCALE  HISTOGRAM '''

plt.figure()
plt.title('ColorScale Mask Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Bins')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist_img = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist_img, color = col)
    plt.xlim([0, 256])
    
plt.show()

# Mask ___________________________________________________________________

img_blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(img_blank, (img.shape[1]//2, img.shape[0]//2), 200, 255, -1)
cv.imshow('Mask_circle', mask)

''' Mask must be binary format, so we don't need the following bitwise_and code '''
# Masked = cv.bitwise_and(img, img, mask = mask)
# cv.imshow('img_masked', Masked)

plt.figure()
plt.title('ColorScale Mask Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Bins')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist_img = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist_img, color = col)
    plt.xlim([0, 256])
    
plt.show()

cv.waitKey(0)