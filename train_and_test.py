import numpy as np
import pandas as pd
import time

start_time = time.time()
# 2000行 36列 DataFrame结构
pressure_data = pd.read_csv('E:/Pressure_data/1.csv', header=None)
# 2000行 5528列
density_data = pd.read_csv('E:/Density_data/1.csv', header=None)
# 2000行 5564列
data = pd.concat([pressure_data, density_data], axis=1)
# 1600行 5564列
train_data = data.sample(frac=0.8)
train_data_index = train_data.index
# print(train_data_index)
test_index = data.index.delete(train_data_index)
# print(test_index)

train_data.to_csv('E:/train.csv', mode='a', header=False, index=False)
test = data.reindex(index=test_index)
# print(test)
test.to_csv('E:/test.csv', mode='a', header=False, index=False)

end_time = time.time()
during_time = (end_time - start_time)/60
print("Total Time is %.2f" % during_time)
"""0.32分钟"""
