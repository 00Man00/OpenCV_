import numpy as np
import cv2

img = cv2.imread('test.jpg',0)
cv2.imshow('image',img)
key = cv2.waitKey(0)                        # waitKey 函数可以返回键值，通过返回的键值(ord()方法)进行下一步操作
if key==27:                                 # ESC键
    cv2.destroyAllWindows()
elif key == ord('s'):                       #按下ctril+s就对打开的图像进行保存了
    cv2.imwrite('test.jpg',img)
    cv2.destroyAllWindows()