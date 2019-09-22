"从TFRecords文件中读取数据"

import tensorflow as tf
from train_read_from_tfrecords import batch_size

filename = ["train.tfrecords"]


def parser(record):
    features = tf.parse_single_example(
        record,
        features={
            "images_raw": tf.FixedLenFeature([], tf.string),
            "features": tf.FixedLenFeature([10], tf.float32)
        }
    )

    feature = features['features']
    print("feature.shape", feature.get_shape().as_list())
    return feature


with tf.name_scope('input_data') as scope:
    Dataset = tf.data.TFRecordDataset(filename)
    Dataset = Dataset.map(parser).batch(batch_size=batch_size)
    train_iterator = Dataset.make_initializable_iterator()
    train_next_element = train_iterator.get_next()

