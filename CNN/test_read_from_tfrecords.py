"从TFRecords文件中读取数据"

import tensorflow as tf
from tfrecords_train import IMG_HEIGHT, IMG_WIDTH
from train_read_from_tfrecords import batch_size

buffer_size = 50000
filename = ["test.tfrecords"]


def parser(record):
    features = tf.parse_single_example(
        record,
        features={
            "images_raw": tf.FixedLenFeature([], tf.string),
            "features": tf.FixedLenFeature([10], tf.float32)
        }
    )

    "这里解析的时候图像的数据类型一定要是uint8!!!!!"
    decoded_image = tf.decode_raw(features['images_raw'], tf.uint8)
    decoded_image = tf.reshape(decoded_image, [IMG_HEIGHT,IMG_WIDTH])
    # decoded_images.shape [252, 400, 3]
    "但是可以在这里进行数据类型的修改！！！"
    decoded_image = tf.cast(decoded_image, tf.float32)
    print("decoded_images.shape", decoded_image.get_shape().as_list())

    feature = features['features']
    # feature.shape [10]
    print("feature.shape", feature.get_shape().as_list())
    return decoded_image, feature


with tf.name_scope('test_input_data') as scope:
    Dataset = tf.data.TFRecordDataset(filename)
    print("=" * 10)

    "测试集，不需要打乱顺序和重复多个epoch"
    Dataset = Dataset.map(parser).repeat().batch(batch_size=batch_size)
    test_iterator = Dataset.make_initializable_iterator()
    test_next_element = test_iterator.get_next()

# """
# 不是把下面的data和label导入train的文件！！！
# 而是把next_element导入train的文件
# """
# with tf.Session() as sess:
#     sess.run(iterator.initializer)
#     for i in range(num_cases):
#         images, features = sess.run(next_element)
#         # (32, 252, 400, 3)
#         print(images.shape)
