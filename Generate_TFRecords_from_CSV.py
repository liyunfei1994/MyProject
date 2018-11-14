import os
import tensorflow as tf


def generate_tfrecords_file(input_filename, output_filename):
    print("Start to convert {} to {}".format(input_filename, output_filename))
    """创建一个writer来写TFRecords， 参数是输出文件的名字"""
    writer = tf.python_io.TFRecordWriter(output_filename)

    for line in open(input_filename, "r"):
        """line是个字符串， 调用split方法返回的是一个列表"""
        data = line.split(",")
        """label = ['2.33', '3.45'....]"""
        label = [float(i) for i in data[37:5566]]
        """features = [2.33, 3.45...], 将列表里的字符串变成了浮点数， 去掉了引号"""
        features = [float(i) for i in data[0:37]]
        """将读取到的数据放在protocol buffer中"""
        example = tf.train.Example(features=tf.train.Features(
            feature={
                "label":
                tf.train.Feature(float_list=tf.train.FloatList(value=label)),
                "features":
                tf.train.Feature(float_list=tf.train.FloatList(value=features)),
            }))
        """将protocol buffer的内容序列化为一个字符串，将该字符串写入TFRecords文件"""
        writer.write(example.SerializeToString())

    writer.close()

    print("Successfully convert {} to {}".format(input_filename, output_filename))


def main():
    current_path = os.getcwd()
    for filename in os.listdir(current_path):
        if filename.startswith("") and filename.endswith(".csv"):
            generate_tfrecords_file(filename, filename + ".tfrecords")


if __name__ == "__main__":
    main()
    
