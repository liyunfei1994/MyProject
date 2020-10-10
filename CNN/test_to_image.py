import tensorflow as tf
import Network
import os
from test_run_image_tfrecords import test_iterator, test_next_element, batch_size
import scipy.misc


MODEL_SAVE_PATH = './logs'
test_images_gray = "./test_images_gray"
NUM_EXAMPLES = len(next(os.walk(test_images_gray))[2])

os.environ["CUDA_VISIBLE_DEVICES"] = "1, 3"

features_batch = test_next_element
steps = int(NUM_EXAMPLES/batch_size)

logits = Network.inference(
    input_tensor=features_batch,
    regularizer=None)

saver = tf.train.Saver()

num = 0
batch = 0

with tf.Session() as sess:

    sess.run(test_iterator.initializer)
    print("Reading checkpoints...")
    ckpt = tf.train.get_checkpoint_state(MODEL_SAVE_PATH)
    print("ckpt", ckpt)

    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess=sess, save_path=ckpt.model_checkpoint_path)

        if not os.path.exists("./prediction_test_images"):
            os.makedirs("./prediction_test_images")

        for i in range(steps):
            out_put_image = sess.run(logits)

            for j in range(out_put_image.__len__()):

                scipy.misc.toimage(out_put_image[j], cmin=0.0, cmax=255)\
                    .save("./prediction_test_images/%d.jpg" % num)
                print("out_put_image", out_put_image[j][80][120])
                num += 1
                print("num=", num)
            print("=" * 20)
            batch += 1
            print("batch=", batch)

    else:
        print("No checkpoint file is found")
