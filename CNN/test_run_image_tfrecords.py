"从TFRecords文件中读取数据"

import tensorflow as tf

batch_size = 128
filename = ["test.tfrecords"]


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
    print("=" * 10)
    print("batch_size=", batch_size)
    Dataset = Dataset.map(parser).batch(batch_size=batch_size)
    test_iterator = Dataset.make_initializable_iterator()
    test_next_element = test_iterator.get_next()
    print(test_next_element)
    

