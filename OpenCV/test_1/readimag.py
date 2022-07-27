import cv2

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
img = cv2.imread(r'D://project_code/Python/OpenCV/test_1/5ecd70ef4320136388ae8fae3ecdaad4.jpg')

cv2.imshow('img',img)                            # 展示窗口
cv2.waitKey(0)
cv2.destroyAllWindows()

