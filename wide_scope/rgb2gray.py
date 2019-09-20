import tensorflow as tf
import matplotlib.pyplot as plt
import os
import re
import cv2
import time
from PIL import Image
import numpy as np


rgb_path = "E:/PycharmProjects/wide_scope/6400_crop"
gray_path = "E:/PycharmProjects/wide_scope/6400_crop_gray"

start = time.time()
# print(files)
blank_list = []
# new_file_list 用于存放改变顺序之后的图片的路径
new_file_list = []

file_names = next(os.walk(rgb_path))[2]
print("file_names",file_names)

for i in file_names:
    a = re.sub('[.jpg]', '', i)
    blank_list.append(int(a))

print("blank_list", blank_list)
blank_list.sort()
print("sort", blank_list)

for i in blank_list:
    i = str(i) + '.jpg'
    new_file_list.append(i)

print("new_list", new_file_list)

if not os.path.exists(gray_path):
    os.makedirs(gray_path)


for i in range(len(new_file_list)):
    img = Image.open((os.path.join(rgb_path, new_file_list[i]))).convert('L')
    img.save(os.path.join(gray_path, new_file_list[i]))
    print(np.array(img).shape)
    print("i=", i)

end = time.time()
print("during time is %.2f minutes" % ((end-start)/60))
