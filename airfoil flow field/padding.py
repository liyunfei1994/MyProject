import tensorflow as tf

x1 = tf.constant(1.0, shape=[1,3,3,1])
kernel = tf.constant(1.0, shape=[3,3,3,1])
x2 = tf.constant(1.0, shape=[1,6,6,3])
x3 = tf.constant(1.0, shape=[1,5,5,3])

# y2 = tf.nn.conv2d(x3, kernel, strides=[1,2,2,1], padding="SAME")
y2 = tf.nn.conv2d(x3, kernel, strides=[1,2,2,1], padding="VALID")

print(y2.shape)
sess = tf.Session()
print(sess.run(y2))

padding = "SAME"
Noutput = [Ninput/stride]
输出图像的大小等于输入图像的大小除以步长，向上取整
这里，输入大小为5,5,3， 步长为2， 5/2向上取整为3
(1, 3, 3, 1)
[[[[12.]
   [18.]
   [12.]]

  [[18.]
   [27.]
   [18.]]

  [[12.]
   [18.]
   [12.]]]]
…………………………………
padding = "VALID"
Noutput = [Ninput-f+1/s]
输出图像大小等于输入图像大小减去卷积核大小+1，再除以步长
这里，输入大小为5,5,3,步长为2，卷积核大小为3， 5-3+1/2 向上取整为2
(1, 2, 2, 1)
[[[[27.]
   [27.]]

  [[27.]
   [27.]]]]
   
   
