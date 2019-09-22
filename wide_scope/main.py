import tensorflow as tf
import os
import numpy as np
from utils import show_all_variables
import time
import pandas as pd
import net
from train_read_from_tfrecords import batch_size
from train_read_from_tfrecords import train_next_element, train_iterator
from test_read_from_tfrecords import test_next_element, test_iterator


start_time = time.time()
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

LEARNING_RATE_BASE = 0.1
LEARNING_RATE_DECAY = 0.98
MOVING_AVERAGE_DECAY = 0.999

train_images_path = "./train_images"

NUM_EXAMPLES = len(next(os.walk(train_images_path))[2])
print("num_examples=", NUM_EXAMPLES)
TRAIN_STEPS = 75000

MODEL_SAVE_PATH = './logs'
MODEL_NAME = "model.ckpt"

if not os.path.exists(MODEL_SAVE_PATH):
    os.makedirs(MODEL_SAVE_PATH)


REGULARAZTION_RATE = 0.001
regularizer = tf.contrib.layers.l2_regularizer(REGULARAZTION_RATE)

global_step = tf.Variable(0, name="global_step", trainable=False)

with tf.name_scope("Train_Input_Data"):
    train_label, train_feature = train_next_element

with tf.name_scope("Test_Input_Data"):
    test_label, test_feature = test_next_element

# with tf.variable_scope("Logits") as scope:

train_logits = net.inference(
    input_tensor=train_feature,
    train=True,
    regularizer=regularizer)
    #
    # scope.reuse_variables()
    #
# test_logits = net.inference(
#     input_tensor=test_feature,
#     train=False,
#     regularizer=None)
"最关键的地方是这里，加载模型的时候，这里不可以写成train和test一起的形式，会出错！！！"
with tf.variable_scope("Train_Loss"):
    MSE = tf.reduce_mean(tf.square(train_logits-train_label))
    train_loss = MSE + tf.add_n(tf.get_collection('losses'))
    tf.summary.scalar("Train Loss", train_loss)

# with tf.variable_scope("Test_Loss"):
#     test_loss = tf.reduce_mean(tf.square(test_logits-test_label))
#     tf.summary.scalar("Test Loss", test_loss)

with tf.variable_scope('Optimizer') as scope:
    LEARNING_RATE = tf.train.exponential_decay(
        learning_rate=LEARNING_RATE_BASE,
        global_step=global_step,
        decay_steps=NUM_EXAMPLES / batch_size,
        decay_rate=LEARNING_RATE_DECAY,
        staircase=True)

    optimizer = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE)
    train_step = optimizer.minimize(train_loss, global_step=global_step)


train_writer = tf.summary.FileWriter(MODEL_SAVE_PATH, tf.get_default_graph())

saver = tf.train.Saver(max_to_keep=2)
coord = tf.train.Coordinator()
merged = tf.summary.merge_all()

run_config = tf.ConfigProto(allow_soft_placement=True)
run_config.gpu_options.allocator_type = 'BFC'
run_config.gpu_options.per_process_gpu_memory_fraction = 0.8
run_config.gpu_options.allow_growth = True

init_op = tf.global_variables_initializer()

train_loss_vec = []
test_loss_vec = []

with tf.Session(config=run_config) as sess:
    show_all_variables()

    sess.run(init_op)
    sess.run(train_iterator.initializer)
    sess.run(test_iterator.initializer)

    print("=" * 15)
    print("*" * 15)

    try:
        for i in np.arange(TRAIN_STEPS):

            _, train_loss_value, step = sess.run(
                [train_step, train_loss, global_step])
            # test_loss_value = sess.run(test_loss)

            if (i+1) % 100 == 0:
                print("After %d training steps, loss on training/testing batch is %.2f" % (
                    step, train_loss_value))

                summary_str = sess.run(merged)
                train_writer.add_summary(summary_str, i)

            if (i+1) % 1000 == 0:
                saver.save(
                    sess=sess,
                    save_path=os.path.join(MODEL_SAVE_PATH,MODEL_NAME),
                    global_step=global_step)

                train_loss_vec.append(train_loss_value)
                # test_loss_vec.append(test_loss_value)

    except tf.errors.OutOfRangeError:
        print("[!]Done!OutOFRange")

    finally:

        pd.Series(train_loss_vec).to_csv('./train_loss.csv', header=False)
        # pd.Series(test_loss_vec).to_csv('./test_loss.csv', header=False)
        coord.request_stop()

train_writer.close()

end_time = time.time()
during_time = (end_time - start_time) / 3600
print("Total time is %.2f hours" % during_time)
