import pandas as pd


pressure_data = "E:/PycharmProjects/airfoil flow field deconv CNN/pressure_data.csv"
new_path = "E:/PycharmProjects/airfoil flow field deconv CNN/pressure_data_half.csv"
csv_file = pd.read_csv(pressure_data, header=None)
# <class 'pandas.core.frame.DataFrame'>
print(type(csv_file))

# new_csv_file = pd.DataFrame(csv_file, index=[])
print(csv_file.index)
index = [i for i in range(34994) if i%2 != 0]
csv_file.drop(index, inplace=True)

print(type(csv_file))
csv_file.to_csv(new_path, columns=None, header=None, index=None)
