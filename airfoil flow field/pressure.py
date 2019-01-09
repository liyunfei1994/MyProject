from scipy.io import loadmat
import pandas as pd
import numpy as np

# 存储为一个字典
raw_data = loadmat("E:/new data/pwall_down.mat")
# 是一个ndarray数组类型的变量
# shape = (475052, 10)
pwall_down = raw_data['pwall_down']
# print(pwall_down.shape)

data = pd.DataFrame(pwall_down)
new_index = np.arange(147379, 247379, 10)
data = pd.DataFrame(data, index=new_index)
# shape(10000, 10)
# 每隔10个点测一组压力数据
# 分成训练集和测试集
# print(data)
data.to_csv("E:/PycharmProjects/airfoil flow field deconv/pressure_data.csv",
            index=False, header=False)
