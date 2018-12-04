import tensorflow as tf
import Network
from Read_From_TFRecords_test import iterator
from Read_From_TFRecords_test import next_element
import time


MOVING_AVERAGE_DECAY = 0.999
log_dir = 'E:/logs'
feature, labels = next_element
logits = Network.inference(input_tensor=feature, train=False, regularizer=None)
test_loss = tf.reduce_mean(tf.square(logits - labels))
# variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY)
# variables_to_restore = variable_averages.variables_to_restore()
saver = tf.train.Saver()


while True:
    with tf.Session() as sess:
        # sess.run(tf.global_variables_initializer())
        """生成器的初始化是一定要的"""
        sess.run(iterator.initializer)
        print("Reading checkpoints...")
        ckpt = tf.train.get_checkpoint_state(log_dir)

        # print(ckpt)
        # E:/logs\model.ckpt-31000
        # print(ckpt.model_checkpoint_path)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)

            """取出来的是个str"""
            global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
            print("Loading success, global step is %s" % global_step)
        else:
            print("No checkpoint file is found")
        loss = sess.run(test_loss)
        print("Test loss is %.2f" % loss)
    """程序每隔10秒运行一次，每次运行都是读取最新保存的模型"""
    time.sleep(30)
