import csv
import pandas as pd
import numpy as np
from scipy import interpolate
import time


start_time = time.time()
n = np.arange(1, 11, 0.005)
a = pd.DataFrame(np.array(n))
for i in range(38):
    csvFile = open('E:/Pressure_data/pressure_data.csv', encoding='UTF-8-sig',)
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

# 删去第10列和第20列
new_columns = a.columns.delete([0, 10, 20])
a = a.reindex(columns=new_columns)
a.to_csv('E:/Pressure_data/1.csv', mode='a', header=False, index=False)
