import tensorflow as tf
import Network
import numpy as np
import time
import pandas as pd
import os
from test_read_from_tfrecords import test_iterator, test_next_element


MODEL_SAVE_PATH = './logs'

os.environ["CUDA_VISIBLE_DEVICES"] = "3"

features_batch = test_next_element[1]
images_batch = test_next_element[0]

test_step = 40000

"""测试时不关注正则化损失的值，将用于计算正则化损失的函数设置为None"""
logits = Network.inference(
    input_tensor=features_batch,
    train=False,
    regularizer=None)

test_loss = tf.reduce_mean(tf.square(logits - images_batch))

saver = tf.train.Saver()

test_loss_vec = []
test_global_step = []


with tf.Session() as sess:

    """生成器的初始化是一定要的"""
    sess.run(test_iterator.initializer)
    print("Reading checkpoints...")
    ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)

    if ckpt and ckpt.model_checkpoint_path:
        """加载模型"""
        saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)
        "global是个字符串"
        global_step = ckpt.model_checkpoint_path.split(
            '/')[-1].split('-')[-1]
        test_loss_value = sess.run(test_loss)
        test_loss_vec.append(test_loss_value)
        test_global_step.append(int(global_step))
        print(
            "After %s testing steps, loss on test batch is %.2f" %
            (global_step, test_loss_value))

        if int(global_step) == 33001:
            pd.Series(test_loss_vec).to_csv('./test_loss.csv')
            pd.Series(test_global_step).to_csv('./test_global_step.csv')
    else:
        print("No checkpoint file is found")

