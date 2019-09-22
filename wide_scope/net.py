import tensorflow as tf
from ops import *
from tfrecords_train import IMG_HEIGHT, IMG_WIDTH
from train_read_from_tfrecords import batch_size
import os


NUM_LABELS = IMG_HEIGHT * IMG_WIDTH

CONV1_DEPTH = 2
CONV2_DEPTH = 4
CONV3_DEPTH = 8
CONV4_DEPTH = 16
CONV5_DEPTH = 32
CONV6_DEPTH = 64
CONV7_DEPTH = 128
CONV8_DEPTH = 256

FC_NODE = 512

f_dim = 32

channel_dim = 1

s_h, s_w = IMG_HEIGHT, IMG_WIDTH
# 403,640
s_h2, s_w2 = conv_out_size_same(s_h, 2), conv_out_size_same(s_w, 2)
print("s_h2=", s_h2, "s_w2=",s_w2)
# 202, 320
s_h4, s_w4 = conv_out_size_same(s_h2, 2), conv_out_size_same(s_w2, 2)
print("s_h4=", s_h4, "s_w4=",s_w4)
# 101, 160
s_h8, s_w8 = conv_out_size_same(s_h4, 2), conv_out_size_same(s_w4, 2)
print("s_h8=", s_h8, "s_w8=",s_w8)
# 51, 80
s_h16, s_w16 = conv_out_size_same(s_h8, 2), conv_out_size_same(s_w8, 2)
print("s_h16=", s_h16, "s_w16=",s_w16)
# 26, 40
s_h32, s_w32 = conv_out_size_same(s_h16, 2), conv_out_size_same(s_w16, 2)
print("s_h32=", s_h32, "s_w32=",s_w32)
# 13, 20
s_h64, s_w64 = conv_out_size_same(s_h32, 2), conv_out_size_same(s_w32, 2)
print("s_h64=", s_h64, "s_w64=",s_w64)
# 7, 10
s_h128, s_w128 = conv_out_size_same(s_h64, 2), conv_out_size_same(s_w64, 2)
print("s_h128=", s_h128, "s_w128=",s_w128)
# 4，5
s_h256, s_w256 = conv_out_size_same(s_h128, 2), conv_out_size_same(s_w128, 2)
print("s_h256=", s_h256, "s_w256=",s_w256)
# 2, 3

print("=" * 20)

d_bn_0 = BatchNorm(name="d_bn_0")
d_bn_1 = BatchNorm(name="d_bn_1")
d_bn_2 = BatchNorm(name="d_bn_2")
d_bn_3 = BatchNorm(name="d_bn_3")
d_bn_4 = BatchNorm(name="d_bn_4")
d_bn_5 = BatchNorm(name="d_bn_5")
d_bn_6 = BatchNorm(name="d_bn_6")
d_bn_7 = BatchNorm(name="d_bn_7")
d_bn_8 = BatchNorm(name="d_bn_8")

c_bn_0 = BatchNorm(name="c_bn_0")
c_bn_1 = BatchNorm(name="c_bn_1")
c_bn_2 = BatchNorm(name="c_bn_2")
c_bn_3 = BatchNorm(name="c_bn_3")
c_bn_4 = BatchNorm(name="c_bn_4")
c_bn_5 = BatchNorm(name="c_bn_5")
c_bn_6 = BatchNorm(name="c_bn_6")


