import cv2 as cv
import numpy as np 
path = r"D:\GitHub\OpenCV\OpenCV - Python\Images\elephent.jpg"

# Contours Detection:
# -------------------------------------------------------------
# Contours can be explained simply as a curve joining all 
# the continuous points (along the boundary), having same color or intensity. 
# The contours are a useful tool for shape analysis and 
# object detection and recognition. 
# For better accuracy, use binary images.

# how to find contours 
#------------------------
# 1. Read the Image and convert it to Grayscale Format
# 2. Apply Binary Thresholding
# 3. Use the findContours() function to detect the contours in the image
# 4. Draw Contours on the Original RGB Image or a Blank Image

# two functions:
#------------------------
# 1. findContours()
#   - cv.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
#   - returns: 1. contours: detected contours
#              2. hierarchy: containing information about the image topology
# 2 drawContours()
#   - cv.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]])


# ----------------------------------------------------------------------------
# 1. Read the Image and convert it to Grayscale Format
img = cv.imread(path)
cv.imshow('Image', img)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('img_gray', img_gray) 


img_canny = cv.Canny(img_gray, 125, 175)
cv.imshow('img_canny', img_canny)

img_blur = cv.GaussianBlur(img_gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('img_blur', img_blur)

# 2. Apply Binary Thresholding
# instead of canny and blur we can use binary thresholding
# if pixcle < 125, then set it to black/0 and if more than 125, then set it to white/255
ret, img_thresh = cv.threshold(img_gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('img_thresh', img_thresh)




# 3. Use the findContours() function to detect the contours in the image
contours, hierarchies = cv.findContours(img_thresh, cv.RETR_LIST, 
                                                    cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')


# 4. Draw Contours on the Original RGB Image or a Blank Image
img_blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('img_blank', img_blank)

cv.drawContours(img_blank, contours, -1, (100, 20, 200), 1)
cv.imshow('Draw_Contours', img_blank)



cv.waitKey(0)
cv.destroyAllWindows()

