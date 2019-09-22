import os
import tensorflow as tf
import numpy as np
import re
import time
import cv2
from PIL import Image

"""
这个程序生成了测试集的TFRecords文件
"""

image_path = "./test_images"
pressure_path = "./test_pressure.csv"
resize_ratio = 0.8
IMG_HEIGHT = int(504 * resize_ratio)
IMG_WIDTH = int(800 * resize_ratio)

def read_images_and_pressure(image_path, pressure_path):
    blank_list = []
    # new_file_list 用于存放改变顺序之后的图片的路径
    new_file_list = []
    file_names = next(os.walk(image_path))[2]
    "file_names中的图片的顺序是乱的"
    # print("file_names", file_names)
    # print()
    # print()
    for i in file_names:
        a = re.sub('[.jpg]', '', i)
        blank_list.append(int(a))

    # print("blank_list", blank_list)

    blank_list.sort()
    print("sort")
    # print("blank_list", blank_list)

    for i in blank_list:
        i = str(i) + '.jpg'
        new_file_list.append(i)
    # new_file_list 中存放的图片顺序是从小到大的排列
    # print("new_file_list", new_file_list)
    num_files = len(file_names)
    print("num_files", num_files)

    images = np.zeros(shape=(num_files, IMG_HEIGHT, IMG_WIDTH),dtype=np.uint8)
    features = np.zeros(shape=(num_files, 10), dtype=np.float32)

    # print("features", features.shape)
    f = open(pressure_path)
    lines = f.readlines()
    for i, pressure_data in enumerate(lines):
        # i 是序号，pressure_data是字符串，以逗号分隔，结尾是\n
        a = pressure_data.rstrip('\n').split(',')
        b = [float(i) for i in a]
        features[i] = b

    f.close()

    for i, image in enumerate(new_file_list):
        img = np.array(Image.open(os.path.join(image_path, image)))
        # type(img) > numpy ndarray  (504, 800, 3)
        if img is None:
            print("Error: could not load image")
        else:
            print("Before resize:")
            print("img.shape", img.shape)

        try:
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            images[i] = img
            print("After resize:")
            print("images[%d].shape %s, %s" % (i,images[i].shape, type(images[i])))
        except BaseException:
            print("Error: could not resize")

    print("images.shape", images.shape)
    # images.shape (10000, 252, 400, 3)
    print("features.shape", features.shape)
    # features.shape (10000, 10)

    # 返回两个值，就是元组

    return images, features


def _float_feature(value):
    # print("_float_feature, type(value)", type(value))  # ndarray
    # print("float shape", value.shape)  # (10, )
    return tf.train.Feature(float_list=tf.train.FloatList(value=value))


def _bytes_images(value):
    # print("_bytes_feature, type(value)", type(value))   # bytes
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def generate_tfrecords_file(
        input_image_filename,
        input_features_name,
        output_filename):
    num = input_image_filename.shape[0]
    print("num =", num)  # 10000
    output_filename += ".tfrecords"
    # 创建一个writer来写TFRecords， 参数是输出文件的名字
    print("write in", output_filename)
    writer = tf.io.TFRecordWriter(output_filename)

    for i in range(num):
        img_raw = input_image_filename[i].tobytes()
        # print("type(img_raw)", type(img_raw), "len(img_raw)", len(img_raw))
        example = tf.train.Example(features=tf.train.Features(
            feature={
                'features': _float_feature(input_features_name[i]),
                'images_raw': _bytes_images(img_raw)
            }
        ))
        writer.write(example.SerializeToString())

    writer.close()

    print("Successfully convert to {}".format(output_filename))


def main():
    print("reading images begin!")
    start_time = time.time()
    images, features = read_images_and_pressure(
        image_path=image_path, pressure_path=pressure_path)

    duration = time.time() - start_time
    print("reading images end, cost %.2f minutes" % (duration / 60.0))

    "convert to TFRecords"
    print("convert to TFRecords begin!")
    s_time = time.time()
    generate_tfrecords_file(
        input_image_filename=images,
        input_features_name=features,
        output_filename="test")
    dura_time = time.time() - s_time
    print("convert to TFRecords end, cost %.2f minutes" % (dura_time / 60.0))


if __name__ == "__main__":
    main()
