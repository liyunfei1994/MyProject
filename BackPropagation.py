import numpy as np
import tensorflow as tf
from tensorflow.python.framework import ops

ops.reset_default_graph()
# Regression Example:
# 回归算法的例子
# We will create sample data as follows:
# x-data: 100 random samples from a normal ~ N(1, 0.1)
# target: 100 values of the value 10.
# We hwill fit te model:
# x-data * A = target
# Theoretically, A = 10.
# Create graph
sess = tf.Session()

# Regression Example:
# We will create sample data as follows:
# x-data: 100 random samples from a normal ~ N(1, 0.1)
# target: 100 values of the value 10.
# We hwill fit te model:
# x-data * A = target
# Theoretically, A = 10.

# Create data
"""随机生成一百个数"""
x_vals = np.random.normal(1, 0.1, 100)
y_vals = np.repeat(10., 100)
x_data = tf.placeholder(shape=[1], dtype=tf.float32)
y_target = tf.placeholder(shape=[1], dtype=tf.float32)

# Create variable (one model parameter = A)
A = tf.Variable(tf.random_normal(shape=[1]))

# Add operation to graph
my_output = tf.multiply(x_data, A)

# Add L2 loss operation to graph
loss = tf.square(my_output - y_target)

# Create Optimizer
my_opt = tf.train.GradientDescentOptimizer(0.02)
train_step = my_opt.minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()
sess.run(init)

# Run Loop
for i in range(5000):
    """从0-99中随机取一个值"""
    rand_index = np.random.choice(100)
    """从一百个数里面取一个数"""
    """rand_x需要加个方扩号，为的是使维度相同，否则会报错"""
    """Cannot feed value of shape () for Tensor 'Placeholder:0', which has shape '(1,)'"""
    rand_x = [x_vals[rand_index]]
    rand_y = [y_vals[rand_index]]
    """可以将一个列表喂给一个placeholder"""
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})
    if (i + 1) % 500 == 0:
        print('Step #' + str(i + 1) + ' A = ' + str(sess.run(A)))
        print('Loss = ' + str(sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})))
