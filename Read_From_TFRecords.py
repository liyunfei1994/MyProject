import tensorflow as tf

"""num_cases就是有多少个batch"""
"""1600个训练数据，1600*100 = 160000"""
"""400个训练数据，400*100 = 40000"""
"""要记得区分训练集和测试集"""
num_cases = 20800
buffer_size = 10000000
batch_size = 5
num_epochs = 65
filename = ["train.csv.tfrecords"]

def parser(record):
    features = tf.parse_single_example(
        record,
        features={
            "label": tf.FixedLenSequenceFeature([], tf.float32, allow_missing=True),
            "features": tf.FixedLenSequenceFeature([], tf.float32, allow_missing=True)
        }
    )
    data = tf.cast(features['features'], tf.float32)
    label = tf.cast(features['label'], tf.float32)
    return data, label


with tf.name_scope('input_data') as scope:
    filename = filename
    Dataset = tf.data.TFRecordDataset(filename)
    Dataset = Dataset.map(parser).shuffle(buffer_size=buffer_size
                                          ).batch(batch_size=batch_size).repeat(num_epochs)
    iterator = Dataset.make_initializable_iterator()
    # sess = tf.Session()
    # sess.run(iterator.initializer)
    # next_element是个元组
    next_element = iterator.get_next()

"""
不是把下面的data和label导入train的文件！！！
而是把next_element导入train的文件
"""
with tf.Session() as sess:
    sess.run(iterator.initializer)
    for i in range(num_cases):
        data, label = sess.run(next_element)
        # print(label.shape)
        """type(data)--> numpy.ndarray"""
        # print(data.shape)
        """shape-->(5,36)"""
        # print(label.shape)
        """shape-->(5,5528)"""
