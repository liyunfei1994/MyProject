import csv
import numpy as np
from scipy import interpolate
import pandas as pd

x = np.arange(1, 11)
csvFile = open('E:/pressure_data.csv', encoding='UTF-8')
reader = csv.reader(csvFile)
column = [row[1] for row in reader]
column = list(map(eval, column))
y = np.array(column)
tck = interpolate.splrep(x, y, s=0, k=1)
x_new = np.arange(1, 11, 0.005)
y_new = interpolate.splev(x_new, tck, der=0)
y_new = pd.DataFrame(y_new)
y_new.to_csv('E:/1.csv', mode='a', header=False)
