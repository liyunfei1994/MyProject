import csv
import pandas as pd
import numpy as np
from scipy import interpolate
import time

strat_time = time.time()
n = np.arange(1, 11, 0.005)
a = pd.DataFrame(np.array(n))
for i in range(38):
    csvFile = open('E:/Pressure_data/pressure_data.csv', encoding='UTF-8-sig')
    reader = csv.reader(csvFile)
    x = np.arange(1, 11)
    column = [row[i] for row in reader]
    column = list(map(eval, column))
    y = np.array(column)
    tck = interpolate.splrep(x, y, w=np.ones_like(x), s=0, k=1)
    x_new = np.arange(1, 11, 0.005)
    y_new = interpolate.splev(x_new, tck, der=0)
    y_new = pd.DataFrame(y_new, columns=[i])

    a = pd.concat([a, y_new], axis=1, ignore_index=True)
    # a = pd.concat([a, y_new], axis=1)
    # print(y_new)
    # y_new.to_csv('E:/Pressure_data/1.csv', mode='a', index=False, header=False,)
    """知道问题出在哪里了"""
    """循环回来打印的时候,colomn打印出来是空的"""
    """需要我把reader也放在循环内部"""
    # print(column)
    # print(a)
a.to_csv('E:/Pressure_data/111.csv', mode='a', header=False, index=False)
end_time = time.time()
during_time = end_time - start_time
print("Total time is %.5f" % during_time)
"""7 minutes"""
