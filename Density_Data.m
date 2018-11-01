%这段代码的作用是将原始的CSV数据文件的最后一行拿出来
%从中随机取出来十分之一的数据存成了CSV文件
filename = 'density.csv';
data = csvread(filename, 0, 3);
data = data';
index = randperm(length(data), 5528); %length(data) = 55280
final_data = data(index);
csvwrite('density_out.csv', final_data);
