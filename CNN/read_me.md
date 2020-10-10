#  各个文件的作用

---

* main.py		训练的主程序
* network.py   搭建模型的主文件
* ops.py           模型搭建的时候，需要用到的一些函数所在的文件
* utils.py          程序运行时，想输出一些结果，以及删除logs文件夹内所有已有文件
* tfrecords_train.py    生成训练集的tfrecords文件，特征和标签配对
* tfrecords_test.py      生成测试集的tfrecords文件，特征和标签配对
* train_read_from_tfrecords.py    从训练集的tfrecords文件读取数据，输入网络
* test_main.py    输出测试集的损失曲线
* test_run_image_tfrecords.py   将测试集的特征输入网络，输出预测结果
* test_to_image.py    输出测试集的结果的主运行文件

Enjoy
