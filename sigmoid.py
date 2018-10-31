import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 解决中文显示的问题
mpl.rcParams['axes.unicode_minus'] = False


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


fig = plt.figure(num="ooo",figsize=(6, 4))
ax = fig.add_subplot(111)

x = np.linspace(-10, 10)
y = sigmoid(x)
tanh = 2 * sigmoid(2 * x) - 1
# 设定x轴和y轴的取值范围
plt.xlim(-11, 11)
plt.ylim(-1.1, 1.1)
# 如果我们要移动坐标到中心点，那么我们可以移动其中的两条边
# 并隐藏两条边即可
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 指定x轴以及y轴的绑定
# 将x，y轴绑定到特定位置
# 这种情况是坐标轴的交点是(0, 0)
# 这个试一试就知道了， 就是指定坐标轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 设置坐标轴显示刻度的位置
ax.set_xticks([-10, -5, 0, 5, 10])
ax.set_yticks([-1, -0.5, 0.5, 1])

plt.plot(x, y, label="Sigmoid", color="blue")
plt.plot(2 * x, tanh, label="Tanh", color="red")
plt.legend()
plt.savefig('sigmoid.jpg')
plt.show()
