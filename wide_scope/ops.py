import tensorflow as tf
import math


def conv_out_size_same(size, stride):
    return int(math.ceil(float(size) / float(stride)))


def variable_summaries(var, name):

    with tf.name_scope("summaries"):
        tf.summary.histogram(name, var)
        mean = tf.reduce_mean(var)
        tf.summary.scalar('mean/' + name, mean)
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


def linear(input_, output_size, scope="Linear", regularizer=None, stddev=0.1, bias_start=0.1):
    shape = input_.get_shape().as_list()
    with tf.variable_scope(scope):

        matrix = tf.get_variable(name="weights", shape=[shape[1], output_size], dtype=tf.float32,
                                 initializer=tf.truncated_normal_initializer(stddev=stddev))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(matrix))
        variable_summaries(matrix, scope+"weights")
        bias = tf.get_variable("bias", [output_size],
                               initializer=tf.constant_initializer(bias_start))
        variable_summaries(bias, scope+"bias")

        return tf.matmul(input_, matrix) + bias


def conv2d(input_, output_dim, k_h=2, k_w=2, d_h=2, d_w=2, stddev=0.02,name="conv2d"):
    with tf.variable_scope(name):
        w = tf.get_variable('weights', [k_h, k_w, input_.get_shape()[-1], output_dim],
              initializer=tf.truncated_normal_initializer(stddev=stddev))
        variable_summaries(w, name+"_weights")
        conv = tf.nn.conv2d(input_, w, strides=[1, d_h, d_w, 1], padding='SAME')

        biases = tf.get_variable('biases', [output_dim], initializer=tf.constant_initializer(0.0))
        variable_summaries(biases, name+"_biases")
        "卷积之后也接了reshape， 这里没有接激活函数"
        # conv = tf.reshape(tf.nn.bias_add(conv, biases), conv.get_shape())
        conv = tf.reshape(tf.nn.bias_add(conv, biases), conv.get_shape())
        print(name+"_shape", conv.get_shape())

    return conv


def deconv2d(input_, output_shape,k_h=2, k_w=2, d_h=2, d_w=2, stddev=0.02,name="deconv2d"):
    with tf.variable_scope(name):
        # filter : [height, width, output_channels, in_channels]
        w = tf.get_variable(name='w', shape=[k_h, k_w, output_shape[-1], input_.get_shape()[-1]],
                            initializer=tf.random_normal_initializer(stddev=stddev))
        variable_summaries(w, name+"_weights")
        deconv = tf.nn.conv2d_transpose(input_, w, output_shape=output_shape, strides=[1, d_h, d_w, 1])
        biases = tf.get_variable(name='biases', shape=[output_shape[-1]], initializer=tf.constant_initializer(0.1))
        variable_summaries(biases, name + "_bias")
        deconv = tf.reshape(tf.nn.bias_add(deconv, biases), deconv.get_shape())
        print(name+"_shape", deconv.get_shape())

        return deconv


def lrelu(x, leak=0.2, name="leaky_relu1"):
    with tf.variable_scope(name):
        return tf.maximum(x, leak*x)
