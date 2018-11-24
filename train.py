import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime
import Network
from Read_From_TFRecords import next_element
from Read_From_TFRecords import iterator
from Read_From_TFRecords import num_cases
from Read_From_TFRecords import batch_size

"""总的样本数"""
NUM_EXAMPLES = num_cases * batch_size
BATCH_SIZE = batch_size
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.98
MOVING_AVERAGE_DECAY = 0.999
# TRAINING_STEPS = 20

global_step = tf.Variable(0, name="global_step", trainable=False)


with tf.name_scope("moving_average"):
    """滑动平均"""
    EMA = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # 在所有代表网络参数的变量上使用滑动平均
    variable_average_op = EMA.apply(tf.trainable_variables())

"""正则化"""
# 正则化的权重
REGULARAZTION_RATE = 0.001
regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

"""模型保存的路径和文件名"""
MODEL_SAVE_PATH = 'E:/logs'
MODEL_NAME = "model.ckpt"

feature, label = next_element

"""前向传播的结果logits"""
logits = Network.inference(feature, train=True, regularizer=regularizer)
# """logits--> Tensor("fully2/Add:0", shape=(?, 5528), dtype=float32)"""

with tf.name_scope("loss_function"):
    """全连接层权重的正则化损失 + 网络前向传播的损失"""
    train_loss = Network.losses(logits=logits, labels=label) + tf.add_n(tf.get_collection('losses'))

"""指数衰减学习率"""
LEARNING_RATE = tf.train.exponential_decay(learning_rate=LEARNING_RATE_BASE,
                                           global_step=global_step,
                                           decay_steps=NUM_EXAMPLES/BATCH_SIZE,
                                           decay_rate=LEARNING_RATE_DECAY,
                                           staircase=True)

train_step = Network.training(loss=train_loss, learning_rate=LEARNING_RATE)

with tf.control_dependencies([train_step, variable_average_op]):
    # tf.no_op()表示执行完 train_step, variable_averages_op 操作之后什么都不做
    train_op = tf.no_op(name='train')

loss_vec = []

summary_op = tf.summary.merge_all()

"""生成一种写日志的writer,将当前的TF计算图写入日志"""
train_writer = tf.summary.FileWriter(MODEL_SAVE_PATH, tf.get_default_graph())

# 声明tf.train.Saver类用于保存模型
saver = tf.train.Saver()

init_op = tf.global_variables_initializer()
coord = tf.train.Coordinator()

with tf.Session() as sess:

    try:
        sess.run(init_op)
        sess.run(iterator.initializer)
        for i in np.arange(num_cases):
            _, loss_value, step = sess.run([train_op, train_loss, global_step])
            if i % 10 == 0:
                print("After %d training steps, loss on training batch is %.5f" % (
                    i, loss_value
                ))
                summary_str = sess.run(summary_op)
                train_writer.add_summary(summary_str, i)
            if i % 5 == 0:
                saver.save(sess=sess, save_path=os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                   global_step=global_step)
            loss_vec.append(np.sqrt(loss_value))

    except tf.errors.OutOfRangeError:
        print("DONE TRAINING.")

    finally:
        plt.plot(np.arange(0, num_cases+1), loss_vec, 'k-', label="train loss")
        plt.title("LOSS PER Generation")
        plt.legend(loc="upper right")
        plt.xlabel("Generation")
        plt.ylabel("Loss")
        plt.show()

        coord.request_stop()
