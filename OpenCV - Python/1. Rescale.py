import cv2 as cv

path_img = r"D:\Extra Courses\OpenCV\Python\elephent.jpg"
path_vid = r"D:\Extra Courses\OpenCV\Python\side.mp4"
#####################################################
#functiond 
def rescleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)



######################################################

# read the image
img = cv.imread(path_img)
# show the image
cv.imshow('elephent', img)
img_resized = rescleFrame(img, 0.5)
cv.imshow('elephent_resized', img_resized)

#///////////////////////////////////////////////////////
# images/videos/live videos

# read the video
capture = cv.VideoCapture(path_vid)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescleFrame(frame, 0.2)
    
    # show the video
    cv.imshow('Side', frame)
    cv.imshow('SideResized', frame_resized)
    




     if cv.waitKey(0) & 0xFF == ord('d'):
        break 