def inference(input_tensor, train, regularizer):

    "convert the pressure data 2-D  to  4-D Tensor"
    z1 = linear(input_=input_tensor, output_size=f_dim * 8 ,scope="Linear_1")
    z2 = linear(input_=z1, output_size=f_dim * 8 * s_w256 * s_h256, scope="Linear_2")
    "这里一定要给出明确的shape，而不能是-1，转置卷积和卷积在一起使用时，需要明确给出形状"
    h0 = tf.reshape(z2, [batch_size, s_h256, s_w256, f_dim * 8])
    h0 = tf.nn.elu(d_bn_0(h0, train=train))

    with tf.variable_scope("Deconv"):
        h1 = deconv2d(input_=h0, output_shape=[batch_size, s_h128, s_w128, f_dim * 4], name="deconv1")
        h1 = tf.nn.elu(d_bn_1(h1, train=train))

        h2 = deconv2d(input_=h1, output_shape=[batch_size, s_h64, s_w64, f_dim * 2], name="deconv2")
        h2 = tf.nn.elu(d_bn_2(h2, train=train))

        h3 = deconv2d(input_=h2, output_shape=[batch_size, s_h32, s_w32, f_dim], name="deconv3")
        h3 = tf.nn.elu(d_bn_3(h3, train=train))

        h4 = deconv2d(input_=h3, output_shape=[batch_size, s_h16, s_w16, f_dim//2], name="deconv4")
        h4 = tf.nn.elu(d_bn_4(h4, train=train))

        h5 = deconv2d(input_=h4, output_shape=[batch_size, s_h8, s_w8, f_dim //4], name="deconv5")
        h5 = tf.nn.elu(d_bn_5(h5, train=train))

        h6 = deconv2d(input_=h5, output_shape=[batch_size, s_h4, s_w4, f_dim//8], name="deconv6")
        h6 = tf.nn.elu(d_bn_6(h6, train=train))

        h7 = deconv2d(input_=h6, output_shape=[batch_size, s_h2, s_w2, f_dim//16], name="deconv7")
        h7 = tf.nn.elu(d_bn_7(h7, train=train))

        h8 = deconv2d(input_=h7, output_shape=[batch_size, s_h, s_w, channel_dim], name="deconv8")
        h8 = tf.nn.tanh(d_bn_8(h8, train=train))

    print("=" * 20)

    with tf.variable_scope("Conv"):
        conv1 = tf.nn.elu(conv2d(input_=h8, output_dim=CONV1_DEPTH, name="conv1"))
        conv2 = tf.nn.elu(c_bn_0(conv2d(input_=conv1, output_dim=CONV2_DEPTH, name="conv2"), train=train))
        conv3 = tf.nn.elu(c_bn_1(conv2d(input_=conv2, output_dim=CONV3_DEPTH, name="conv3"), train=train))
        conv4 = tf.nn.elu(c_bn_2(conv2d(input_=conv3, output_dim=CONV4_DEPTH, name="conv4"), train=train))
        conv5 = tf.nn.elu(c_bn_3(conv2d(input_=conv4, output_dim=CONV5_DEPTH, name="conv5"), train=train))
        conv6 = tf.nn.elu(c_bn_4(conv2d(input_=conv5, output_dim=CONV6_DEPTH, name="conv6"), train=train))
        conv7 = tf.nn.elu(c_bn_5(conv2d(input_=conv6, output_dim=CONV7_DEPTH, name="conv7"), train=train))
        conv8 = tf.nn.elu(c_bn_6(conv2d(input_=conv7, output_dim=CONV8_DEPTH, name="conv8"), train=train))

    with tf.variable_scope("Avg_Pool"):
        pool1 = tf.nn.avg_pool(conv8, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding="SAME")
        print("pool1_shape", pool1.get_shape())

    with tf.variable_scope("Fully_reshape"):
        pool_shape = pool1.get_shape().as_list()
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        reshaped = tf.reshape(pool1, [batch_size, -1])
        print("reshaped.shape", reshaped.get_shape())

    z3 = linear(input_=reshaped, output_size=FC_NODE, scope="Linear_3", regularizer=regularizer)
    z3 = tf.nn.elu(z3)

    z4 = linear(input_=z3, output_size=NUM_LABELS, scope="Linear_4", regularizer=regularizer)

    output_array = tf.reshape(z4, [-1, IMG_HEIGHT, IMG_WIDTH])
    # (64, 252, 400)
    print("output_array.shape", output_array.get_shape())

    return output_array
