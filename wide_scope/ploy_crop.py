import numpy as np
import cv2
from PIL import Image
import os
import time
import re


start_time = time.time()

# 列出原有图片存放的文件名
file = os.listdir(r"E:\PycharmProjects\wide_scope\new_images")
file_length = len(file)
# 29820
print(file_length)

# 原有图片存放的路径
root_path = "E:/PycharmProjects/wide_scope/"
dir = root_path + "new_images" + "/"
count = 0

"选取了叶栅通道周围20个点"
"需要注意这里numpy数组的数据类型需要是int型"
b = np.array([[0, 18.8], [543, 0], [705, 282], [800, 282],
                [800, 470], [724, 470], [724, 450],
               [671.69, 339.68], [645.28, 300.42], [603.77, 279.73],
              [539.62, 210.84], [483.01, 189.68], [426.41, 189.89], [0, 199.89]],
            dtype=np.int32)

if not os.path.exists(root_path + "6400_crop_test"):
    os.makedirs(root_path + "6400_crop_test")

blank_list = []
new_list = []

for root, dirs, files in os.walk(dir):
    print(root)
    # E:/PycharmProjects/wide_scope/new_images/
    print(dirs)
    # []
    print(files)
    # 此时files中的图片的顺序是不对的，需要修改
    # ['0.jpg', '1.jpg', '10.jpg', '100.jpg']  29820
    "修改files中的图片的顺序"
    "使得图片按照正常的顺序进行操作"
    for file in files:
        a = re.sub('[.jpg]', '', file)   # a是str
        blank_list.append(int(a))

    print(blank_list)


    blank_list.sort()

    print(blank_list)

    for i in blank_list:
        i = str(i) + '.jpg'
        new_list.append(i)

    print(new_list)
    # 此时列表中的图片顺序才是正确的
    # ['0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg',]
    index = 0

    for file in new_list:
        srcImg = cv2.imread(dir + str(file))
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

        cv2.imwrite(root_path + "6400_crop_test" + "/" + str(file), masked)

        index += 1

        print("index = ", index)


end_time = time.time()
print("end, during time is %.2f minutes" % ((end_time - start_time)/60.0))
