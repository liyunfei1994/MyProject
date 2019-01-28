import numpy as np
import cv2
from PIL import Image


image = cv2.imread("E:/PycharmProjects/pictures/6400/1.jpg")

"选取了叶栅通道周围20个点"
"需要注意这里numpy数组的数据类型需要是int型"
b  = np.array([[0, 56.84], [158.49, 56.84],  [301.86, 56.94], [415.09, 72],
               [479.24, 87], [539.6, 113.68],[596.22, 151.57], [630.18, 189.47],
               [671.69, 242.52], [709.43, 291.78], [735.84, 341.05], [735.84, 454.73],
               [698.11, 378.94],[671.69, 329.68],[645.28, 280.42],[603.77, 238.73],
               [539.62, 200.84],[483.01, 185.68],[426.41, 181.89],[0, 181.89]],
              dtype = np.int32)

roi_t = []
for i in range(len(b)):
    roi_t.append(b[i])

roi_t = np.asarray(roi_t)

"扩展维度"
roi_t = np.expand_dims(roi_t, axis=0)
# (1, 20, 2)
im = np.zeros(image.shape[:2], dtype = "uint8")
# print("im\n", im, "shape->", im.shape)
# (504, 800)


"绘制多边形"

"参数的意思分别是：画布，点，是否闭合，线的颜色"
cv2.polylines(img=im, pts=roi_t, isClosed=1, color=255)

"填充多边形，画布，点，填充的颜色"
cv2.fillPoly(img=im, pts=roi_t, color=255)
mask = im
# 显示绘制多边形只有的画布
cv2.imshow("Mask", mask)
cv2.waitKey()


"按位与操作"
# 目标图片，源图片
masked = cv2.bitwise_and(src1=image, src2=image, mask=mask)
# type(masked)  numpy
# shape(504, 800, 3)
cv2.imwrite("image.jpg", masked)
