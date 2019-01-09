% 有几个疑问，为什么要去除零漂，为什么要用前5000行的均值?
% 为什么选择475052？曲线的横坐标是什么？为什么要除以10000
% 本来是有593920行，取出来前475052行，目的是？

%从文件中加载数据用importdata()函数
% 注释的快捷键是ctrl+r，取消注释的快捷键是ctrl+t
% B.txt的第一列代表的是背压，第二列代表的是红外信号
A=importdata('E:\new data\4\B.txt');%隔离段上壁面压力测点数据
% 获得数组的维度信息用size()函数，用数组接收
% m = 593920, n = 2
[m,n]=size(A);
% test=1:5, test = 1 2 3 4 5
% 这里有个疑问，475052是什么意思，
xx=1:475052;
yy=xx./10000;
% 将A数组中的1-5000行所有列取出来
% mean()函数不指定维度，返回每一列的均值
% pwall_avg_up=[1.4617, 0.0003]
pwall_avg_up=mean(A(1:5000,:));
% repmat()函数的用法，B = repmat(A,m,n)，其功能是以A的内容堆叠在（MxN）的矩阵B中
% 这个公式就是说：求出A前5000行的均值，再repmat成m行的矩阵，再用A矩阵减去这个值
% 目的是A矩阵的所有行，都减去前5000行的平均值
% size(pwall_v_up)=[593920, 2]
pwall_v_up=A-repmat(pwall_avg_up,m,1);%去除零漂
% 取出pwall_v_up前475052行第一列，除以4再加0.1

% 以下几个公式的具体意义
% 这里转换成的压力为Mpa
pwall_up=pwall_v_up(1:475052,1)/4+0.1; %电信号转压力信号,测点1~11为高频传感器（0.1~1MPa对应1~5V）
% 转换为pa
pwall_up=pwall_up*1000000;
% 转换为压比，38682的值怎么得来，是什么意思？
pwall_up=pwall_up/38682.08;
% 这个图1也是关于背压的变化？
figure(1);
for i=1:1
  plot(yy',pwall_up(:,i));
  hold on;
end

B=importdata('E:\new data\4\A.txt');%隔离段上壁面压力测点数据
% size(B)=[593920, 12],a=593920,b=12
[a,b]=size(B);
xx=1:475052;
yy=xx./10000;
pwall_avg_down=mean(B(1:5000,:));
pwall_v_down=B-repmat(pwall_avg_down,a,1);%去除零漂
% A.txt的1-10列是压力电信号
pwall_down=pwall_v_down(1:475052,1:10)/4+0.1; %电信号转压力信号,测点1~11为高频传感器（0.1~1MPa对应1~5V）
pwall_down=pwall_down*1000000/38682.08;
% 第二个图展示的是10个压力测点的变化情况，纵坐标是压比，横坐标是时间，47.5s
figure(2);
for i=1:10
  plot(yy',pwall_down(:,i));
  hold on;
end

A=importdata('E:\new data\4\B.txt');%隔离段上壁面压力测点数据，指令
[a,b]=size(A);
xx=1:475052;
yy=xx./10000;
figure(3);
% B.txt的第二列，红外信号
% 图片3展示的是信号的变化情况
plot(yy',A(1:475052,2))   

% 总压
% 这个换算的关系是怎么得到的？没想清楚
pt_p=pwall_v_down(1:475052,11)/((4.4-0.88)/5)+0.1; %测点11为低频总压传感器（0.1~5MPa对应0.88~4.4V）,总压
% 图4是总压的变化
figure(4);
plot(yy',pt_p);

% 图5是背压的变化
figure(5);  %背压
plot(yy',pwall_up(1:475052,1));
fenxi(:,1)=yy';
fenxi(:,2)=pwall_up(1:475052,1);
