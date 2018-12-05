import tensorflow as tf
import Network
from Read_From_TFRecords_test import test_iterator
from Read_From_TFRecords_test import test_data_batch
from Read_From_TFRecords_test import test_label_batch
import time
import pandas as pd
import matplotlib.pyplot as plt


log_dir = 'E:/logs'
"""测试时不关注正则化损失的值，将用于计算正则化损失的函数设置为None"""
logits = Network.inference(input_tensor=test_data_batch, train=False, regularizer=None)
test_loss = tf.reduce_mean(tf.square(logits - test_label_batch))
saver = tf.train.Saver()
test_loss_vec = []

while True:
    with tf.Session() as sess:

        """生成器的初始化是一定要的"""
        sess.run(test_iterator.initializer)
        print("Reading checkpoints...")
        ckpt = tf.train.get_checkpoint_state(log_dir)

        if ckpt and ckpt.model_checkpoint_path:
            """加载模型"""
            saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)

            """通过文件名得到模型保存时迭代的轮数，取出来的是个str"""
            global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
            print("Loading success, global step is %s" % global_step)
            loss = sess.run(test_loss)
            test_loss_vec.append(loss)
            print("Test loss is %.6f" % loss)
            test = pd.Series(data=test_loss_vec)
            test.to_csv('E:/test.csv', mode='w')
            if global_step == '20000':
                plt.plot(test_loss_vec,'r-',linewidth=2, label='test loss')
                plt.xlabel('Generation')
                plt.ylabel('Test loss')
                plt.legend(loc='upper right')
                plt.show()

        else:
            print("No checkpoint file is found")

    """程序每隔10秒运行一次，每次运行都是读取最新保存的模型"""
    time.sleep(30)
