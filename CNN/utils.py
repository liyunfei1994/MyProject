import tensorflow.contrib.slim as slim
import tensorflow as tf


def show_all_variables():
    # tf.trainable_variables()返回的是一个列表
    print("Show All Variables")
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)

# 用递归的方式删除文件夹下的所有文件
def delAll(path):
    if os.path.isdir(path):
        files = os.listdir(path)  # ['a.doc', 'b.xls', 'c.ppt']
        # 遍历并删除文件
        for file in files:
            p = os.path.join(path, file)
            if os.path.isdir(p):
                # 递归
                delAll(p)
            else:
                os.remove(p)
        # 删除文件夹
        os.rmdir(path)
    else:
        os.remove(path)
