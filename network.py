import tensorflow as tf

"""
有2000个case
"""
# INPUT_NODE = 784
# OUTPUT_NODE = 10
"""假设我现在有36个数据点，将其组织成6*6的矩阵"""
INPUT_SIZE = 36
OUTPUT_SIZE = 5528
NUM_CHANNELS = 1
NUM_LABELS = 5528
"""卷积核都是2*2的大小"""
CONV1_SIZE = 2
CONV1_DEPTH = 32

CONV2_SIZE = 2
CONV2_DEPTH = 64

FC_NODE = 512


def inference(input_tensor, train, regularizer):

    # [batch_size, 36] --> [batch_size, 6, 6, 1]
    input_tensor = tf.reshape(input_tensor, [-1, 6, 6, 1])
    """这里定义的卷积层的输入为6*6*1的数据"""
    with tf.variable_scope("conv1") as scope:
        conv1_weights = tf.get_variable(name="weights", shape=[CONV1_SIZE, CONV1_SIZE, NUM_CHANNELS, CONV1_DEPTH],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        conv1_biases = tf.get_variable(name="bias", shape=[CONV1_DEPTH], initializer=tf.constant_initializer(0.0))
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
        conv2_biases = tf.get_variable("bias", shape=[CONV2_DEPTH], initializer=tf.constant_initializer(0.0))
        """经过一次卷积， 输出为6*6*64"""
        conv2 = tf.nn.conv2d(pool1, conv2_weights, strides=[1, 1, 1, 1], padding="SAME")
        relu2 = tf.nn.relu(tf.nn.bias_add(conv2, conv2_biases))

    with tf.variable_scope("pool2") as scope:
        """池化之后，输出3*3*64, 步长为2"""
        pool2 = tf.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")

    """将其进行拉直"""
    pool_shape = pool2.get_shape().as_list()
    nodes = pool_shape[1] * pool_shape[2] * pool_shape[3]
    """[batch_size, 3*3*64]"""
    reshaped = tf.reshape(pool2, [-1, nodes])

    with tf.variable_scope("fully1") as scope:
        fc1_weights = tf.get_variable(name="weight", shape=[nodes, FC_NODE],
                                        initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer is not None:
            tf.add_to_collection('losses', regularizer(fc1_weights))

        fc1_biases = tf.get_variable(name="bias", shape=[FC_NODE], initializer=tf.constant_initializer(0.1))
        fc1 = tf.nn.relu(tf.matmul(reshaped, fc1_weights) + fc1_biases)
        if train:
            fc1 = tf.nn.dropout(fc1, 0.5)

    with tf.variable_scope("fully2") as scope:
        fc2_weights = tf.get_variable(name="weight", shape=[FC_NODE, NUM_LABELS],
                                      initializer=tf.truncated_normal_initializer(stddev=0.1))
        if regularizer is not None:
            tf.add_to_collection("losses", regularizer(fc2_weights))

        fc2_biases = tf.get_variable(name="bias", shape=[NUM_LABELS], initializer=tf.constant_initializer(0.1))

        logit = tf.add(tf.matmul(fc1, fc2_weights), fc2_biases)

    """输出为batch_size * NUM_LABELS"""
    return logit


"""Declare loss function (MSE)"""
def losses(logits, labels):
    with tf.variable_scope("loss") as scope:
        loss = tf.reduce_mean(tf.square(logits - labels))
        tf.summary.scalar(scope.name + '/loss', loss)
    return loss


def training(loss, learning_rate):
    with tf.variable_scope("optimizer") as scope:
        optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
        global_step = tf.Variable(0, name='global_step')
        train_op = optimizer.minimize(loss, global_step=global_step)
    return train_op
