import tensorflow as tf
import os
import numpy as np
from utils_CNN import show_all_variables
import time
import Network
import math
from read_from_tfrecords import batch_size, num_epochs
from read_from_tfrecords import next_element, iterator

start_time = time.time()
os.environ["CUDA_VISIBLE_DEVICES"] = "1,3"

LEARNING_RATE_BASE = 0.9
LEARNING_RATE_DECAY = 0.98
MOVING_AVERAGE_DECAY = 0.999

"""总的样本数"""
NUM_EXAMPLES = 17497
TRAIN_STEPS = 300000

"""模型保存的路径和文件名"""
MODEL_SAVE_PATH = './logs'
MODEL_NAME = "model.ckpt"
if not os.path.exists(MODEL_SAVE_PATH):
    os.makedirs(MODEL_SAVE_PATH)


"""正则化"""
# 正则化的权重
REGULARAZTION_RATE = 0.01
regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

global_step = tf.Variable(0, name="global_step", trainable=False)

"""滑动平均"""
with tf.name_scope("Moving_Average"):
    EMA = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variable_average_op = EMA.apply(tf.trainable_variables())

with tf.name_scope("Input"):
    "images_batch的数据类型一定得是uint8"
    images_batch, features_batch = next_element

logits = Network.inference(input_tensor= features_batch, train=True, regularizer=regularizer)

with tf.variable_scope("Loss"):
    RMSE = tf.reduce_mean(tf.square(logits - images_batch))
    train_loss = RMSE + tf.add_n(tf.get_collection('losses'))
    tf.summary.scalar("Train Loss", train_loss)


with tf.variable_scope('Optimizer') as scope:
    """指数衰减学习率"""
    LEARNING_RATE = tf.train.exponential_decay(learning_rate=LEARNING_RATE_BASE,
                                               global_step=global_step,
                                               decay_steps=NUM_EXAMPLES * num_epochs / batch_size,
                                               decay_rate=LEARNING_RATE_DECAY,
                                               staircase=True)
    # LEARNING_RATE = 0.002
    optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE)
    train_step = optimizer.minimize(train_loss, global_step=global_step)

    with tf.control_dependencies([train_step, variable_average_op]):
        # tf.no_op()表示执行完 train_step, variable_averages_op 操作之后什么都不做
        train_op = tf.no_op(name='train')


"""生成一种写日志的writer,将当前的TF计算图写入日志"""
train_writer = tf.summary.FileWriter(MODEL_SAVE_PATH, tf.get_default_graph())

# 声明tf.train.Saver类用于保存模型
saver = tf.train.Saver()
coord = tf.train.Coordinator()
merged = tf.summary.merge_all()

run_config = tf.ConfigProto(allow_soft_placement=True)
run_config.gpu_options.allocator_type='BFC'
run_config.gpu_options.per_process_gpu_memory_fraction=0.90
run_config.gpu_options.allow_growth=True

init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    try:
        show_all_variables()

        sess.run(init_op)
        sess.run(iterator.initializer)
        print("=" * 15)
        print("*" * 15)
        for i in np.arange(TRAIN_STEPS):

            _, train_loss_value,step = sess.run([train_op, train_loss,  global_step])

            if i % 50 == 0:
                print("After %d training steps, loss on training batch is %.2f" % (
                    step, train_loss_value
                ))
                """运行所有日志的生成操作"""
                summary_str = sess.run(merged)
                """将所有日志写入文件"""
                train_writer.add_summary(summary_str, i)
            if i % 1000 == 0:
                saver.save(sess=sess, save_path=os.path.join(MODEL_SAVE_PATH, MODEL_NAME),
                            global_step=global_step)
    except tf.errors.OutOfRangeError:
        print("[!] OutOfRange, Done Training!")
    except tf.errors.ResourceExhaustedError:
        print("[!] ResourceExhaustedError")

    finally:
        coord.request_stop()


train_writer.close()


end_time = time.time()
during_time = (end_time - start_time)/60
print("Total time is %.2f minutes" % during_time)
