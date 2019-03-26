import numpy as np
import pandas as pd
import os
import re

pressure_data_path = "E:/PycharmProjects/CNN/pressure_data_13990.csv"
train_pressure_path = "E:/PycharmProjects/CNN/train_pressure.csv"
test_pressure_path = "E:/PycharmProjects/CNN/test_pressure.csv"
split_ratio = 0.8
pressure_data = pd.read_csv(pressure_data_path, header=None)
print(pressure_data)
print(pressure_data.__len__())
np.random.seed(10)
shuffled_indices = np.random.permutation(len(pressure_data))
# numpy.ndarray
# print("shuffled_indices", type(shuffled_indices))
# [ 7477  3059  2132 ... 10872 12333  1154]
# print(shuffled_indices)
train_indices = shuffled_indices[:int(len(pressure_data) * split_ratio)]
test_indices = shuffled_indices[int(len(pressure_data) * split_ratio):]
# 11192
# print("train_indices", train_indices[:10])
new_train_indices = np.sort(train_indices)
print("train_indices_sort", new_train_indices[:30])
print("len(train_indices)",len(train_indices))
# 2798
print("test_indices", test_indices)
print("test_indices_length", len(test_indices))
new_test_indices = np.sort(test_indices)
print("test_indices_sort", new_test_indices)
# print(len(test_indices))
# print(shuffled_indices)
print("=" * 20)
pressure_data.drop(train_indices, inplace=True)
print(pressure_data)
# pressure_data.to_csv(test_pressure_path, columns=None, header=None, index=None)
# 训练集删去测试集的索引
# pressure_data.drop(test_indices, inplace=True)
# print(pressure_data)
# pressure_data.to_csv(train_pressure_path, columns=None, header=None, index=None)

"接下来处理训练集的图像"
#
# images_path = "E:/PycharmProjects/pictures/6400_crop"
# train_images_path = "E:/PycharmProjects/pictures/train_images"
# test_images_path = "E:/PycharmProjects/pictures/test_images"
# new_images_path = "E:/PycharmProjects/pictures/6400_crop_sort"
#
#
# # for root, dirs, files in os.walk(images_path):
# #     for i, name in enumerate(files):
# #         # print(i, name)
# #         os.rename(os.path.join(images_path, name), os.path.join(new_images_path, str(i)+'.jpg'))
# print("*" * 20)
# for root, dirs, files in os.walk(new_images_path):
#     for name in files:
#         # print(name)
#         "此时name就是乱序排列的"
#         if int(re.sub('[.jpg]', '', name)) in test_indices:
#             os.rename(os.path.join(new_images_path, name), os.path.join(test_images_path, name))
#             # pass
