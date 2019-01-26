# DCGAN 学习笔记--代码

标签（空格分隔）： DCGAN

---

最近一段时间在学习生成对抗网络的内容(GAN)，并且用代码实现了DCGAN，写下这篇笔记，记录自己的学习历程。  
****
[DCGAN代码来源](https://github.com/carpedm20/DCGAN-tensorflow)  
****  
``` Python
import os
import numpy as np

from model import DCGAN
from utils import pp, visualize,  show_all_variables

import tensorflow as tf


flags = tf.app.flags
flags.DEFINE_integer("epoch", 25, "Epoch to train [25]")
flags.DEFINE_float("learning_rate", 0.0002, "Learning rate of for adam [0.0002]")
flags.DEFINE_float("beta1", 0.5, "Momentum term of adam [0.5]")
flags.DEFINE_float("train_size", np.inf, "The size of train images [np.inf]")
flags.DEFINE_integer("batch_size", 16, "The size of batch images [64]")
flags.DEFINE_integer("input_height", 504, "The size of image to use (will be center cropped). [108]")
flags.DEFINE_integer("input_width", 800,
                     "The size of image to use (will be center cropped). If None, same value as input_height [None]")
flags.DEFINE_integer("output_height", 100, "The size of the output images to produce [64]")
flags.DEFINE_integer("output_width", 158,
                     "The size of the output images to produce. If None, same value as output_height [None]")
# 指定处理哪个数据集
flags.DEFINE_string("dataset", "6400", "The name of dataset [celebA, mnist, lsun]")
flags.DEFINE_string("input_fname_pattern", "*.jpg", "Glob pattern of filename of input images [*]")
flags.DEFINE_string("checkpoint_dir", "checkpoint", "Directory name to save the checkpoints [checkpoint]")
flags.DEFINE_string("data_dir", "./data", "Root directory of dataset [data]")
# sample_dir 存放图片样本的目录
flags.DEFINE_string("sample_dir", "samples", "Directory name to save the image samples [samples]")
flags.DEFINE_boolean("train", False, "True for training, False for testing [False]")
flags.DEFINE_boolean("crop", True, "True for training, False for testing [False]")
flags.DEFINE_boolean("visualize", False, "True for visualizing, False for nothing [False]")
flags.DEFINE_integer("generate_test_images", 100, "Number of images to generate during test. [100]")

FLAGS = flags.FLAGS

"""注意这里main函数括号里的下划线_，没有会报错"""
def main(_):
    # step1：首先是打印参数数据
     # flags.FLAGS.__flags为包含了所有输入的列表
    pp.pprint(flags.FLAGS.__flags)

    # 判断输入图像、输出图像的宽是否指定，如果没有指定，则等于其图像的高。
    if FLAGS.input_width is None:
        FLAGS.input_width = FLAGS.input_height
    if FLAGS.output_width is None:
        FLAGS.output_width = FLAGS.output_height
    # 然后判断checkpoint和sample的文件是否存在，不存在则创建。
    if not os.path.exists(FLAGS.checkpoint_dir):
        os.makedirs(FLAGS.checkpoint_dir)
    if not os.path.exists(FLAGS.sample_dir):
        os.makedirs(FLAGS.sample_dir)

    # 控制GPU资源使用率
    # gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
    run_config = tf.ConfigProto(allow_soft_placement=True)
    run_config.gpu_options.allocator_type='BFC'
    run_config.gpu_options.per_process_gpu_memory_fraction=0.90
    run_config.gpu_options.allow_growth=True


    with tf.Session(config=run_config) as sess:


        dcgan = DCGAN(
            sess,
            input_width=FLAGS.input_width,
            input_height=FLAGS.input_height,
            output_width=FLAGS.output_width,
            output_height=FLAGS.output_height,
            batch_size=FLAGS.batch_size,
            sample_num=FLAGS.batch_size,
            z_dim=FLAGS.generate_test_images,
            dataset_name=FLAGS.dataset,
            input_fname_pattern=FLAGS.input_fname_pattern,
            crop=FLAGS.crop,
            checkpoint_dir=FLAGS.checkpoint_dir,
            sample_dir=FLAGS.sample_dir,
            data_dir=FLAGS.data_dir)

        show_all_variables()
        if FLAGS.train:
            print("-.-" * 10)
            print("进行训练")
            dcgan.train(FLAGS)
        else:
            print("进行测试")
            if not dcgan.load(FLAGS.checkpoint_dir)[0]:
                raise Exception("[!] Train a model first, then run test mode")

        OPTION = 1
        visualize(sess, dcgan, FLAGS, OPTION)


if __name__ == '__main__':
    tf.app.run()

```  
- [x] 以上这份代码叫作main.py，作为程序的入口主函数，之后在服务器中输入 python main.py运行即可.  
- [x] 这份代码主要学到的是如何设置GPU计算的方法以及如何使用命令行参数  
****  
``` Python
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

```  
- [x] 这份代码叫作ops.py,主要实现的功能就是定义了网络中的一些运算，包括卷积，转置卷积，线性运算(x*w+b)以及激活函数leakyRelu，还有关于日志函数的部分，并且定义了BN层的类，用于之后调用类的实例。  
****  
``` Python
"""
Some codes from https://github.com/Newmu/dcgan_code
"""
"这份代码主要是定义了各种对图像处理的函数，相当于其他3个文件的头文件。"
import math
import imageio
import random
import pprint
import scipy.misc
import numpy as np
from time import gmtime, strftime
import cv2
import tensorflow as tf
import tensorflow.contrib.slim as slim


pp = pprint.PrettyPrinter()
get_stddev = lambda x, k_h, k_w: 1/math.sqrt(k_w*k_h*x.get_shape()[-1])


def show_all_variables():
    # tf.trainable_variables()返回的是一个列表
    print("列出所有的变量")
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)

"imread函数返回的是numpy数组"
def imread(path, grayscale = False):
    # print("-.-" * 10)
    # print("进入读取图片的函数 imread")
    if (grayscale):
        # print("图片为灰度图片，读取图片")
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        # print("图片为彩色图片，读取图片")
        return cv2.imread(path)


def get_image(image_path, input_height, input_width,
              resize_height=100, resize_width=158,
              crop=False, grayscale=False):
    # print("-.-" * 10)
    # print("进入获取图片的函数 get_image")
    image = imread(image_path, grayscale)
    # print("读取图片返回的结果是", type(image))
    return transform(image, input_height, input_width,
                     resize_height, resize_width, crop)


"transform函数的作用就是进行resize"
def transform(image, input_height, input_width,
              resize_height=100, resize_width=158, crop=False):
    # print("-.-" * 10)
    # print("进入transform函数")
    if crop:
        # print("进行裁剪")
        cropped_image = center_crop(
            image, input_height, input_width,
            resize_height, resize_width)
    else:
        # print("不进行裁剪")
        cropped_image = cv2.resize(src=image, dsize=(resize_width, resize_height))
        "这里进行了修改，直接返回了resize之后的"
    # print("transform函数的结果是", cropped_image.shape)
    return cropped_image


def center_crop(x, crop_h, crop_w,
                resize_h=100, resize_w=158):
    if crop_w is None:
        crop_w = crop_h
    h, w = x.shape[:2]
    j = int(round((h - crop_h)/2.))
    i = int(round((w - crop_w)/2.))
    "要注意这个resize函数图片的高和宽与TensorFlow是相反的"
    return cv2.resize(
      src=x[j:j+crop_h, i:i+crop_w], dsize=(resize_w, resize_h))


"以上是获得图片的函数，以下是保存图片的函数"


def save_images(images, size, image_path):
    # numpy 数组 [64, 100, 158, 3]
    print("传入save_images函数的 images 是", type(images),"维度", images.shape)
    print("传入的size", size)
    return imsave(inverse_transform(images), size, image_path)

def imsave(images, size, path):
    print("进入 imsave 函数")
    image = np.squeeze(merge(images, size))
    print("merge函数成功完成，结果是", image.shape)   # [400, 632, 3]
    print("现在merger函数中的image是", image.shape)
    return scipy.misc.imsave(path, image)


def inverse_transform(images):
    print("进入 inverse_transform 函数")
    print("inverse_transform 的shape", images.shape)   #[16, 100, 158, 3]
    return (images+1.)/2.


def merge_images(images, size):
    return inverse_transform(images)


def merge(images, size):
    print("进入 merge 函数")
    print("把16张照片合成一张照片")
    h, w = images.shape[1], images.shape[2]
    # h 100, w 158
    print("h", h, "w", w)
    if (images.shape[3] in (3,4)):
        # print("images.shape[3]=", images.shape[3]) # 3
        c = images.shape[3]
        # h * size[0]=100 * 4= 400
        # w * size[1]=158 * 4 = 632
        img = np.zeros((h * size[0], w * size[1], c))
        # print("img-shape", img.shape)   # [400, 632,3]
        for idx, image in enumerate(images):
            # print("idx", idx)  idx[0-15]
            # print("image", type(image),"维度是", image.shape)  numpy数组，[100, 158, 3]
            # size[1] = 4
            i = idx % size[1] # [0123 0123 0123 0123]
            # print("i",i)
            j = idx // size[1]  #[0000 1111 2222 3333]
            # print("j", j)
            img[j * h:j * h + h, i * w:i * w + w, :] = image

        print("img", img.shape) # [400, 632, 3]
        return img
    # elif images.shape[3]==1:
    #     img = np.zeros((h * size[0], w * size[1]))
    #     for idx, image in enumerate(images):
    #         i = idx % size[1]
    #         j = idx // size[1]
    #         img[j * h:j * h + h, i * w:i * w + w] = image[:,:,0]
    #     return img
    else:
        raise ValueError('in merge(images,size) images parameter '
                         'must have dimensions: HxW or HxWx3 or HxWx4')



def image_manifold_size(num_images):
    print("进入 image_manifold_size 函数")
    print("传入 image_manifold_size 函数的参数是", num_images)   #32
    # 5
    manifold_h = int(np.floor(np.sqrt(num_images)))
    # print("manifold_h", manifold_h)
    # 5
    manifold_w = int(np.ceil(np.sqrt(num_images)))
    # print("manifold_w", manifold_w)

    # print("判断以下这步是否正确")
    assert manifold_h * manifold_w == num_images
    print("assert 正确")
    "返回两个元素，返回的是元组"
    return manifold_h, manifold_w


def make_gif(images, fname, duration=2, true_image=False):
    import moviepy.editor as mpy

    def make_frame(t):
        try:
            x = images[int(len(images)/duration*t)]
        except:
            x = images[-1]

        if true_image:
            return x.astype(np.uint8)
        else:
            return ((x+1)/2*255).astype(np.uint8)

    clip = mpy.VideoClip(make_frame, duration=duration)
    clip.write_gif(fname, fps = len(images) / duration)

def visualize(sess, dcgan, config, option):
    image_frame_dim = int(math.ceil(config.batch_size**.5))
    if option == 0:
        z_sample = np.random.uniform(-0.5, 0.5, size=(config.batch_size, dcgan.z_dim))
        samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
        save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_%s.png' % strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
    elif option == 1:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.random.uniform(-1, 1, size=(config.batch_size , dcgan.z_dim))
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            if config.dataset == "mnist":
                y = np.random.choice(10, config.batch_size)
                y_one_hot = np.zeros((config.batch_size, 10))
                y_one_hot[np.arange(config.batch_size), y] = 1

                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample, dcgan.y: y_one_hot})
            else:
                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})

            save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_arange_%s.png' % (idx))
    elif option == 2:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in [random.randint(0, dcgan.z_dim - 1) for _ in range(dcgan.z_dim)]:
            print(" [*] %d" % idx)
            z = np.random.uniform(-0.2, 0.2, size=(dcgan.z_dim))
            z_sample = np.tile(z, (config.batch_size, 1))
            #z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            if config.dataset == "mnist":
                y = np.random.choice(10, config.batch_size)
                y_one_hot = np.zeros((config.batch_size, 10))
                y_one_hot[np.arange(config.batch_size), y] = 1

                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample, dcgan.y: y_one_hot})
            else:
                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})

            try:
                make_gif(samples, './samples/test_gif_%s.gif' % (idx))
            except:
                save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_%s.png' % strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
    elif option == 3:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
            make_gif(samples, './samples/test_gif_%s.gif' % (idx))
    elif option == 4:
        image_set = []
        values = np.arange(0, 1, 1./config.batch_size)

        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample): z[idx] = values[kdx]

            image_set.append(sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample}))
            make_gif(image_set[-1], './samples/test_gif_%s.gif' % (idx))

        new_image_set = [merge(np.array([images[idx] for images in image_set]), [10, 10]) \
                         for idx in range(64) + range(63, -1, -1)]
        make_gif(new_image_set, './samples/test_gif_merged.gif', duration=8)




```  
- [x] 这份代码是utils.py，主要定义了关于图像的一些操作，大体上分为得到图片和保存图片两大部分，以及之后的制作动图可视化的部分。这部分可修改的地方很多，需要根据自己的需要进行改正。  
****
``` Python
import os
import time
import math
# 通配符
from glob import glob
import cv2
import tensorflow as tf
import numpy as np
from ops import *
from utils import *


# 定义了卷积之后的大小。输入为卷积之前的大小和步长
def conv_out_size_same(size, stride):
    return int(math.ceil(float(size) / float(stride)))


class DCGAN(object):

    def __init__(self, sess, input_height=504, input_width=800, crop=True,
                 batch_size=16, sample_num=16, output_height=100, output_width=158,
                 y_dim=None, z_dim=100, gf_dim=64, df_dim=64,
                 gfc_dim=1024, dfc_dim=1024, c_dim=3, dataset_name='6400',
                 input_fname_pattern='*.jpg', checkpoint_dir=None,
                 sample_dir=None, data_dir='E:/PycharmProjects/pictures/'):
        print("创建DCGAN实例")

        self.sess = sess
        # 不裁剪
        self.crop = crop

        self.batch_size = batch_size
        self.sample_num = sample_num

        self.input_height = input_height
        self.input_width = input_width
        self.output_height = output_height
        self.output_width = output_width
        "这里有个疑问，y轴和z轴分别指的是？"
        self.y_dim = y_dim
        self.z_dim = z_dim

        self.gf_dim = gf_dim
        self.df_dim = df_dim

        self.gfc_dim = gfc_dim
        self.dfc_dim = dfc_dim

        # batch normalization : deals with poor initialization helps gradient flow
        # 判别器的BN层，创建类实例的时候不需要输入参数
        self.d_bn1 = BatchNorm(name='d_bn1')
        print("这里创建了判别器的第一个BN层实例:",self.d_bn1)
        self.d_bn2 = BatchNorm(name='d_bn2')
        print("这里创建了判别器的第二个BN层实例:", self.d_bn2)

        "如果y_dim是None，则执行这条语句，判别器有第三个BN层"
        if not self.y_dim:
            self.d_bn3 = BatchNorm(name='d_bn3')
            print("这里创建了判别器的第三个BN层实例:", self.d_bn3)
        # 生成器的BN层
        self.g_bn0 = BatchNorm(name='g_bn0')
        print("这里创建了生成器的第0个BN层实例:", self.g_bn0)
        self.g_bn1 = BatchNorm(name='g_bn1')
        print("这里创建了生成器的第1个BN层实例:", self.g_bn1)
        self.g_bn2 = BatchNorm(name='g_bn2')
        print("这里创建了生成器的第2个BN层实例:", self.g_bn2)

        "如果y_dim是None，则执行这条语句，生成器有第三个BN层"
        if not self.y_dim:
            self.g_bn3 = BatchNorm(name='g_bn3')
            print("这里创建了生成器的第3个BN层实例:", self.g_bn3)

        # 数据集的名字
        self.dataset_name = dataset_name
        print("数据集为:", self.dataset_name)
        self.input_fname_pattern = input_fname_pattern
        self.checkpoint_dir = checkpoint_dir
        # 数据集的位置
        self.data_dir = data_dir
        print("数据集所在目录为:", self.data_dir)

        # 判断数据集的名字是否是mnist，如果不是，需要从本地文件夹中加载数据
        data_path = os.path.join(self.data_dir, self.dataset_name, self.input_fname_pattern)
        print("数据路径为:", data_path, "类型为:", type(data_path))
        # glob返回的是一个列表，self.data是一个列表
        self.data = glob(data_path)
        print("glob()之后的长度为:", self.data.__len__(), "类型为:", type(self.data))
        if len(self.data) == 0:
            raise Exception("[!] No data found in '" + data_path + "'")

        # 随机打乱数据集
        np.random.shuffle(self.data)
        "self.data列表中保存的是每一张照片的路径"
        "./data/6400/3966.jpg"
        # imreading 是一个numpy数组，shape[504, 800, 3]
        print("self.data[0]:", self.data[0])
        imreadImg = imread(self.data[0])
        print("读取图片的返回结果是:", type(imreadImg))

        # 如果是彩色图片
        if len(imreadImg.shape) >= 3:  # check if image is a non-grayscale image by checking channel number
            # c_dim代表RGB的通道数
            # self.c_dim = 3
            self.c_dim = imread(self.data[0]).shape[-1]
            print("图片的channel为:", self.c_dim)
        else:
            # 否侧的话就是单通道的
            self.c_dim = 1

        # 这一步是判断所有的数据是不是比一个batch_size的大，否则抛出异常
        if len(self.data) < self.batch_size:
            raise Exception("[!] Entire dataset size is less than the configured batch_size")
        # 灰度值为False
        self.grayscale = (self.c_dim == 1)
        print("灰度值为:", self.grayscale)
        # 构建模型函数，在初始化里面就完成了
        self.build_model()

    def build_model(self):
        print("开始构建模型")
        "首先判断y_dim，然后用tf.placeholder占位符定义并初始化y。"
        "y是标签类别数,self.y_dim = None"
        if self.y_dim:
            self.y = tf.placeholder(tf.float32, [self.batch_size, self.y_dim], name='y')
        else:
            "执行这条语句，self.y = None"
            self.y = None
        # 判断是否进行裁剪，如果是，图片的维度为输出高度，输出宽度，通道
        # 进行裁剪，输入和输出的大小是不一样的
        print("self.y_dim=", self.y_dim)
        "先不裁剪"
        if self.crop:
            image_dims = [self.output_height, self.output_width, self.c_dim]
            print("裁剪, 维度为:", image_dims)
        else:
            "不进行裁剪，图片的维度就是输入图片的维度"
            # [504, 800, 3]
            image_dims = [self.input_height, self.input_width, self.c_dim]
            print("不裁剪, 维度为:", image_dims)
        # [100, 158, 3]
        print("裁剪之后，图片的维度为：", image_dims)
        # 利用tf.placeholder定义inputs，是真实数据的向量，维度是四维，第一个维度是batch_size
        self.inputs = tf.placeholder(
            tf.float32, [self.batch_size] + image_dims, name='real_images')
        # [32, 100, 158, 3]
        print("输入图片的占位符的维度:", self.inputs.get_shape().as_list())
        "这里定义了图片的输入"
        # [64, 504, 800, 3]
        inputs = self.inputs

        # 定义并初始化生成器用到的噪音z，z_sum
        # z_dim就是生成器的输入噪声的列数，行数现在还不确定
        "z_dim->[None, 100]"
        print("self.z是噪声输入")
        self.z = tf.placeholder(
            dtype=tf.float32, shape=[None, self.z_dim], name='z')
        print("self.z 的维度：", self.z.get_shape().as_list())
        self.z_sum = histogram_summary("z", self.z)

        "self.G-->[64, 504, 800, 3]"
        "self.G 也相当于是图片，只不过是生成的图片"
        self.G = self.generator(self.z, self.y)
        print("得到了生成器的输出", self.G,"维度是", self.G.get_shape().as_list())

        "self.D是通过sigmoid的值，self.D_logits是没有通过激活函数的值"
        "self.D-->sigmoid [batch, 1],"
        self.D, self.D_logits = self.discriminator(inputs, self.y, reuse=False)
        print("真实图片进入判别器，判别器的输出self.D为经过sigmoid的", self.D.get_shape().as_list(),)
        print("self.D_logits为不经过sigmoid的", self.D_logits.get_shape().as_list())

        # sampler与generator类似，只是BN层不train
        print("传给sampler()函数的也是噪声的输入")
        print("self.sampler是sampler函数的输出")
        self.sampler = self.sampler(self.z, self.y)

        "这里将生成器生成的图片self.G 传给了判别器"
        "D_是fake的结果,self.D_-->[batch, 1]"
        print("将生成器的输出", self.G.get_shape().as_list(),"传给判别器")
        self.D_, self.D_logits_ = self.discriminator(self.G, self.y, reuse=True)
        print("虚假图片进入判别器，判别器的输出self.D_为经过sigmoid的", self.D_.get_shape().as_list(), )
        print("self.D_logits_为不经过sigmoid的", self.D_logits_.get_shape().as_list())

        self.d_sum = histogram_summary("d", self.D)
        self.d__sum = histogram_summary("d_", self.D_)
        self.G_sum = image_summary("G", self.G)

        def sigmoid_cross_entropy_with_logits(x, y):
            try:
                return tf.nn.sigmoid_cross_entropy_with_logits(logits=x, labels=y)
            except:
                return tf.nn.sigmoid_cross_entropy_with_logits(logits=x, targets=y)

        "真实图片，判别器的输出与1的比较"
        "判别器的真实损失"
        print("定义判别器的真实损失，真实图片输入判别器的输出为", self.D_logits,"将其余全一比较，得到损失")
        self.d_loss_real = tf.reduce_mean(
            sigmoid_cross_entropy_with_logits(self.D_logits, tf.ones_like(self.D)))
        "生成器生成的图片，判别器的判别与0的比较"
        "判别器的虚假损失"
        print("定义判别器的虚假损失，虚假图片输入判别器的输出为", self.D_logits_, "将其余全零比较，得到损失")
        self.d_loss_fake = tf.reduce_mean(
            sigmoid_cross_entropy_with_logits(self.D_logits_, tf.zeros_like(self.D_)))

        print("定义生成器的损失，将虚假图片输入判别器得到的输出为", self.D_logits_, "将其余全一比较，得到损失")
        self.g_loss = tf.reduce_mean(
            sigmoid_cross_entropy_with_logits(self.D_logits_, tf.ones_like(self.D_)))

        self.d_loss_real_sum = scalar_summary("d_loss_real", self.d_loss_real)
        self.d_loss_fake_sum = scalar_summary("d_loss_fake", self.d_loss_fake)

        self.d_loss = self.d_loss_real + self.d_loss_fake

        self.g_loss_sum = scalar_summary("g_loss", self.g_loss)
        self.d_loss_sum = scalar_summary("d_loss", self.d_loss)

        t_vars = tf.trainable_variables()
        print("t_vars", type(t_vars),"长度为", t_vars.__len__())

        self.d_vars = [var for var in t_vars if 'd_' in var.name]
        self.g_vars = [var for var in t_vars if 'g_' in var.name]

        self.saver = tf.train.Saver()
        print("至此，构建模型完成")


    def train(self, config):
        print("-.-" * 10)
        print("进行训练")
        print("定义优化器")
        d_optim = tf.train.AdamOptimizer(config.learning_rate, beta1=config.beta1) \
            .minimize(self.d_loss, var_list=self.d_vars)
        g_optim = tf.train.AdamOptimizer(config.learning_rate, beta1=config.beta1) \
            .minimize(self.g_loss, var_list=self.g_vars)
        try:
            print("运行初始化，global_init")
            tf.global_variables_initializer().run()
        except:
            print("运行初始化，init_all")
            tf.initialize_all_variables().run()

        self.g_sum = merge_summary([self.z_sum, self.d__sum,
                                    self.G_sum, self.d_loss_fake_sum, self.g_loss_sum])
        self.d_sum = merge_summary(
            [self.z_sum, self.d_sum, self.d_loss_real_sum, self.d_loss_sum])
        "写日志"
        self.writer = SummaryWriter("./logs", self.sess.graph)

        print("准备样本噪声输入, sample_z")
        sample_z = np.random.uniform(-1, 1, size=(self.sample_num, self.z_dim))
        print("样本噪声输入维度", sample_z.shape)   #[32, 100]

        # 取出来了32个的样本
        sample_files = self.data[0:self.sample_num]
        # sample_files保存的是32个样本图片的路径
        print("sample_files", type(sample_files), "长度为", sample_files.__len__())   #32
        # print("sample_files[0]", sample_files[0])
        "get_image()函数返回的是每一张照片的numpy数组形式"
        print("原照片的维度为", cv2.imread(self.data[0]).shape) #[504, 800, 3]

        # TODO:读取照片的函数有问题
        sample = [
            get_image(sample_file,
                      input_height=self.input_height,
                      input_width=self.input_width,
                      resize_height=self.output_height,
                      resize_width=self.output_width,
                      crop=self.crop,
                      grayscale=self.grayscale) for sample_file in sample_files]
        print("sample中的元素是", type(sample[0]))  #ndarray
        print("sample", type(sample), "长度是", sample.__len__())   # 32
        if (self.grayscale):
            sample_inputs = np.array(sample).astype(np.float32)[:, :, :, None]
        else:
            sample_inputs = np.array(sample).astype(np.float32)

        print("sample_inputs-->", sample_inputs.shape)

        counter = 1
        start_time = time.time()
        could_load, checkpoint_counter = self.load(self.checkpoint_dir)
        if could_load:
            counter = checkpoint_counter
            print(" [*] Load SUCCESS")
        else:
            print(" [!] Load failed...")

        for epoch in range(config.epoch):
            print("-.-" * 10)
            print("开始epoch")
            self.data = glob(os.path.join(
                config.data_dir, config.dataset, self.input_fname_pattern))
            print("self.data",type(self.data),"长度为", self.data.__len__())  #10000
            print("随机打乱图片")
            np.random.shuffle(self.data)
            "batch的index"
            print("len(self.data)", len(self.data))   #10000
            # 有多少个batch
            batch_idxs = min(len(self.data), config.train_size) // config.batch_size
            print("batch_idx=", batch_idxs)   # 312

            for idx in range(0, int(batch_idxs)):

                "图片的批处理"
                "取出来一个批次的图片"
                # print("-.-" * 10)
                # print("开始第一个batch的训练")
                "下一批batch取出来的就是不同的图片"
                batch_files = self.data[idx * config.batch_size:(idx + 1) * config.batch_size]
                # 一个batch_files有32张图片
                # print("batch_files", batch_files.__len__())  #32
                # 一个32的列表，每一个元素是每一张图片的路径，str
                # print("batch_files", batch_files)
                "get_image输入的是图片路径"
                # batch_file是每一张图片的路径，为str
                batch = [
                    get_image(batch_file,
                              input_height=self.input_height,
                              input_width=self.input_width,
                              resize_height=self.output_height,
                              resize_width=self.output_width,
                              crop=self.crop,
                              grayscale=self.grayscale) for batch_file in batch_files]
                # batch列表中有32个元素，每个元素是每一张图片的numpy数组
                # batch是个列表，每个元素是每张图片的numpy数组,维度是[100, 158, 3]
                # print("batch", type(batch), "batch[0]", type(batch[0]), "batch[0] shape", batch[0].shape)
                if self.grayscale:
                    batch_images = np.array(batch).astype(np.float32)[:, :, :, None]
                    # print("灰度，batch_images的维度", batch_images.shape)
                else:
                    "batch_images 是判别器的输入"
                    batch_images = np.array(batch).astype(np.float32)
                    # print("RGB，batch_images的维度", batch_images.shape)

                # batch_images-->numpy [32, 100, 158, 3]
                # batch_images.shape[32, 100, 158, 3]  batch_images[0] shape[100, 158, 3]
                # print("batch_images", batch_images.shape,"batch_images[0] shape", batch_images[0].shape)
                # np.random.uniform(low = 0.0, high = 1.0, size = None)
                "噪声输入的批处理"
                "batch_z 是生成器的输入"
                "下一批batch 就是不同的噪声输入"
                batch_z = np.random.uniform(-1, 1, [config.batch_size, self.z_dim]) \
                    .astype(np.float32)
                # [32, 100]
                # print("batch_z", batch_z.shape)

                # Update D network
                "这里完成了数据的输入"
                # print("更新判别器网络")
                # print("self.inputs", self.inputs.get_shape().as_list()) # [32, 100, 158, 3]
                "喂数据的时候，判别网络需要喂入真实图片以及噪声输入"
                "判别器输入batch_images 和 batch_z"
                _, summary_str = self.sess.run([d_optim, self.d_sum],
                                               feed_dict={self.inputs: batch_images, self.z: batch_z})
                self.writer.add_summary(summary_str, counter)

                # Update G network
                "更新生成器网络的时候，喂入噪声输入"
                _, summary_str = self.sess.run([g_optim, self.g_sum],
                                               feed_dict={self.z: batch_z})
                self.writer.add_summary(summary_str, counter)

                "这里更新了两次生成器"
                "喂给生成器的是batch_z"
                _, summary_str = self.sess.run([g_optim, self.g_sum],
                                               feed_dict={self.z: batch_z})
                self.writer.add_summary(summary_str, counter)

                # Tensor.eval(feed_dict={})  启动计算的另一种方式
                errD_fake = self.d_loss_fake.eval(feed_dict={self.z: batch_z})
                # errD_fake = self.sess.run(self.d_loss_fake, feed_dict={self.z:batch_z})
                errD_real = self.d_loss_real.eval(feed_dict={self.inputs: batch_images})
                errG = self.g_loss.eval(feed_dict={self.z: batch_z})

                counter += 1
                print("Epoch: [%2d/%2d] [%4d/%4d] time: %4.4f, d_loss: %.8f, g_loss: %.8f" \
                      % (epoch, config.epoch, idx, batch_idxs,
                         time.time() - start_time, errD_fake + errD_real, errG))

                if np.mod(counter, 100) == 1:
                    try:
                        print("-.-" * 10)
                        print("每100个batch 运行sample函数")
                        samples, d_loss, g_loss = self.sess.run(
                            [self.sampler, self.d_loss, self.g_loss],
                            feed_dict={
                                self.z: sample_z,
                                self.inputs: sample_inputs,
                            },
                        )
                        print("运行成功")
                        # samples是个numpy数组 [32, 100, 158, 3]
                        print("samples", type(samples),"维度是", samples.shape)
                        print("samples.shape[0]", samples.shape[0])  #32
                        # print("samples[0]", samples[0])
                        # a = samples[0]
                        # np.save("./samples/samples[0].npy", a)
                        # 将一个batch的图片存成一整张正方形的图片
                        save_images(samples, image_manifold_size(samples.shape[0]),
                                    './{}/train_{:02d}_{:04d}.png'.format(config.sample_dir, epoch, idx))
                        print("[Sample] d_loss: %.8f, g_loss: %.8f" % (d_loss, g_loss))
                    except:
                        print("one pic error!...")

                if np.mod(counter, 500) == 2:
                    self.save(config.checkpoint_dir, counter)


    def discriminator(self, image, y=None, reuse=False):
        print("接下来进入判别器")
        print("判别器的输入为", image, "维度是", image.get_shape().as_list())
        # image是真实图片
        with tf.variable_scope("discriminator") as scope:
            if reuse:
                scope.reuse_variables()

            "标签数为None，self.y_dim = None,执行下面这条语句"
            if not self.y_dim:
                print("self.y_sim = None")
                # df_dim  = 64
                # self.df_dim指的是卷积核的个数
                "image-->[64, 504, 800, 3]"
                "h0-->[64, 252, 400, 64]"
                h0 = lrelu(conv2d(image, self.df_dim, name='d_h0_conv'))
                print("h0-->", h0.get_shape().as_list())
                "h1-->[64, 126, 200, 128]"
                h1 = lrelu(self.d_bn1(conv2d(h0, self.df_dim * 2, name='d_h1_conv')))
                print("h1-->", h1.get_shape().as_list())
                "h2-->[64, 63, 100, 256]"
                h2 = lrelu(self.d_bn2(conv2d(h1, self.df_dim * 4, name='d_h2_conv')))
                print("h2-->", h2.get_shape().as_list())
                "h3-->[64, 32, 50, 512]"
                h3 = lrelu(self.d_bn3(conv2d(h2, self.df_dim * 8, name='d_h3_conv')))
                print("h3-->", h3.get_shape().as_list())
                "h4-->[64, 1]"
                h4 = linear(input_=tf.reshape(h3, [self.batch_size, -1]), output_size=1, scope='d_h4_lin')
                print("h4-->", h4.get_shape().as_list())
                "判别器最终的输出是一个值"
                return tf.nn.sigmoid(h4), h4
            else:
                yb = tf.reshape(y, [self.batch_size, 1, 1, self.y_dim])
                x = conv_cond_concat(image, yb)

                h0 = lrelu(conv2d(x, self.c_dim + self.y_dim, name='d_h0_conv'))
                h0 = conv_cond_concat(h0, yb)

                h1 = lrelu(self.d_bn1(conv2d(h0, self.df_dim + self.y_dim, name='d_h1_conv')))
                h1 = tf.reshape(h1, [self.batch_size, -1])
                h1 = concat([h1, y], 1)

                h2 = lrelu(self.d_bn2(linear(h1, self.dfc_dim, 'd_h2_lin')))
                h2 = concat([h2, y], 1)

                h3 = linear(h2, 1, 'd_h3_lin')

                return tf.nn.sigmoid(h3), h3


    def generator(self, z, y=None):
        print("进入生成器")
        print("生成器的输入为", z, "维度为",z.get_shape().as_list())
        with tf.variable_scope("generator") as scope:

            "如果y_dim为None，执行下面这条语句"
            if not self.y_dim:
                print("self.y_dim = None")
                s_h, s_w = self.output_height, self.output_width
                print("s_h=", s_h, "s_w=", s_w)
                s_h2, s_w2 = conv_out_size_same(s_h, 2), conv_out_size_same(s_w, 2)
                print("s_h2=", s_h2, "s_w2=", s_w2)
                s_h4, s_w4 = conv_out_size_same(s_h2, 2), conv_out_size_same(s_w2, 2)
                print("s_h4=", s_h4, "s_w4=", s_w4)
                s_h8, s_w8 = conv_out_size_same(s_h4, 2), conv_out_size_same(s_w4, 2)
                print("s_h8=", s_h8, "s_w8=", s_w8)
                s_h16, s_w16 = conv_out_size_same(s_h8, 2), conv_out_size_same(s_w8, 2)
                print("s_h16=", s_h16, "s_w16=", s_w16)

                # project `z` and reshape
                "z_=[None, 35840]"
                self.z_, self.h0_w, self.h0_b = linear(
                    z, self.gf_dim * 8 * s_h16 * s_w16, 'g_h0_lin', with_w=True)
                print("线性运算之后的结果:",self.z_.get_shape().as_list(), "矩阵:",
                      self.h0_w.get_shape().as_list(),"偏置:", self.h0_b.get_shape().as_list())
                "self.h0-->[None, 7, 10, 512]"
                self.h0 = tf.reshape(
                    self.z_, [-1, s_h16, s_w16, self.gf_dim * 8])
                print("reshape之后维度为:", self.h0.get_shape().as_list())
                "linear-->reshape-->BN-->relu-->h0"
                "注意，生成器的BN层是需要训练的"
                "h0-->reshape=[None, 32, 50, 512]"
                h0 = tf.nn.relu(self.g_bn0(self.h0))

                print("接下来生成器进行转置卷积")

                self.h1, self.h1_w, self.h1_b = deconv2d(
                    input_=h0, output_shape=[self.batch_size, s_h8, s_w8, self.gf_dim * 4], name='g_h1', with_w=True)
                print("self.h1-->", self.h1.get_shape().as_list())
                "h1-->[64, 63, 100, 256]"
                h1 = tf.nn.relu(self.g_bn1(self.h1))

                "h2-->[64, 126, 200, 128]"
                h2, self.h2_w, self.h2_b = deconv2d(
                    h1, [self.batch_size, s_h4, s_w4, self.gf_dim * 2], name='g_h2', with_w=True)
                print("h2-->", h2.get_shape().as_list())
                h2 = tf.nn.relu(self.g_bn2(h2))

                "h3-->[64, 252, 400, 64]"
                h3, self.h3_w, self.h3_b = deconv2d(
                    h2, [self.batch_size, s_h2, s_w2, self.gf_dim * 1], name='g_h3', with_w=True)
                print("h3-->", h3.get_shape().as_list())
                h3 = tf.nn.relu(self.g_bn3(h3))

                "h4-->[64, 504, 800, 3]"
                h4, self.h4_w, self.h4_b = deconv2d(
                    h3, [self.batch_size, s_h, s_w, self.c_dim], name='g_h4', with_w=True)
                print("h4-->", h4.get_shape().as_list())

                "最后再通过一次激活函数Tanh"
                print("最后再通过一次Tanh")
                return tf.nn.tanh(h4)
            else:
                s_h, s_w = self.output_height, self.output_width
                s_h2, s_h4 = int(s_h / 2), int(s_h / 4)
                s_w2, s_w4 = int(s_w / 2), int(s_w / 4)

                # yb = tf.expand_dims(tf.expand_dims(y, 1),2)
                yb = tf.reshape(y, [self.batch_size, 1, 1, self.y_dim])
                z = concat([z, y], 1)

                h0 = tf.nn.relu(
                    self.g_bn0(linear(z, self.gfc_dim, 'g_h0_lin')))
                h0 = concat([h0, y], 1)

                h1 = tf.nn.relu(self.g_bn1(
                    linear(h0, self.gf_dim * 2 * s_h4 * s_w4, 'g_h1_lin')))
                h1 = tf.reshape(h1, [self.batch_size, s_h4, s_w4, self.gf_dim * 2])

                h1 = conv_cond_concat(h1, yb)

                h2 = tf.nn.relu(self.g_bn2(deconv2d(h1,
                                                    [self.batch_size, s_h2, s_w2, self.gf_dim * 2], name='g_h2')))
                h2 = conv_cond_concat(h2, yb)

                return tf.nn.sigmoid(
                    deconv2d(h2, [self.batch_size, s_h, s_w, self.c_dim], name='g_h3'))


    def sampler(self, z, y=None):
        print("进入sampler函数")
        with tf.variable_scope("generator") as scope:
            scope.reuse_variables()

            if not self.y_dim:
                s_h, s_w = self.output_height, self.output_width
                print("s_h=", s_h, "s_w=", s_w)
                s_h2, s_w2 = conv_out_size_same(s_h, 2), conv_out_size_same(s_w, 2)
                print("s_h2=", s_h2, "s_w2=", s_w2)
                s_h4, s_w4 = conv_out_size_same(s_h2, 2), conv_out_size_same(s_w2, 2)
                print("s_h4=", s_h4, "s_w4=", s_w4)
                s_h8, s_w8 = conv_out_size_same(s_h4, 2), conv_out_size_same(s_w4, 2)
                print("s_h8=", s_h8, "s_w8=", s_w8)
                s_h16, s_w16 = conv_out_size_same(s_h8, 2), conv_out_size_same(s_w8, 2)
                print("s_h16=", s_h16, "s_w16=", s_w16)

                h0 = tf.reshape(
                    linear(z, self.gf_dim * 8 * s_h16 * s_w16, 'g_h0_lin'),
                    [-1, s_h16, s_w16, self.gf_dim * 8])
                print("sampler函数中,h0-->", h0.get_shape().as_list())
                "linear-->reshape-->BN-->relu-->h0"
                "与生成器不同的是，sampler中的BN层是不训练的"
                h0 = tf.nn.relu(self.g_bn0(h0, train=False))

                "h1-->[64, 63, 100, 256]"
                h1 = deconv2d(h0, [self.batch_size, s_h8, s_w8, self.gf_dim * 4], name='g_h1')
                print("sampler函数中,h1-->", h1.get_shape().as_list())
                h1 = tf.nn.relu(self.g_bn1(h1, train=False))

                "h2-->[64, 126, 200, 128]"
                h2 = deconv2d(h1, [self.batch_size, s_h4, s_w4, self.gf_dim * 2], name='g_h2')
                print("sampler函数中,h2-->", h2.get_shape().as_list())
                h2 = tf.nn.relu(self.g_bn2(h2, train=False))

                "h3-->[64, 252, 400, 64]"
                h3 = deconv2d(h2, [self.batch_size, s_h2, s_w2, self.gf_dim * 1], name='g_h3')
                print("sampler函数中,h3-->", h3.get_shape().as_list())
                h3 = tf.nn.relu(self.g_bn3(h3, train=False))

                "h4-->[64, 504, 800, 3]"
                h4 = deconv2d(h3, [self.batch_size, s_h, s_w, self.c_dim], name='g_h4')
                print("sampler函数中,h4-->", h4.get_shape().as_list())

                print("sampler函数，最后再通过Tanh")
                return tf.nn.tanh(h4)
            else:
                s_h, s_w = self.output_height, self.output_width
                s_h2, s_h4 = int(s_h / 2), int(s_h / 4)
                s_w2, s_w4 = int(s_w / 2), int(s_w / 4)

                # yb = tf.reshape(y, [-1, 1, 1, self.y_dim])
                yb = tf.reshape(y, [self.batch_size, 1, 1, self.y_dim])
                z = concat([z, y], 1)

                h0 = tf.nn.relu(self.g_bn0(linear(z, self.gfc_dim, 'g_h0_lin'), train=False))
                h0 = concat([h0, y], 1)

                h1 = tf.nn.relu(self.g_bn1(
                    linear(h0, self.gf_dim * 2 * s_h4 * s_w4, 'g_h1_lin'), train=False))
                h1 = tf.reshape(h1, [self.batch_size, s_h4, s_w4, self.gf_dim * 2])
                h1 = conv_cond_concat(h1, yb)

                h2 = tf.nn.relu(self.g_bn2(
                    deconv2d(h1, [self.batch_size, s_h2, s_w2, self.gf_dim * 2], name='g_h2'), train=False))
                h2 = conv_cond_concat(h2, yb)

                return tf.nn.sigmoid(deconv2d(h2, [self.batch_size, s_h, s_w, self.c_dim], name='g_h3'))


    @property
    def model_dir(self):
        return "{}_{}_{}_{}".format(
            self.dataset_name, self.batch_size,
            self.output_height, self.output_width)


    def save(self, checkpoint_dir, step):
        model_name = "DCGAN.model"
        checkpoint_dir = os.path.join(checkpoint_dir, self.model_dir)

        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)

        self.saver.save(self.sess,
                        os.path.join(checkpoint_dir, model_name),
                        global_step=step)

    def load(self, checkpoint_dir):
        import re
        print(" [*] Reading checkpoints...")
        checkpoint_dir = os.path.join(checkpoint_dir, self.model_dir)

        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)
        if ckpt and ckpt.model_checkpoint_path:
            ckpt_name = os.path.basename(ckpt.model_checkpoint_path)
            self.saver.restore(self.sess, os.path.join(checkpoint_dir, ckpt_name))
            counter = int(next(re.finditer("(\d+)(?!.*\d)", ckpt_name)).group(0))
            print(" [*] Success to read {}".format(ckpt_name))
            return True, counter
        else:
            print(" [*] Failed to find a checkpoint")
            return False, 0

```  
- [x] 这部分代码是最关键的，定义了模型以及训练的部分，生成器和判别器的定义，以及用于显示验证的sampler函数。需要仔细体会。  
****
通过这份代码，可以实现基本的**DCGAN**的操作。




