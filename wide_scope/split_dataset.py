import numpy as np
import pandas as pd
import os
import re


pressure_path = r"E:\PycharmProjects\wide_scope\pressure_data.csv"
train_pressure_path = r"E:\PycharmProjects\wide_scope\train_pressure.csv"
test_pressure_path = r"E:\PycharmProjects\wide_scope\test_pressure.csv"

pressure_data = pd.read_csv(pressure_path, header=None)
# 29820
print(pressure_data)
# 划分的比例
split_ratio = 0.7
np.random.seed(10)
shuffled_indices = np.random.permutation(len(pressure_data))
print("shuffled indices",shuffled_indices)

train_indices = shuffled_indices[:int(len(pressure_data) * split_ratio)]
print("train indices", train_indices.shape)
test_indices = shuffled_indices[int(len(pressure_data) * split_ratio):]
print("test indices", test_indices.shape)

new_train_indices = np.sort(train_indices)
print("train_indices_sort", new_train_indices[:10])

new_test_indices = np.sort(test_indices)
print("test_indices_sort", new_test_indices[:10])

# pressure_data.drop(index=train_indices, inplace=True)
# print(pressure_data)
# pressure_data.to_csv(test_pressure_path, columns=None, header=None, index=None)
# pressure_data.drop(test_indices, inplace=True)
# print(pressure_data)
# pressure_data.to_csv(train_pressure_path, columns=None, header=None, index=None)

# ======================
# 至此，将压力数据的训练集和测试集划分完毕

images_path = r"E:\PycharmProjects\wide_scope\6400_crop_gray"
train_images_path = "E:/PycharmProjects/wide_scope/train_images"
test_images_path = "E:/PycharmProjects/wide_scope/test_images"

if not os.path.exists(train_images_path):
    os.makedirs(train_images_path)

if not os.path.exists(test_images_path):
    os.makedirs(test_images_path)


"将照片放在训练集的文件夹中"
for root, dirs, files in os.walk(images_path):
    # print("files.length",files.__len__())
    # 29820
    index = 0
    for name in files:
        # print()
        "此时name就是乱序排列的"
        if int(re.sub('[.jpg]', '', name)) in train_indices:
            os.rename(os.path.join(images_path, name), os.path.join(train_images_path, name))
            index += 1
            print("index = ", index)

"将照片放在测试集的文件夹中"
for root, dirs, files in os.walk(images_path):

    index = 0
    for name in files:
        # print(name)
        "此时name就是乱序排列的"
        if int(re.sub('[.jpg]', '', name)) in test_indices:
            os.rename(os.path.join(images_path, name), os.path.join(test_images_path, name))
            index += 1
            print("index = ", index)

"结束之后， 原有的文件夹中的所有的图片都被放进了训练集的文件夹和测试集的文件夹"
