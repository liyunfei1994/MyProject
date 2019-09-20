import numpy as np
import os
from scipy.io import loadmat
import pandas as pd
import time


start_time = time.time()
pressure_mat_path = "E:/PycharmProjects/wide_scope/sensor_pressure.mat"
raw_data = loadmat(pressure_mat_path)
# loadmat() 之后得到的是一个dict
# dict_keys(['__header__', '__version__', '__globals__', 'sensor_pressure'])
print(raw_data.keys())

sensor_pressure = raw_data['sensor_pressure']
# 取出来之后是个ndarray
# 497320, 10
print(sensor_pressure.shape)

pressure_data = pd.DataFrame(sensor_pressure)
print(pressure_data)
new_index = np.arange(126100, 424300, 10)
# 29820
print(new_index.__len__())
pressure_data = pd.DataFrame(pressure_data, index=new_index)
# [29820 rows x 10 columns]
print(pressure_data)

if not os.path.exists("E:/PycharmProjects/wide_scope/pressure_data.csv"):
    pressure_data.to_csv("E:/PycharmProjects/wide_scope/pressure_data.csv",
            index=False, header=False)
else:
    os.remove("E:/PycharmProjects/wide_scope/pressure_data.csv")
    pressure_data.to_csv("E:/PycharmProjects/wide_scope/pressure_data.csv",
                index=False, header=False)

end_time = time.time()
print("End! During time is %.2f minutes" % ((end_time - start_time)/60))
