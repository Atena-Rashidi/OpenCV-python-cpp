import cv2 as cv
import numpy as np 


path = r"D:\Extra Courses\OpenCV\Python\Atena.jpg"

# uint8 is an unsigned 8-bit integer that can represent values 0..255. 
# int on the other hand is usually a 32-bit signed integer. 
# When you create an array using dtype=int, each element in that aray takes 4 bytes. 
# OpenCV apparently expect array to be made of 8-bit tuples representing red, green and blue. 

# If the image is 8-bit unsigned, it is displayed as is.
# If the image is 16-bit unsigned or 32-bit integer, the pixels are divided by 256. That is, the value range [0,255*256] is mapped to [0,255].
# If the image is 32-bit floating-point, the pixel values are multiplied by 255. That is, the value range [0,1] is mapped to [0,255].
   
# creat a blanck image 
# shape is: (height, width, number of channel)
# shape for black and white: (500,500)
# shape for colored: (500, 500,3)
blanck = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('blanck', blanck)

img = cv.imread(path)
cv.imshow('Atena', img)
# img shape (1024, 769, 3)
print("img shape", img.shape)


# change the colot of blak image to green
blanck [:] = 0, 255, 0 
cv.imshow('blanckToGreen', blanck)


# coloring an specific part of an image
blanck[150:350, 150: 350] = 150, 70, 3
cv.imshow('GreenToCenterColore' , blanck)


# Draw a rectangle 
cv.rectangle(blanck, (50, 50), (450, 450), (150, 10, 150), thickness= 3)
cv.imshow('Rectangle', blanck)

# to color inside the rectangle we use thickness=cv.FILLED or thickness= -1
cv.rectangle(blanck, (50,50), (450, 450), (150, 10, 150), thickness = -1)
cv.imshow('FilledRec', blanck)

# Draw circle 
cv.circle(blanck, (blanck.shape[1]//2 , blanck.shape[0]//2), 140, (210, 200, 110), thickness= -1)
cv.imshow('circleInMiddle', blanck)

# Draw Line
cv.line(blanck, (0, 0), (blanck.shape[1]//2 , blanck.shape[0]//2), (20, 90, 225), thickness=3)
cv.imshow('Line', blanck)

# text
cv.putText(blanck, "This is a Frame", (blanck.shape[1]//4 , blanck.shape[0]//2), cv.FONT_HERSHEY_COMPLEX, 1, (200, 55, 250), 3)
cv.imshow('Text', blanck)


cv.waitKey(0)