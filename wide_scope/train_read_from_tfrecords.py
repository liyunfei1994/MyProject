import tensorflow as tf
from tfrecords_train import IMG_HEIGHT, IMG_WIDTH

buffer_size = 100000
batch_size = 64
num_epochs = 900
filename = ["train.tfrecords"]


def parser(record):
    features = tf.io.parse_single_example(
        record,
        features={
            "images_raw": tf.io.FixedLenFeature([], tf.string),
            "features": tf.io.FixedLenFeature([10], tf.float32)
        }
    )

    # "这里解析的时候图像的数据类型一定要是uint8!!!!!"
    decoded_image = tf.decode_raw(features['images_raw'], tf.uint8)
    decoded_image = tf.reshape(decoded_image, [IMG_HEIGHT, IMG_WIDTH])
    # decoded_images.shape [252, 400]
    # "但是可以在这里进行数据类型的修改！！！"
    decoded_image = tf.cast(decoded_image, tf.float32)
    # [403, 640]
    print("decoded_images.shape", decoded_image.get_shape().as_list())

    feature = features['features']
    # feature.shape [10]
    print("feature.shape", feature.get_shape().as_list())
    return decoded_image, feature


with tf.name_scope('train_input_data') as scope:
    Dataset = tf.data.TFRecordDataset(filename)
    print("=" * 10)
    print("batch_size=", batch_size)
    Dataset = Dataset.map(parser).shuffle(buffer_size=buffer_size).repeat(num_epochs).batch(batch_size=batch_size)
    train_iterator = Dataset.make_initializable_iterator()
    train_next_element = train_iterator.get_next()

# with tf.Session() as sess:
#     sess.run(train_iterator.initializer)
#     for i in range(2):
#         images, features = sess.run(train_next_element)
#         # (4, 403, 640)
#         print("images.shape",images.shape)
#         # (4, 10)
#         print("features.shape", features.shape)
