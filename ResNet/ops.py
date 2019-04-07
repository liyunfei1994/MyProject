import tensorflow as tf
import numpy as np
import tensorflow.contrib.slim as slim
import math


def show_all_variables():
    # tf.trainable_variables()返回的是一个列表
    print("show all variables")
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)

def variable_summaries(var, name):

    # 将生成监控信息的操作放在同一个命名空间下
    with tf.name_scope("summaries"):
        # 通过tf.summary.histogram记录张量中元素的取值分布
        tf.summary.histogram(name, var)
        # 计算变量的平均值
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean/' + name, mean)
        # 计算变量的标准差
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        tf.summary.scalar('stddev/' + name, stddev)

class BatchNorm(object):
    def __init__(self, epsilon=1e-5, momentum=0.9, name="batch_norm"):
        with tf.variable_scope(name):
            self.epsilon = epsilon
            self.momentum = momentum
            self.name = name


    def __call__(self, x, train=True):
        return tf.contrib.layers.batch_norm(x,
                                            decay=self.momentum,
                                            updates_collections=None,
                                            epsilon=self.epsilon,
                                            scale=True,
                                            is_training=train,
                                            scope=self.name)

BN = BatchNorm()

def bn_relu_conv_layer(input_layer, filter_shape, stride):

    bn_layer = BN(input_layer)
    relu_layer = tf.nn.relu(bn_layer)

    filter = tf.get_variable("filter", shape=filter_shape,
                             initializer=tf.truncated_normal_initializer(stddev=0.02))
    conv_layer = tf.nn.conv2d(relu_layer, filter, strides=[1, stride, stride, 1], padding='SAME')
    return conv_layer

def conv_bn_relu_layer(input_layer, filter_shape, stride):

    filter = tf.get_variable("weights", shape=filter_shape,
                             initializer=tf.truncated_normal_initializer(stddev=0.02))
    conv_layer = tf.nn.conv2d(input_layer, filter, strides=[1, stride, stride, 1], padding='SAME')
    bn_layer = BN(conv_layer)
    output = tf.nn.relu(bn_layer)
    return output

def residual_block(input_layer, output_channel, first_block=False):

    input_channel = input_layer.get_shape().as_list()[-1]
    print("input_channel", input_channel)
    print("output_channel", output_channel)
    # 当输入图片的维度比输出图片的维度小时，2-->4-->8-->16
    # 步长就改为2，这样输出的图片尺寸就会减小，维度增大，尺寸减小,维度不变，尺寸不变
    if input_channel * 2 == output_channel:
        increase_dim = True
        stride = 2
        print("stride = ", stride)
    elif input_channel == output_channel:
        increase_dim = False
        stride = 1
        print("stride = ", stride)
    else:
        raise ValueError('Output and input channel does not match in residual blocks!!!')

    # The first conv layer of the first residual block does not need to be normalized and relu-ed.
    # 第一个残差单元的第一个卷积层不需要归一化以及激活函数
    with tf.variable_scope('conv1_in_block'):
        if first_block:
            # filter = create_variables(name='conv', shape=[3, 3, input_channel, output_channel])
            filter = tf.get_variable("filter", shape=[3,3,input_channel, output_channel],
                                     initializer=tf.truncated_normal_initializer(stddev=0.02))
            "第一个block的第一个卷积层，步长为1,图像尺寸大小不变"
            conv1 = tf.nn.conv2d(input_layer, filter=filter, strides=[1, 1, 1, 1], padding='SAME')
            print("First Block")
            print("conv1 In Block", conv1.get_shape().as_list())
        else:
            "如果不是第一个block，卷积层的步长由维度的变化决定"
            print("Not First Block")
            conv1 = bn_relu_conv_layer(input_layer, filter_shape=[3, 3, input_channel, output_channel], stride=stride)
            print("conv1 In Block", conv1.get_shape().as_list())

    with tf.variable_scope('conv2_in_block'):
        "第二个卷积层的步长为1"
        "第二个卷积层不改变维度数目"
        conv2 = bn_relu_conv_layer(conv1, [3, 3, output_channel, output_channel], stride=1)
        print("conv2 In Block", conv2.get_shape().as_list())

    # When the channels of input layer and conv2 does not match, we add zero pads to increase the
    # depth of input layers
    if increase_dim is True:
        print("increase_dim = ", increase_dim)
        pooled_input = tf.nn.avg_pool(input_layer, ksize=[1, 2, 2, 1],
                                      strides=[1, 2, 2, 1], padding='VALID')
        print("pooled_input",pooled_input.get_shape().as_list())
        "只在channel这个维度上填充0，将输入层扩充维度， 16-->32，16上下各加8"
        padded_input = tf.pad(pooled_input, [[0, 0], [0, 0], [0, 0], [input_channel // 2,
                                                                     input_channel // 2]])
        print("padded_input", padded_input.get_shape().as_list())
    else:
        print("increase_dim = ", increase_dim)
        padded_input = input_layer

    "将卷积层的输出与原始的输入相加"
    # 这样channel维度一致，才可以相加
    output = conv2 + padded_input
    print("=" * 20)
    return output

def activation_summary(x):
    '''
    :param x: A Tensor
    :return: Add histogram summary and scalar summary of the sparsity of the tensor
    '''
    tensor_name = x.op.name
    tf.summary.histogram(tensor_name + '/activations', x)
    tf.summary.scalar(tensor_name + '/sparsity', tf.nn.zero_fraction(x))


def conv2d(input_, output_dim,
        k_h=3, k_w=3, d_h=2, d_w=2, stddev=0.02,
        name="conv2d"):
    with tf.variable_scope(name):
        w = tf.get_variable('weights', [k_h, k_w, input_.get_shape()[-1], output_dim],
              initializer=tf.truncated_normal_initializer(stddev=stddev))
        variable_summaries(w, name+"weights")
        conv = tf.nn.conv2d(input_, w, strides=[1, d_h, d_w, 1], padding='SAME')

        biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
        variable_summaries(biases, name+"biases")
        conv = tf.nn.relu(tf.nn.bias_add(conv, biases))

    return conv

def upsampling(x, height, width):
    # 临界点插值进行图片的放大，上采样
    # 上采样的过程先不用转置卷积，用tf.image
    with tf.name_scope("image.resize"):
        return tf.image.resize_nearest_neighbor(x, [height, width])


def linear(input_, output_size, scope="Linear", stddev=0.1, bias_start=0.0):

    shape = input_.get_shape().as_list()

    with tf.variable_scope(scope or "Linear"):
        try:
            matrix = tf.get_variable(name="weights", shape=[shape[1], output_size], dtype=tf.float32,
                                     initializer=tf.random_normal_initializer(stddev=stddev))
            variable_summaries(matrix, scope+"weights")
        except ValueError as err:
            msg = "NOTE: Usually, this is due to an issue with the image dimensions. " \
                  " Did you correctly set '--crop' or '--input_height' or '--output_height'?"
            err.args = err.args + (msg,)
            raise
        bias = tf.get_variable("bias", [output_size],
                               initializer=tf.constant_initializer(bias_start))
        variable_summaries(bias, scope+"bias")

        return tf.matmul(input_, matrix) + bias

def conv_out_size_same(size, stride):
    return int(math.ceil(float(size) / float(stride)))
