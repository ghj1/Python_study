import sys
import cv2
cap = cv2.VideoCapture(0) # 카메라 수 
while True:
    ret, frame = cap.read()
    inversed = ~frame # 반전 cv2.imshow('frame', frame)
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed )
    if cv2.waitKey(60) == 27:
        break
cap.release()

cv2.destroyAllWindows()