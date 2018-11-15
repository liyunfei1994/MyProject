import tensorflow as tf

num_cases = 10
buffer_size = 10000
batch_size = 2
num_epochs = 2

filename = ["train.csv.tfrecords"]
Dataset = tf.data.TFRecordDataset(filename)
"""原有的Dataset中的数据类型是tf.string，需要进行解析才能转成Tensor"""
"""<TFRecordDataset shapes: (), types: tf.string>"""
"""Cast string to float is not supported"""
# print(Dataset)
def parser(record):
    features = tf.parse_single_example(
        record,
        features = {
            "label": tf.FixedLenSequenceFeature([], tf.float32, allow_missing=True),
            "features": tf.FixedLenSequenceFeature([], tf.float32, allow_missing=True)
        }
    )
    """{'features': <tf.Tensor 'ParseSingleExample/ParseSingleExample:0' shape=(?,) dtype=float32>, """
    """'label': <tf.Tensor 'ParseSingleExample/ParseSingleExample:1' shape=(?,) dtype=float32>}"""
    # print("features-->",features)
    """解析之后，features 是一个字典"""
    """Type--> <class 'dict'>"""
    # print("Type-->", type(features))
    """此时data的dtype就是tensor"""
    """features['features']--> <class 'tensorflow.python.framework.ops.Tensor'>"""
    # print("features['features']-->",type(features['features']))
    data = tf.cast(features['features'], tf.float32)
    """type(data)--> <class 'tensorflow.python.framework.ops.Tensor'>"""
    """data 是个Tensor"""
    # print("type(data)-->",type(data))
    label = tf.cast(features['label'], tf.float32)


    return data, label

Dataset = Dataset.map(parser).shuffle(buffer_size=buffer_size).batch(batch_size=batch_size).repeat(num_epochs)

iterator = Dataset.make_initializable_iterator()

next_element = iterator.get_next()
"""<class 'tuple'>"""
# print(type(next_element))

with tf.Session() as sess:
    sess.run(iterator.initializer)
    for i in range(num_cases):
        data, label = sess.run(next_element)
        """type(data)--> numpy.ndarray"""
        print(data.shape)
