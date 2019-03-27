import tensorflow as tf
import math
from ops_CNN import *
from train_read_from_tfrecords import batch_size
from tfrecords_train import IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL

NUM_LABELS = IMG_HEIGHT * IMG_WIDTH * IMG_CHANNEL
CONV1_SIZE = 5
CONV1_DEPTH = 16

CONV2_SIZE = 5
CONV2_DEPTH = 16

FC_NODE1 = 256
FC_NODE2 = 256


f_dim = 64
channel_dim = 3


"""生成变量监控信息，并定义生成监控信息日志的操作，var是需要记录的张量"""
"""name给出了在可视化结果中显示的图表名称，这个名称一般与变量名一致"""


def variable_summaries(var, name):

    # 将生成监控信息的操作放在同一个命名空间下
    with tf.name_scope("summaries"):
        # 通过tf.summary.histogram记录张量中元素的取值分布
        tf.summary.histogram(name, var)
        # 计算变量的平均值
        mean = tf.reduce_mean(var)
        """定义生成平均值信息日志的操作"""
        tf.summary.scalar('mean/' + name, mean)
        # 计算变量的标准差
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        """定义生成标准差信息日志的操作"""
        tf.summary.scalar('stddev/' + name, stddev)


def conv_out_size_same(size, stride):
    return int(math.ceil(float(size) / float(stride)))


