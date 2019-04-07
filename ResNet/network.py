import tensorflow as tf
from ops import *
from tfrecords_train import IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL


NUM_LABELS = IMG_HEIGHT*IMG_WIDTH*IMG_CHANNEL

FC_NODE = 256

f_dim = 64

CONV0_Depth = 16
CONV0_SIZE = 3

CONV2_Depth = 32
CONV3_Depth = 64

def inference(input_tensor_batch, num_residual_blocks, reuse, regularizer, train):

    layers = []
    with tf.variable_scope('input_reshape'):

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
        print("=" * 20)

        d_bn_0 = BatchNorm(name="d_bn_0")
        c_bn_1 = BatchNorm(name="c_bn_1")
        c_bn_2 = BatchNorm(name="c_bn_2")
        c_bn_3 = BatchNorm(name="c_bn_3")

        z = linear(input_=input_tensor_batch, output_size=f_dim * 8 * s_h16 * s_w16)
        h0 = tf.reshape(z, [-1, s_h16, s_w16, f_dim * 8])
        h0 = tf.nn.relu(d_bn_0(h0))
        # [None, 16, 25, 512]
        print("h0.shape", h0.get_shape().as_list())

        h1 = upsampling(h0, s_h8, s_w8)
        # [None, 32, 50, 512]
        print("h1.shape", h1.get_shape().as_list())
        h1 = c_bn_1(conv2d(input_=h1, output_dim=f_dim * 4, d_h=1, d_w=1, name="conv_upsample1"))
        # [None, 32, 50, 256]
        print("h1.shape", h1.get_shape().as_list())

        h2 = upsampling(h1, s_h4, s_w4)
        # [None, 63, 100, 256]
        print("h2.shape", h2.get_shape().as_list())
        h2 = c_bn_2(conv2d(input_=h2, output_dim=f_dim * 2, d_h=1, d_w=1, name="conv_upsample2"))
        # [None, 63, 100, 128]
        print("h2.shape", h2.get_shape().as_list())

        h3 = upsampling(h2, s_h2, s_w2)
        # [None, 126, 200, 128]
        print("h3.shape", h3.get_shape().as_list())
        h3 = c_bn_3(conv2d(input_=h3, output_dim=f_dim, d_h=1, d_w=1, name="conv_upsample3"))
        # [None, 126, 200, 64]
        print("h3.shape", h3.get_shape().as_list())

        h4 = upsampling(h3, s_h, s_w)
        # [None, 252, 400, 64]
        print("h4.shape", h4.get_shape().as_list())
        h4 = conv2d(input_=h4, output_dim=f_dim//2, d_h=1, d_w=1, name="conv_upsample4")
        # [None, 252, 400, 32]
        print("h4.shape", h4.get_shape().as_list())


    with tf.variable_scope('conv0', reuse=reuse):
        conv0 = conv_bn_relu_layer(input_layer=h4,
                                   filter_shape=[CONV0_SIZE, CONV0_SIZE, h4.get_shape().as_list()[-1], CONV0_Depth],
                                   stride=1)
        # [None, 252, 400, 16]
        print("conv0.shape", conv0.get_shape().as_list())
        activation_summary(conv0)
        layers.append(conv0)
        print("=" * 20)

    for i in range(num_residual_blocks):
        "第一个循环，block的channel都是16"
        print("i = ", i)
        with tf.variable_scope('conv1_%d' % i, reuse=reuse):
            print("conv1_%d" % i)
            if i == 0:
                "第一个block"
                "这里channel没有发生改变"
                conv1 = residual_block(input_layer=layers[-1], output_channel=CONV0_Depth, first_block=True)
            else:
                conv1 = residual_block(input_layer=layers[-1], output_channel=CONV0_Depth)
            activation_summary(conv1)
            layers.append(conv1)
    print("*" * 20)
    for i in range(num_residual_blocks):
        "第二个循环，block的channel都是32，与上一个循环不一样"
        print("i = ", i)
        with tf.variable_scope('conv2_%d' %i, reuse=reuse):
            "这里input_channel和output_channel不一样"
            print("conv2_%d" % i)
            conv2 = residual_block(input_layer=layers[-1], output_channel=CONV2_Depth)
            activation_summary(conv2)
            layers.append(conv2)
    print("*" * 20)
    for i in range(num_residual_blocks):
        "第三个循环，block的channel都是64，与上一个循环不一样"
        print("i = ", i)
        with tf.variable_scope('conv3_%d' %i, reuse=reuse):
            print("conv3_%d" % i)
            conv3 = residual_block(input_layer=layers[-1], output_channel=CONV3_Depth)
            layers.append(conv3)
        "判断卷积之后的结果的后三个维度是不是[63,100,64]"
        assert conv3.get_shape().as_list()[1:] == [63, 100, 64]


    with tf.variable_scope("fullly_reshape"):
        """将其进行拉直"""
        pool_shape = layers[-1].get_shape().as_list()
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        reshaped = tf.reshape(layers[-1], [-1, nodes])
        print("reshaped shape", reshaped.get_shape().as_list())

    with tf.variable_scope("fully1"):

        with tf.name_scope("weights"):
            fc1_weights = tf.get_variable(
                name="fc1_weights",
                shape=[
                    nodes,
                    FC_NODE],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            print("fc1_weights", fc1_weights.get_shape())
            variable_summaries(fc1_weights, "fully1" + "/weights")
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))

        with tf.name_scope("biases"):
            fc1_biases = tf.get_variable(
                name="fc1_biases",
                shape=[FC_NODE],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc1_biases, "fully1" + "/biases")
        # [batch_size, FC_NODE]
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            # dropout在训练时会随即将部分节点的输出改为0
            # 有可能就是造成我fully权重都是0的罪魁祸首
            fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope("fully2"):

        with tf.name_scope("weights"):
            fc2_weights = tf.get_variable(
                name="fc2_weights",
                shape=[
                    FC_NODE,
                    NUM_LABELS],
                initializer=tf.truncated_normal_initializer(
                    stddev=0.1))
            print("fc2_weights", fc2_weights.get_shape())
            variable_summaries(fc2_weights, "fully2" + "/weights")
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(fc2_weights))

        with tf.name_scope("biases"):
            fc2_biases = tf.get_variable(
                name="fc2_biases",
                shape=[NUM_LABELS],
                initializer=tf.constant_initializer(0.1))
            variable_summaries(fc2_biases, "fully2" + "/biases")
        # [batch_size, 252*400*3]
        fc2 = tf.matmul(fc1, fc2_weights)+fc2_biases
        "去掉最后一层的dropout"
        # if train:
        #     fc2 = tf.nn.dropout(fc2, 0.4)

    with tf.variable_scope("output_reshape"):
        output_array = tf.reshape(fc2, [-1, IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL])
        print("output_shape", output_array.get_shape().as_list())
        layers.append(output_array)

    return layers[-1]
