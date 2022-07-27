import cv2

#创建窗口
cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)
#获取视频设备
cap = cv2.VideoCapture(0)
while True:
    #从摄像头中读取视频帧
    ret,frame = cap.read()

    #将视频帧在窗口中显示
    cv2.imshow('video',frame)

    #按q退出
    key = cv2.waitKey(0)
    if(key & 0xff == ord("q")):
        break

#释放资源
cap.release()
cv2.destroyAllWindows()