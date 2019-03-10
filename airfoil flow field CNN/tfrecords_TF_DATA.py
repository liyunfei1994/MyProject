import tensorflow as tf
from tfrecords import IMG_HEIGHT, IMG_WIDTH, IMG_CHANNEL

num_cases = 500
buffer_size = 10000000
batch_size = 64
num_epochs = 50
filename = ["train.tfrecords"]


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
    decoded_image = tf.reshape(decoded_image, [IMG_HEIGHT,IMG_WIDTH,IMG_CHANNEL])
    # decoded_images.shape [252, 400, 3]
    "但是可以在这里进行数据类型的修改！！！"
    decoded_image = tf.cast(decoded_image, tf.float32)
    print("decoded_images.shape", decoded_image.get_shape().as_list())

    feature = features['features']
    # feature.shape [10]
    print("feature.shape", feature.get_shape().as_list())
    return decoded_image, feature


with tf.name_scope('input_data') as scope:
    Dataset = tf.data.TFRecordDataset(filename)
    print("=" * 10)
    Dataset = Dataset.map(parser).shuffle(buffer_size=buffer_size).batch(batch_size=batch_size).repeat(num_epochs)
    iterator = Dataset.make_initializable_iterator()
    next_element = iterator.get_next()

# """
# 不是把下面的data和label导入train的文件！！！
# 而是把next_element导入train的文件
# """
# with tf.Session() as sess:
#     sess.run(iterator.initializer)
#     for i in range(num_cases):
#         images, features = sess.run(next_element)
#         # (64, 252, 400, 3)
#         print(images.shape)
