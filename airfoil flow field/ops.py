import tensorflow as tf
from utils import *


image_summary = tf.summary.image
scalar_summary = tf.summary.scalar
histogram_summary = tf.summary.histogram
merge_summary = tf.summary.merge
SummaryWriter = tf.summary.FileWriter


"批量归一化,即所谓的BN层"

class BatchNorm(object):
    def __init__(self, epsilon=1e-5, momentum=0.9, name="batch_norm"):
        with tf.variable_scope(name):
            self.epsilon = epsilon
            self.momentum = momentum
            self.name = name


    # 调用BN层实例的时候传入输入参数
    def __call__(self, x, train=True):
        # x代表输入，第一个维度为batch_size
        # scale: If True, multiply by `gamma`. If False, `gamma` is not used
        # epsilon: Small float added to variance to avoid dividing by zero
        # updates_collections: 一般都会将其设置为None，让均值和方差即时更新
        # is_training: 当它为True，代表是训练过程，这时会不断更新样本集的均值与方差。
        # 当测试时，要设置成False，这样就会使用训练样本集的均值和方差
        # 这里没有设置偏移beta
        print("调用BN层的实例 %s, 训练为%s" % (self.name, train))
        return tf.contrib.layers.batch_norm(x,
                                            decay=self.momentum,
                                            updates_collections=None,
                                            epsilon=self.epsilon,
                                            scale=True,
                                            is_training=train,
                                            scope=self.name)


def concat(tensors, axis, *args, **kwargs):
    # 这里的tensor是一个列表，包括x和y
    return tf.concat(tensors, axis, *args, **kwargs)


def conv_cond_concat(x, y):

    """Concatenate conditioning vector on feature map axis."""
    # 这里x 和 y都是张量
    # x和y前三个维度的值需要相同
    x_shapes = x.get_shape()
    y_shapes = y.get_shape()
    return concat([
        x, y * tf.ones([x_shapes[0], x_shapes[1], x_shapes[2], y_shapes[3]])], 3)


# 定义了卷积的操作
def conv2d(input_, output_dim,
           k_h=5, k_w=5, d_h=2, d_w=2, stddev=0.02,
           name="conv2d"):
    # 卷积核的大小为5， 滑动的步长为2
    # output_dim指的就是这一层卷积核的个数
    print("卷积操作")
    print("卷积的输入维度为", input_.get_shape().as_list())
    with tf.variable_scope(name):
        w = tf.get_variable(name='w', shape=[k_h, k_w, input_.get_shape()[-1], output_dim],
                            initializer=tf.truncated_normal_initializer(stddev=stddev))
        print("卷积的权重w-->", w.get_shape().as_list())
        conv = tf.nn.conv2d(input_, w, strides=[1, d_h, d_w, 1], padding='SAME')
        print("卷积只有的维度-->", conv.get_shape().as_list())

        biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
        conv = tf.reshape(tf.nn.bias_add(conv, biases), conv.get_shape())

        return conv


# 定义了转置卷积的操作
def deconv2d(input_, output_shape,
             k_h=5, k_w=5, d_h=2, d_w=2, stddev=0.02,
             name="deconv2d", with_w=False):
    print("转置卷积-->", name)
    with tf.variable_scope(name):
        # filter : [height, width, output_channels, in_channels]
        # 这里的output_shape是一个四维的
        # input_是个张量，output_shape是个列表
        print("output_shape-->", output_shape)
        w = tf.get_variable(name='w', shape=[k_h, k_w, output_shape[-1], input_.get_shape()[-1]],
                            initializer=tf.random_normal_initializer(stddev=stddev))
        print("权重w-->", w.get_shape().as_list())
        # 转置卷积还必须明确指定输出形状是多少
        deconv = tf.nn.conv2d_transpose(input_, w, output_shape=output_shape,
                                        strides=[1, d_h, d_w, 1])
        print("转置卷积之后-->", deconv.get_shape().as_list())
        biases = tf.get_variable('biases', [output_shape[-1]], initializer=tf.constant_initializer(0.0))
        deconv = tf.reshape(tf.nn.bias_add(deconv, biases), deconv.get_shape())

        if with_w:
            print("with_w=True, 返回转置卷积之后的结果",deconv.get_shape().as_list(),
                  "权重",w.get_shape().as_list(),"偏置",biases.get_shape().as_list())
            return deconv, w, biases
        else:
            print("with_w=False,返回转置卷积之后的结果",deconv.get_shape().as_list())
            return deconv


# 定义了leakyRELU
def lrelu(x, leak=0.2, name="lrelu"):
    return tf.maximum(x, leak * x)


# 定义了线性运算，返回x*w+b
def linear(input_, output_size, scope=None, stddev=0.02, bias_start=0.0, with_w=False):
    # input_是一个张量，这里将维度变成一个列表
    # 这里的output_size是个标量
    # 这个input_是个二维的噪声输入
    print("进入linear函数")
    shape = input_.get_shape().as_list()
    print("input_的维度是:", shape)
    print("output_size为:", output_size)

    with tf.variable_scope(scope or "Linear"):
        try:
            matrix = tf.get_variable(name="Matrix", shape=[shape[1], output_size], dtype=tf.float32,
                                     initializer=tf.random_normal_initializer(stddev=stddev))
            print("matrix的维度:", matrix.get_shape().as_list())
        except ValueError as err:
            msg = "NOTE: Usually, this is due to an issue with the image dimensions. " \
                  " Did you correctly set '--crop' or '--input_height' or '--output_height'?"
            err.args = err.args + (msg,)
            raise
        bias = tf.get_variable("bias", [output_size],
                               initializer=tf.constant_initializer(bias_start))
        if with_w:
            print("with_w为true,返回了矩阵相乘的结果，矩阵和偏置")
            return tf.matmul(input_, matrix) + bias, matrix, bias
        else:
            print("with_w为False,只返回了矩阵相乘的结果")
            return tf.matmul(input_, matrix) + bias
