"main.py主要是调用前面定义好的模型、图像处理方法，来进行训练测试，程序的入口"
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
