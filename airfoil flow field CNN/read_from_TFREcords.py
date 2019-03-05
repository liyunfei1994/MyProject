import tensorflow as tf
from PIL import Image
import os
import cv2
import scipy.misc


TRAIN_FILE = 'train.tfrecords'
gen_picture = './pictures_out'

IMG_HEIGHT = 252
IMG_WIDTH = 400
IMG_CHANNELS = 3
IMG_PIXELS = IMG_HEIGHT * IMG_WIDTH * IMG_CHANNELS

batch_size = 64
epoches = 15

def read_and_decode(filename_queue):
    #创建一个reader来读取TFRecord文件中的样例
    reader = tf.TFRecordReader()
    #从文件中读出一个样例
    _,serialized_example = reader.read(filename_queue)
    #解析读入的一个样例
    features = tf.parse_single_example(serialized_example,features={
        'features':tf.FixedLenFeature([10],tf.float32),
        'images_raw':tf.FixedLenFeature([],tf.string)
        })
    #将字符串解析成图像对应的像素数组
    image = tf.decode_raw(features['images_raw'],tf.uint8)
    image = tf.reshape(image,[IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS])
    # image Tensor("sub:0", shape=(252, 400, 3), dtype=float32)
    # read_and_decode image [126, 200, 3]
    print("read_and_decode image", image.get_shape().as_list())

    feature = features['features']
    # read_and_decode feature [10]
    print("read_and_decode feature", feature.get_shape().as_list())

    return image,feature

def inputs(batch_size,num_epochs):
    file = TRAIN_FILE

    with tf.name_scope('input') as scope:
        filename_queue = tf.train.string_input_producer([file], shuffle=False, num_epochs=num_epochs)
        # filename_queue <tensorflow.python.ops.data_flow_ops.FIFOQueue object at 0x7f0e72755ac8>
        print("filename_queue", filename_queue)
    image,feature = read_and_decode(filename_queue)
    # image Tensor("sub:0", shape=(252, 400, 3), dtype=float32)
    # feature Tensor("Cast:0", shape=(), dtype=int32)
    # inputs image [126, 200, 3]
    print("inputs image", image.get_shape().as_list())
    # inputs feature [10]
    print("inputs feature", feature.get_shape().as_list())
    #随机获得batch_size大小的图像和label
    images_batch,features_batch = tf.train.shuffle_batch([image, feature],
        batch_size=batch_size,
        num_threads=10000,
        capacity=10000 + 3 * batch_size,
        min_after_dequeue=10000
    )

    # 到这里，就组成了batch数据
    return images_batch,features_batch


if __name__ == '__main__':

    image_batch, features_batch = inputs(batch_size=batch_size, num_epochs=epoches)
    init_op = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())

    sess = tf.Session()
    sess.run(init_op)
    # 启动多线程处理数据，创建一个协调器，管理线程
    coord = tf.train.Coordinator()
    # 启动文件名队列线程，让队列跑起来
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
        for i in range(2734):
            images = sess.run(image_batch)
            print("images", type(images))  # ndarray
            # images.shape (64, 126, 200, 3)
            print("images.shape", images.shape)  # ndarray
            features = sess.run(features_batch)
            print("features", type(features))   # ndarray
            # features.shape (64, 10)
            print("features.shape", features.shape)  # ndarray

            "可以算到这一步了"
            "解决了保存图像的问题，images是个batch，不能直接保存images，只能保存batch中的一个，images[0]"
            # scipy.misc.toimage(images, cmin=0, cmax=255).save((gen_picture + '/' + "sample" + '%s') % i)
            im = Image.fromarray(images[0], mode='RGB')
            im.save((gen_picture + '/' + "sample" + "%s" + ".png") % i)
            print(("write ok" + "=" * 5 + "i = " + "%s") % i)
    except tf.errors.OutOfRangeError:
        print("OutOfRangeError")
    coord.request_stop()
    coord.join(threads)
    sess.close()
