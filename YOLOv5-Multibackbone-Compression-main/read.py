import cv2
dirpath = r'C:\Users\19821\Desktop\裁剪数据\新建文件夹\新建文件夹\花花\1.jpg'
img_cv   = cv2.imread(dirpath)#读取数据
print("img_cv:",img_cv.shape)


#看下读取的数据怎么样
