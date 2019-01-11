import tensorflow as tf
import tensorflow.contrib.slim as slim

x1=tf.Variable(tf.constant(1,shape=[1],dtype=tf.float32),name='x11')
x2=tf.Variable(tf.constant(2,shape=[1],dtype=tf.float32),name='x22')
m=tf.train.ExponentialMovingAverage(0.99,5)
v=tf.trainable_variables()
for i in v:
    print ('-'*10)
    print (i)

print ('*'*10)   
slim.model_analyzer.analyze_vars(v,print_info=True)
print ('*'*10)


----------
<tf.Variable 'x11:0' shape=(1,) dtype=float32_ref>
----------
<tf.Variable 'x22:0' shape=(1,) dtype=float32_ref>
**********
---------
Variables: name (type shape) [size]
---------
x11:0 (float32_ref 1) [1, bytes: 4]
x22:0 (float32_ref 1) [1, bytes: 4]
Total size of variables: 2
Total bytes of variables: 8
**********

#tf.trainable_variables返回的是需要训练的变量列表；
#然后用tensorflow.contrib.slim中的model_analyzer.analyze_vars打印出所有与训练相关的变量信息
