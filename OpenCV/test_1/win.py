'''
1、窗口的展示
2、图像、视频的加载
3、基本图像的绘制
4、车辆识别

'''
# 新建窗口
# namedWindow() 
# imshow()
# destroyAllWindows()      
# resizeWindow()          调整窗口大小

import cv2
cv2.namedWindow('new',cv2.WINDOW_AUTOSIZE)     # 新建一个窗口
cv2.resizeWindow('new',640,480)                # 调整窗口的大小
cv2.imshow('new',0)                            # 展示窗口
                                                
key = cv2.waitKey(0)                           # 窗口的停留时间
if(key == 'q'):                                
    exit()
cv2.destroyAllWindows()                        # 消除所有的窗口

# 加载图片   imread()

