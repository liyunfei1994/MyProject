import csv
import pandas as pd
import numpy as np
from scipy import interpolate
import time


start_time = time.time()
n = np.arange(1, 11, 0.005)
a = pd.DataFrame(np.array(n))
for i in range(5528):
    csvFile = open('E:/Density_data/density_data.csv', encoding='UTF-8-sig',)
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

new_columns = a.columns.delete(0)
a = a.reindex(columns=new_columns)
a.to_csv('E:/Density_data/1.csv', mode='a', header=False, index=False)

end_time = time.time()
during_time = (end_time - start_time)/60
print("Total Time is %.3f" % during_time)
"""7.72分钟"""
