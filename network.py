import tensorflow as tf

"""
有2000个case
"""
# INPUT_NODE = 784
# OUTPUT_NODE = 10
"""假设我现在有36个数据点，将其组织成6*6的矩阵"""
# INPUT_SIZE = 36
# OUTPUT_SIZE = 5528
NUM_CHANNELS = 1
NUM_LABELS = 5528
"""卷积核都是2*2的大小"""
CONV1_SIZE = 2
CONV1_DEPTH = 32

CONV2_SIZE = 2
CONV2_DEPTH = 64

FC_NODE = 512

"""生成变量监控信息，并定义生成监控信息日志的操作，var是需要记录的张量"""
"""name给出了在可视化结果中显示的图表名称"""
def variable_summaries(var, name):

    # 将生成监控信息的操作放在同一个命名空间下
    with tf.name_scope("summaries"):
        tf.summary.histogram(name, var)
        mean = tf.reduce_mean(var)
        """定义生成平均值信息日志的操作"""
        tf.summary.scalar('mean/' + name, mean)
        stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
        """定义生成标准差信息日志的操作"""
        tf.summary.scalar('stddev/' + name, stddev)


def inference(input_tensor, train, regularizer):

    # [batch_size, 36] --> [batch_size, 6, 6, 1]
    with tf.variable_scope('input_reshape') as scope:
        input_tensor = tf.reshape(input_tensor, [-1, 6, 6, 1])
    """这里定义的卷积层的输入为6*6*1的数据"""
    with tf.variable_scope("conv1") as scope:
        conv1_weights = tf.get_variable(name="weights", shape=[CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEPTH],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        """调用生成权重监控信息日志的函数"""
        variable_summaries(conv1_weights, "conv1" + "/weights")
        conv1_biases = tf.get_variable(name="bias", shape=[CONV1_DEPTH], initializer=tf.constant_initializer(0.0))
        variable_summaries(conv1_biases, "conv1" + "/biases")
        """移动的步长为1"""
        conv1 = tf.nn.conv2d(input_tensor, conv1_weights, strides=[1, 1, 1, 1], padding="SAME")
        """经过一次卷积之后，大小为6*6*32"""
        relu1 = tf.nn.relu(tf.nn.bias_add(conv1, conv1_biases))

    with tf.variable_scope("pool1") as scope:
        """池化之后的大小为6*6*32，步长为1"""
        pool1 = tf.nn.max_pool(relu1, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding="SAME")

    with tf.variable_scope("conv2") as scope:
        conv2_weights = tf.get_variable(name="weights", shape=[CONV2_SIZE, CONV2_SIZE, CONV1_DEPTH, CONV2_DEPTH],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(conv2_weights, "conv2" + "/weights")
        conv2_biases = tf.get_variable("bias", shape=[CONV2_DEPTH], initializer=tf.constant_initializer(0.0))
        variable_summaries(conv2_biases, "conv2" + "/biases")
        """经过一次卷积， 输出为6*6*64"""
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding="SAME")
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.variable_scope("pool2") as scope:
        """池化之后，输出3*3*64, 步长为2"""
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    with tf.variable_scope("fullly_reshape") as scope:
        """将其进行拉直"""
        pool_shape = pool2.get_shape().as_list()
        nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
        """[batch_size, 3*3*64]"""
        reshaped = tf.reshape(pool2, [-1, nodes])

    with tf.variable_scope("fully1") as scope:
        fc1_weights = tf.get_variable(name="weight", shape=[nodes, FC_NODE],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(fc1_weights, "fully1" + "/weights")
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))

        fc1_biases = tf.get_variable(name="bias", shape=[FC_NODE], initializer=tf.constant_initializer(0.1))
        variable_summaries(fc1_biases, "fully1" + "/biases")
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope("fully2") as scope:
        fc2_weights = tf.get_variable(name="weight", shape=[FC_NODE, NUM_LABELS],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        variable_summaries(fc2_weights, "fully2" + "/weights")
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(fc2_weights))

        fc2_biases = tf.get_variable(name="bias", shape=[NUM_LABELS], initializer=tf.constant_initializer(0.1))
        variable_summaries(fc2_biases, "fully2" + "/biases")

        logit = tf.add(tf.matmul(fc1, fc2_weights), fc2_biases)

    """记录网络输出节点取值的分布"""
    tf.summary.histogram("network", logit)
    """输出为batch_size * NUM_LABELS"""
    return logit


"""Declare loss function (MSE)"""
"""这部分定义的是前向传播的损失，暂时不能将这部分的损失加入损失集合中"""
def losses(logits, labels):
    with tf.variable_scope("loss") as scope:
        loss = tf.reduce_mean(tf.square(logits - labels))
        """定义损失日志的操作"""
        tf.summary.scalar(scope.name + '/loss', loss)
    return loss

