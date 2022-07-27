import cv2

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',680,480)
#获取视频设备
cap = cv2.VideoCapture(r'D://project_code/Python/OpenCV/test_1/dianlu.mp4')
while True:
    #从摄像头中读取视频帧
    ret , frame = cap.read()

    #将视频帧在窗口中显示
    cv2.imshow('video',frame)

    #按q退出
    key = cv2.waitKey(40)
    if(key & 0xff == ord("q")):
        break

#释放资源
cap.release()
cv2.destroyAllWindows()