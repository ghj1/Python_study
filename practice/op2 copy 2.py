import cv2 as cv
import numpy as np

cap = cv.VideoCapture('images/woman.mp4')
retval, frame=cap.read()
frame = cv.resize(frame, None, fx=0.3,fy=0.3, interpolation=cv.INTER_AREA)

while True:
    retval, frame=cap.read()
    if not retval:
        break

    frame=cv.resize(frame,None,fx=0.3,fy=0.3,interpolation=cv.INTER_AREA)
    #print(frame)
    # Load the aerial image and convert to HSV colourspace
    #image = cv.imread("./test.png")
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    # Define lower and uppper limits of what we call "brown"
    brown_lo=np.array([39,0,0])
    brown_hi=np.array([86,255,255])

    # Mask image to only select browns
    mask=cv.inRange(hsv,brown_lo,brown_hi)

    # Change image to red where we found brown
    frame[mask>0]=(255,217,236)

    cv.imshow("result.png",frame)
    key=cv.waitKey(25)
    if key==27:
        break

 
if cap.isOpened():
    cap.release()
    
cv.destroyAllWindows()