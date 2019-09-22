"将训练集的压力数据导出网络预测的图片"

import tensorflow as tf
import net
import os
from train_run_image_tfrecords import train_iterator, train_next_element, batch_size
import scipy.misc


MODEL_SAVE_PATH = './logs'
train_image_path = "./train_images"
NUM_EXAMPLES = len(next(os.walk(train_image_path))[2])
print("num_examples=", NUM_EXAMPLES)

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

features_batch = train_next_element
steps = int(NUM_EXAMPLES/batch_size)

logits = net.inference(
    input_tensor=features_batch,
    train=False,
    regularizer=None)

saver = tf.train.Saver()

num = 0
batch = 0

with tf.Session() as sess:

    sess.run(train_iterator.initializer)
    print("Reading checkpoints...")
    ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
    print("ckpt", ckpt)

    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)

        if not os.path.exists("./prediction_train_images"):
            os.makedirs("./prediction_train_images")

        for i in range(steps):
            out_put_image = sess.run(logits)

            for j in range(out_put_image.__len__()):

                scipy.misc.toimage(out_put_image[j], cmin=0.0, cmax=255)\
                    .save("./prediction_train_images/%d.jpg" % num)
                print("out_put_image", out_put_image[j][80][120])
                num += 1
                print("num=", num)
            print("=" * 20)
            batch += 1
            print("batch=", batch)

    else:
        print("No checkpoint file is found")
