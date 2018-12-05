import tensorflow as tf

# num_case就是总的case的个数除以batch_size的数目
# 总的case是2000，batch是2，这个数就是50，超过50就会报错
# epoch = 100, 总的case就有2000 * 100 = 200000
"""num_cases就是有多少个batch"""
"""1600个训练数据，1600*100 = 160000"""
"""400个训练数据，400*100 = 40000"""
"""要记得区分训练集和测试集"""
num_cases = 400
batch_size = 10
filename = ["test.csv.tfrecords"]

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
    test_dataset = tf.data.TFRecordDataset(filename)
    """测试数据的Dataset不需要经过打乱顺序和重复多个epoch，直接进行解析和batch"""
    test_dataset = test_dataset.map(parser).batch(batch_size=batch_size)
    """定义测试数据上的迭代器"""
    test_iterator = test_dataset.make_initializable_iterator()
    test_data_batch, test_label_batch = test_iterator.get_next()
