import numpy as np
import cv2
from PIL import Image
import os
import time
import re


start_time = time.time()

file = os.listdir("E:/PycharmProjects/pictures/6400")
file_length = len(file)

root_path = "E:/PycharmProjects/pictures/"
dir = root_path + "6400" + "/"
count = 0

"选取了叶栅通道周围20个点"
"需要注意这里numpy数组的数据类型需要是int型"

b = np.array([[0, 56.84], [158.49, 56.84], [301.86, 56.94], [415.09, 72],
              [479.24, 87], [539.6, 113.68], [596.22, 151.57], [630.18, 189.47],
              [671.69, 242.52], [709.43, 291.78], [735.84, 341.05], [735.84, 454.73],
              [698.11, 378.94], [671.69, 329.68], [645.28, 280.42], [603.77, 238.73],
              [539.62, 200.84], [483.01, 185.68], [426.41, 181.89], [0, 181.89]],
             dtype=np.int32)

if not os.path.exists(root_path + "6400_crop"):
    os.makedirs(root_path + "6400_crop")

blank_list = []
new_list = []

for root, dirs, files in os.walk(dir):
    # print(root)
    # E: / PycharmProjects / pictures / 6400 /
    # print(dirs)
    # []
    # print(files)
    # ['0.jpg', '1.jpg', '10.jpg', '100.jpg']
    "修改files中的图片的顺序"
    "使得图片按照正常的顺序进行操作"
    for file in files:
        a = re.sub('[.jpg]', '', file)
        blank_list.append(int(a))


    blank_list.sort()

    for i in blank_list:
        i = str(i) + '.jpg'
        new_list.append(i)

    for file in new_list:
        srcImg = cv2.imread(root_path + "6400" + "/" + str(file))
        # print("srcImg-type",type(srcImg))  numpy
        # print("*" * 10)
        roi_t = []
        for i in range(len(b)):
            roi_t.append(b[i])

        roi_t = np.asarray(roi_t)

        "扩展维度"
        roi_t = np.expand_dims(roi_t, axis=0)
        # (1, 20, 2)
        im = np.zeros(srcImg.shape[:2], dtype="uint8")
        # print("im\n", im, "shape->", im.shape)
        # (504, 800)

        "绘制多边形"

        "参数的意思分别是：画布，点，是否闭合，线的颜色"
        cv2.polylines(img=im, pts=roi_t, isClosed=1, color=255)

        "填充多边形，画布，点，填充的颜色"
        cv2.fillPoly(img=im, pts=roi_t, color=255)
        mask = im

        "按位与操作"
        # 目标图片，源图片
        masked = cv2.bitwise_and(src1=srcImg, src2=srcImg, mask=mask)
        # type(masked)  numpy
        # shape(504, 800, 3)

        cv2.imwrite(root_path + "6400_crop" + "/" + str(file), masked)


end_time = time.time()
print("end, during time is %.2f minutes" % ((end_time - start_time)/60.0))

# end, during time is 2.46 minutes
