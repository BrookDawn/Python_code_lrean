import cv2
import numpy as np

img = np.zeros((480,680,3),np.uint8)

cv2.line(img,(10,20),(400,20),(0,0,255))

cv2.imshow('draw',img)
cv2.waitKey(0)