def inference(input_tensor, train, regularizer):

    # 输入进来的input_tensor [None, 10]
    # 将输入向量还原成图片的像素矩阵

    with tf.variable_scope('input_reshape') as scope:

        "输入的压力数据经过转置卷积形成了图像矩阵"
        # s_h = 252, 400
        s_h, s_w = IMG_HEIGHT, IMG_WIDTH
        print("s_h = ", s_h, "s_w = ", s_w)
        # s_h2 = 126, s_w2 = 200
        s_h2, s_w2 = conv_out_size_same(s_h, 2), conv_out_size_same(s_w, 2)
        print("s_h2 = ", s_h2, "s_w2 = ", s_w2)
        # s_h4 = 63, s_h4 = 100
        s_h4, s_w4 = conv_out_size_same(s_h2, 2), conv_out_size_same(s_w2, 2)
        print("s_h4 = ", s_h4, "s_w4 = ", s_w4)
        # s_h8 = 32, s_h8 = 50
        s_h8, s_w8 = conv_out_size_same(s_h4, 2), conv_out_size_same(s_w4, 2)
        print("s_h8 = ", s_h8, "s_w8 = ", s_w8)
        # s_h16 = 16, s_h16 = 25
        s_h16, s_w16 = conv_out_size_same(s_h8, 2), conv_out_size_same(s_w8, 2)
        print("s_h16 = ", s_h16, "s_w16 = ", s_w16)

        bn_0 = BatchNorm(name="BN_0")
        bn_1 = BatchNorm(name="BN_1")
        bn_2 = BatchNorm(name="BN_2")
        bn_3 = BatchNorm(name="BN_3")

        z = linear(input_=input_tensor, output_size=f_dim * 8 * s_h16 * s_w16)
        h0 = tf.reshape(z, [-1, s_h16, s_w16, f_dim * 8])
        # h0.shape [None, 16, 25, 512]
        h0 = tf.nn.relu(bn_0(h0, train=train))
        print("h0.shape", h0.get_shape().as_list())

        "接下来进行转置卷积"

        h1 = tf.layers.conv2d_transpose(
            inputs=h0,
            filters=f_dim * 4,
            kernel_size=5,
            strides=(
                2,
                2),
            padding="SAME")

        "tf.layers.conv2d_transpose之后不可以加入reshape,会报错"

        h1 = tf.nn.relu(bn_1(h1, train=train))
        # h1.shape [None, 32, 50, 256]
        print("h1.shape", h1.get_shape().as_list())

        h2 = tf.layers.conv2d_transpose(
            inputs=h1,
            filters=f_dim * 2,
            kernel_size=5,
            strides=(
                2,
                2),
            padding="SAME")
        h2 = tf.nn.relu(bn_2(h2, train=train))
        # h2.shape [None, 64, 100, 128]
        print("h2.shape", h2.get_shape().as_list())

        h3 = tf.layers.conv2d_transpose(
            inputs=h2,
            filters=f_dim * 1,
            kernel_size=5,
            strides=(
                2,
                2),
            padding="SAME")
        # h3.shape [None, 128, 200, 64]
        h3 = tf.nn.relu(bn_3(h3, train=train))
        print("h3.shape", h3.get_shape().as_list())

        h4 = tf.layers.conv2d_transpose(
            inputs=h3,
            filters=channel_dim,
            kernel_size=5,
            strides=(
                2,
                2),
            padding="SAME")
        # h4.shape[None, 256, 400, 3]
        print("h4.shape", h4.get_shape().as_list())
        h4 = tf.nn.tanh(h4)

    "转置卷积之后接全连接层"

    with tf.variable_scope("ReshapeAfterDeconv") as scope:
        """将其进行拉直"""
        deconv_shape = h4.get_shape().as_list()
        nodes1 = deconv_shape[1] * deconv_shape[2] * deconv_shape[3]
        # [None, 256*400*3]
        reshaped1 = tf.reshape(h4, [-1, nodes1])
        print("reshaped1 shape", reshaped1.get_shape().as_list())

    "第一层全连接"

    with tf.variable_scope("fully1") as scope:

        with tf.name_scope("weights"):
            fc1_weights = tf.get_variable(
                name="fc1_weights",
                shape=[
                    nodes1,
                    NUM_LABELS],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            variable_summaries(fc1_weights, "fully1" + "/weights")
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))

        with tf.name_scope("biases"):
            fc1_biases = tf.get_variable(
                name="fc1_biases",
                shape=[NUM_LABELS],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc1_biases, "fully1" + "/biases")
        # [batch_size, FC_NODE1]
        fc1 = tf.nn.relu(tf.matmul(reshaped1, fc1_weights) + fc1_biases)
        if train:
            print("第一个全连接, train = ", train, "drop out")
            fc1 = tf.nn.dropout(fc1, 0.4)

    "第二层全连接"

    with tf.variable_scope("fully2") as scope:

        with tf.name_scope("weights"):
            fc2_weights = tf.get_variable(
                name="fc2_weights",
                shape=[
                    FC_NODE1,
                    NUM_LABELS],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            variable_summaries(fc2_weights, "fully2" + "/weights")
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc2_weights))

        with tf.name_scope("biases"):
            fc2_biases = tf.get_variable(
                name="fc2_biases",
                shape=[NUM_LABELS],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc2_biases, "fully2" + "/biases")
        # [batch_size, FC_NODE1]
        fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)
        if train:
            print("第二个全连接, train = ", train, "drop out")
            fc2 = tf.nn.dropout(fc2, 0.4)

    "卷积之前reshape一下,变成4维矩阵"

    with tf.variable_scope("ReshapeBeforeCONV") as scope:
        output_array1 = tf.reshape(
            fc2, [-1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL])
        # [None, 252, 400, 3]
        print("output_array1", output_array1.get_shape().as_list())

    with tf.variable_scope("CONV1") as scope:

        with tf.name_scope("weights"):
            conv1_weights = tf.get_variable(
                name="conv1_weights",
                shape=[
                    CONV1_SIZE,
                    CONV1_SIZE,
                    IMG_CHANNEL,
                    CONV1_DEPTH],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1),
            )
            variable_summaries(conv1_weights, "conv1" + "/weights")
        with tf.name_scope("biases"):
            conv1_biases = tf.get_variable(
                name="conv1_bias",
                shape=[CONV1_DEPTH],
                initializer=tf.constant_initializer(0.0),
            )
            variable_summaries(conv1_biases, "conv1" + "/biases")
        # 卷积步长为2，"SAME" ，图像尺寸减半
        conv1 = tf.nn.conv2d(
            output_array1, conv1_weights, strides=[
                1, 2, 2, 1], padding="SAME")
        # CONV1 shape [batch, 126, 200, CONV1_DEPTH]
        print("CONV1 shape", conv1.get_shape().as_list())
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    with tf.variable_scope("pool1") as scope:
        pool1 = tf.nn.max_pool(
            relu1, ksize=[
                1, 2, 2, 1], strides=[
                1, 2, 2, 1], padding="SAME")
        # POOL1 shape [batch,63, 100, CONV1_DEPTH]
        print("POOL1 shape", pool1.get_shape().as_list())

    with tf.variable_scope("CONV2") as scope:

        with tf.name_scope("weights"):
            conv2_weights = tf.get_variable(
                name="conv2_weights",
                shape=[
                    CONV2_SIZE,
                    CONV2_SIZE,
                    CONV1_DEPTH,
                    CONV2_DEPTH],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1),
            )
            variable_summaries(conv2_weights, "conv2" + "/weights")
        with tf.name_scope("biases"):
            conv2_biases = tf.get_variable(
                "conv2_bias",
                shape=[CONV2_DEPTH],
                initializer=tf.constant_initializer(0.0),
            )
            variable_summaries(conv2_biases, "conv2" + "/biases")
        conv2 = tf.nn.conv2d(
            pool1, conv2_weights, strides=[
                1, 2, 2, 1], padding="SAME")
        # CONV2 shape [batch, 32, 50, CONV2_DEPTH]
        print("CONV2 shape", conv2.get_shape().as_list())
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.variable_scope("pool2") as scope:
        pool2 = tf.nn.max_pool(
            relu2, ksize=[
                1, 2, 2, 1], strides=[
                1, 2, 2, 1], padding="SAME")
        # POOL2 shape [batch, 16, 25, CONV2_DEPTH]
        print("POOL2 shape", pool2.get_shape().as_list())

    with tf.variable_scope("ReshapeAfterCONV") as scope:
        """将其进行拉直"""
        pool_shape = pool2.get_shape().as_list()
        nodes2 = pool_shape[1] * pool_shape[2] * pool_shape[3]
        # [batch_size, 16*25*32]
        reshaped2 = tf.reshape(pool2, [-1, nodes2])
        print("reshaped2 shape", reshaped2.get_shape().as_list())

    "第三层全连接"

    with tf.variable_scope("fully3") as scope:

        with tf.name_scope("weights"):
            fc3_weights = tf.get_variable(
                name="fc3_weights",
                shape=[
                    nodes2,
                    FC_NODE2],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            variable_summaries(fc3_weights, "fully3" + "/weights")
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc3_weights))

        with tf.name_scope("biases"):
            fc3_biases = tf.get_variable(
                name="fc3_biases",
                shape=[FC_NODE2],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc3_biases, "fully3" + "/biases")
        # [batch_size, FC_NODE]
        fc3 = tf.nn.relu(tf.matmul(reshaped2, fc3_weights) + fc3_biases)
        if train:
            print("第三个全连接, train = ", train, "drop out")
            fc3 = tf.nn.dropout(fc3, 0.4)

    "第四层全连接"

    with tf.variable_scope("fully4") as scope:

        with tf.name_scope("weights"):
            fc4_weights = tf.get_variable(
                name="fc4_weights",
                shape=[
                    FC_NODE2,
                    NUM_LABELS],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            variable_summaries(fc4_weights, "fully4" + "/weights")
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(fc4_weights))

        with tf.name_scope("biases"):
            fc4_biases = tf.get_variable(
                name="fc4_biases",
                shape=[NUM_LABELS],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc4_biases, "fully4" + "/biases")
        # [batch_size, 252*400*3]
        fc4 = tf.add(tf.matmul(fc3, fc4_weights), fc4_biases)
        if train:
            print("第四个全连接，train = ", train, "drop out")
            fc4 = tf.nn.dropout(fc4, 0.4)

    "最后的reshape"

    with tf.variable_scope("output_reshape") as scope:
        output_array2 = tf.reshape(
            fc4, [-1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL])
        # output_shape.dtype <dtype: 'float32'>
        # output_shape [None, 252, 400, 3]
        print("output_shape.dtype", output_array2.dtype)
        print("output_shape", output_array2.get_shape().as_list())
        # TypeError: Value passed to parameter 'x' has DataType uint8 not in list of allowed values:
        # float16, bfloat16, float32, float64, int32, int64, complex64, complex128
        "这里不能将其转为uint8类型的！！！"
        # output_array = tf.cast(output_array, tf.uint8)

    """记录网络输出节点取值的分布"""
    tf.summary.histogram("output_array", output_array2)
    """输出为[batch_size, 252, 400, 3]"""
    return output_array2
