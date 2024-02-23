import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(10,1)

while cap.isOpened() == True:
    ret,frame = cap.read()
    if ret == True:
        px = frame[100,100]
        cv2.imshow('img',frame)
        print(px)
        key = cv2.waitKey(1)
        if key == 27:
            break
    else:
        break
        
cv2.destroyAllWindows()
cap.release()
    
