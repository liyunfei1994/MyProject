import os
import tensorflow as tf

"""
To verify the TFRecords, you can iterate and print each example with this .py
"""
def print_tfrecords_file(input_filename):
    print("Try to print the TFRecords file: {}".format(input_filename))

    max_print_number = 10
    current_print_index = 0
    """An iterator that read the records from a TFRecords file."""
    for serialized_example in tf.python_io.tf_record_iterator(input_filename):
    # Get serialized example from file
        """此时打印example是没有内容的，空的"""
        example = tf.train.Example()
        """因为写进TFRecords文件的是一个字符串，因此需要从字符串中解析出来"""
        """解析之后打印，example发生改变，才能打印出内容"""
        example.ParseFromString(serialized_example)
        label = example.features.feature["label"].float_list.value
        features = example.features.feature["features"].float_list.value
        print("Index: {}, features: {}, label: {}".format(current_print_index,
                                                          features, label))

    # Return when reaching max print number
        current_print_index += 1
        if current_print_index > max_print_number - 1:
            return


def main():
    current_path = os.getcwd()
    for filename in os.listdir(current_path):
        if filename.startswith("") and filename.endswith(".tfrecords"):
            TFRecords_file_path = os.path.join(current_path, filename)
            print_tfrecords_file(TFRecords_file_path)


if __name__ == "__main__":
    main()
