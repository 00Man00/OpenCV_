import cv2
import numpy as np

img = cv2.imread('picture_5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

counter, hierarchy = cv2.findContours(
    binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rect_m = cv2.minAreaRect(counter[0])
point = cv2.boxPoints(rect_m)
point = np.int32(point)
cv2.drawContours(img, [point], 0, (255, 255, 255), 1)

rect = cv2.boundingRect(counter[0])


while True:
    cv2.rectangle(img, rect, (255, 0, 0), 1)
    cv2.imshow('res', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
