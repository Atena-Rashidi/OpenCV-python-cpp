

''' 
https://learnopencv.com/edge-detection-using-opencv/
https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html
Edge detection is an image-processing technique, which is used to identify the boundaries 
(edges) of objects, or regions within an image. 
 Two important edge-detection algorithms in OpenCV: 
    - Laplacian Operator
    - Sobel Edge Detection
    - Canny Edge Detection

---------------------------------------------------------------------------------
- Laplacian Operator
    The Laplacian edge detector uses only one kernel. It calculates second order derivatives in a single pass.
    Parameters
    - src	      Source image.
    - dst	      Destination image of the same size and the same number of channels as src .
    - ddepth	  Desired depth of the destination image.
    - ksize	      Aperture size used to compute the second-derivative filters. See getDerivKernels for details. The size must be positive and odd.
    - scale	      Optional scale factor for the computed Laplacian values. By default, no scaling is applied. See getDerivKernels for details.
    - delta	      Optional delta value that is added to the results prior to storing them in dst .
    - borderType  Pixel extrapolation method, see BorderTypes
---------------------------------------------------------------------------------
- Sobel Edge Detection
    Sobel edge detector is a gradient based method based on the first order derivatives. 
    It calculates the first derivatives of the image separately for the X and Y axes.
    It is based on the fact that in the edge area, the pixel intensity shows a "jump" or a high variation of intensity. 
    Getting the first derivative of the intensity, we observe that an edge is characterized by a maximum.
    If the second derivative is zero, we can use this criterion to attempt to detect edges in an image. 
    However, note that zeros will not only appear in edges (they can actually appear in other meaningless locations);
    this can be solved by applying filtering where needed. 
---------------------------------------------------------------------------------
- Canny Edge Detection
    Reduce Noise using Gaussian Smoothing.
    Compute image gradient using Sobel filter.
    Apply Non-Max Suppression or NMS to just jeep the local maxima
    Finally, apply Hysteresis thresholding which that 2 threshold values T_upper and T_lower
    
    Syntax: cv2.Canny(image, T_lower, T_upper, aperture_size, L2Gradient)
    Where: 
        - Image: Input image to which Canny filter will be applied
        - T_lower: Lower threshold value in Hysteresis Thresholding
        - T_upper: Upper threshold value in Hysteresis Thresholding
        - aperture_size: Aperture size of the Sobel filter.
        - L2Gradient: Boolean parameter used for more precision in calculating Edge Gradient.
        
    '''
import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

path = r"D:\GitHub\OpenCV\OpenCV - Python\Images\Persepolis_Iran.jpg"
img = cv.imread(path)
# img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
cv.imshow('img', img)

''' ______________________________________________________________________ '''
# 1. Conver the img to grayscale
# 2. Apply (cv.Laplacian) to the image to detect the edge
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img_gray', img_gray)

img_Laplacian = cv.Laplacian(img_gray, cv.CV_64F)       # computes gradian of the image
img_Laplacian = np.uint8(np.absolute(img_Laplacian))    # images cannot take negetive values, to prevent it we use absolute then conver it to image specific datatype we use np.uint8
cv.imshow('img_Laplacian', img_Laplacian)

''' ______________________________________________________________________ '''
# 1. Apply (cv.Sobel) to the image to detect the edge accros X access
# 2. Apply (cv.Sobel) to the image to detect the edge accros Y access
# 3. Apply (cv.Sobel) to the image to detect the edge accros X and Y access
img_sobel_X = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
img_sobel_Y = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
img_sobel_X_Y = cv.bitwise_and(img_sobel_X, img_sobel_Y)

cv.imshow('img_sobel_X', img_sobel_X)
cv.imshow('img_sobel_Y', img_sobel_Y)
cv.imshow('img_sobel_X_Y', img_sobel_X_Y)

''' ______________________________________________________________________ '''
# 1. Apply Canny Edge detection
img_canny = cv.Canny(img_gray, 100, 200)
cv.imshow('img_canny', img_canny)




cv.waitKey(0)