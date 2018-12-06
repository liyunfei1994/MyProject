import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import Network
from Read_From_TFRecords_train import next_element
from Read_From_TFRecords_train import iterator
from Read_From_TFRecords_train import num_cases
from Read_From_TFRecords_train import batch_size


start_time = time.time()
"""总的样本数"""
NUM_EXAMPLES = num_cases * batch_size
BATCH_SIZE = batch_size
LEARNING_RATE_BASE = 0.9
LEARNING_RATE_DECAY = 0.98
MOVING_AVERAGE_DECAY = 0.999
# TRAINING_STEPS = 20
"""模型保存的路径和文件名"""
MODEL_SAVE_PATH = 'E:/logs'
MODEL_NAME = "model.ckpt"

"""正则化"""
# 正则化的权重
REGULARAZTION_RATE = 0.01
regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

global_step = tf.Variable(0, name="global_step", trainable=False)

"""滑动平均"""
with tf.name_scope("moving_average"):
    EMA = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variable_average_op = EMA.apply(tf.trainable_variables())

with tf.name_scope("input"):
    feature, label = next_element

"""前向传播的结果logits"""
logits = Network.inference(input_tensor=feature, train=True, regularizer=regularizer)

with tf.name_scope("loss_function"):
    """全连接层权重的正则化损失 + 网络前向传播的损失"""
    train_loss = Network.losses(logits=logits, labels=label) + tf.add_n(tf.get_collection('losses'))

"""指数衰减学习率"""
LEARNING_RATE = tf.train.exponential_decay(learning_rate=LEARNING_RATE_BASE,
                                           global_step=global_step,
                                           decay_steps=NUM_EXAMPLES/BATCH_SIZE,
                                           decay_rate=LEARNING_RATE_DECAY,
                                           staircase=True)

with tf.variable_scope('Optimizer') as scope:
    optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE)
    train_step = optimizer.minimize(train_loss, global_step=global_step)

    with tf.control_dependencies([train_step, variable_average_op]):
        # tf.no_op()表示执行完 train_step, variable_averages_op 操作之后什么都不做
        train_op = tf.no_op(name='train')


"""生成一种写日志的writer,将当前的TF计算图写入日志"""
train_writer = tf.summary.FileWriter(MODEL_SAVE_PATH, tf.get_default_graph())

# 声明tf.train.Saver类用于保存模型
saver = tf.train.Saver()

init_op = tf.global_variables_initializer()
coord = tf.train.Coordinator()

summary_op = tf.summary.merge_all()
loss_vec = []
with tf.Session() as sess:

    try:
        sess.run(init_op)
        """初始化迭代器"""
        sess.run(iterator.initializer)
        for i in np.arange(num_cases):
            _, loss_value, step = sess.run([train_op, train_loss, global_step])
            loss_vec.append(loss_value)
            if i % 50 == 0:
                print("After %d training steps, loss on training batch is %.5f" % (
                    step, loss_value
                ))
                """运行所有日志的生成操作"""
                summary_str = sess.run(summary_op)
                """将所有日志写入文件"""
                train_writer.add_summary(summary_str, i)
            if i % 1000 == 0:
                saver.save(sess=sess, save_path=os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                            global_step=global_step)

    except tf.errors.OutOfRangeError:
        print("DONE TRAINING.")

    finally:
        coord.request_stop()

train_writer.close()

"""画出损失曲线图"""
plt.plot(loss_vec, 'b-.', label='train loss', linewidth=2)
plt.xlim(0, 20000)
plt.ylim(-1, 20000)
plt.title('Loss per Generation')
x_ticks = np.arange(0, 20000, 3000)
y_ticks = np.arange(0, 20000, 3000)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.legend(loc='upper right')
plt.xlabel('Generation')
plt.ylabel('Loss')
plt.show()

end_time = time.time()
during_time = (end_time - start_time)/60
print("Total time is %.2f" % during_time)
"""95minutes"""
