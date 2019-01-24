"""
Some codes from https://github.com/Newmu/dcgan_code
"""
"这份代码主要是定义了各种对图像处理的函数，相当于其他3个文件的头文件。"
import math
import imageio
import random
import pprint
import scipy.misc
import numpy as np
from time import gmtime, strftime
import cv2
import tensorflow as tf
import tensorflow.contrib.slim as slim


pp = pprint.PrettyPrinter()
get_stddev = lambda x, k_h, k_w: 1/math.sqrt(k_w*k_h*x.get_shape()[-1])


def show_all_variables():
    # tf.trainable_variables()返回的是一个列表
    print("列出所有的变量")
    model_vars = tf.trainable_variables()
    slim.model_analyzer.analyze_vars(model_vars, print_info=True)

"imread函数返回的是numpy数组"
def imread(path, grayscale = False):
    # print("-.-" * 10)
    # print("进入读取图片的函数 imread")
    if (grayscale):
        # print("图片为灰度图片，读取图片")
        return cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    else:
        # print("图片为彩色图片，读取图片")
        return cv2.imread(path)


def get_image(image_path, input_height, input_width,
              resize_height=100, resize_width=158,
              crop=False, grayscale=False):
    # print("-.-" * 10)
    # print("进入获取图片的函数 get_image")
    image = imread(image_path, grayscale)
    # print("读取图片返回的结果是", type(image))
    return transform(image, input_height, input_width,
                     resize_height, resize_width, crop)


"transform函数的作用就是进行resize"
def transform(image, input_height, input_width,
              resize_height=100, resize_width=158, crop=False):
    # print("-.-" * 10)
    # print("进入transform函数")
    if crop:
        # print("进行裁剪")
        cropped_image = center_crop(
            image, input_height, input_width,
            resize_height, resize_width)
    else:
        # print("不进行裁剪")
        cropped_image = cv2.resize(src=image, dsize=(resize_width, resize_height))
        "这里进行了修改，直接返回了resize之后的"
    # print("transform函数的结果是", cropped_image.shape)
    return cropped_image


def center_crop(x, crop_h, crop_w,
                resize_h=100, resize_w=158):
    if crop_w is None:
        crop_w = crop_h
    h, w = x.shape[:2]
    j = int(round((h - crop_h)/2.))
    i = int(round((w - crop_w)/2.))
    "要注意这个resize函数图片的高和宽与TensorFlow是相反的"
    return cv2.resize(
      src=x[j:j+crop_h, i:i+crop_w], dsize=(resize_w, resize_h))


"以上是获得图片的函数，以下是保存图片的函数"


def save_images(images, size, image_path):
    # numpy 数组 [64, 100, 158, 3]
    print("传入save_images函数的 images 是", type(images),"维度", images.shape)
    print("传入的size", size)
    return imsave(inverse_transform(images), size, image_path)

def imsave(images, size, path):
    print("进入 imsave 函数")
    image = np.squeeze(merge(images, size))
    print("merge函数成功完成，结果是", image.shape)   # [400, 632, 3]
    print("现在merger函数中的image是", image.shape)
    return scipy.misc.imsave(path, image)


def inverse_transform(images):
    print("进入 inverse_transform 函数")
    print("inverse_transform 的shape", images.shape)   #[16, 100, 158, 3]
    return (images+1.)/2.


def merge_images(images, size):
    return inverse_transform(images)


def merge(images, size):
    print("进入 merge 函数")
    print("把16张照片合成一张照片")
    h, w = images.shape[1], images.shape[2]
    # h 100, w 158
    print("h", h, "w", w)
    if (images.shape[3] in (3,4)):
        # print("images.shape[3]=", images.shape[3]) # 3
        c = images.shape[3]
        # h * size[0]=100 * 4= 400
        # w * size[1]=158 * 4 = 632
        img = np.zeros((h * size[0], w * size[1], c))
        # print("img-shape", img.shape)   # [400, 632,3]
        for idx, image in enumerate(images):
            # print("idx", idx)  idx[0-15]
            # print("image", type(image),"维度是", image.shape)  numpy数组，[100, 158, 3]
            # size[1] = 4
            i = idx % size[1] # [0123 0123 0123 0123]
            # print("i",i)
            j = idx // size[1]  #[0000 1111 2222 3333]
            # print("j", j)
            img[j * h:j * h + h, i * w:i * w + w, :] = image

        print("img", img.shape) # [400, 632, 3]
        return img
    # elif images.shape[3]==1:
    #     img = np.zeros((h * size[0], w * size[1]))
    #     for idx, image in enumerate(images):
    #         i = idx % size[1]
    #         j = idx // size[1]
    #         img[j * h:j * h + h, i * w:i * w + w] = image[:,:,0]
    #     return img
    else:
        raise ValueError('in merge(images,size) images parameter '
                         'must have dimensions: HxW or HxWx3 or HxWx4')



def image_manifold_size(num_images):
    print("进入 image_manifold_size 函数")
    print("传入 image_manifold_size 函数的参数是", num_images)   #32
    # 5
    manifold_h = int(np.floor(np.sqrt(num_images)))
    # print("manifold_h", manifold_h)
    # 5
    manifold_w = int(np.ceil(np.sqrt(num_images)))
    # print("manifold_w", manifold_w)

    # print("判断以下这步是否正确")
    assert manifold_h * manifold_w == num_images
    print("assert 正确")
    "返回两个元素，返回的是元组"
    return manifold_h, manifold_w


def make_gif(images, fname, duration=2, true_image=False):
    import moviepy.editor as mpy

    def make_frame(t):
        try:
            x = images[int(len(images)/duration*t)]
        except:
            x = images[-1]

        if true_image:
            return x.astype(np.uint8)
        else:
            return ((x+1)/2*255).astype(np.uint8)

    clip = mpy.VideoClip(make_frame, duration=duration)
    clip.write_gif(fname, fps = len(images) / duration)

def visualize(sess, dcgan, config, option):
    image_frame_dim = int(math.ceil(config.batch_size**.5))
    if option == 0:
        z_sample = np.random.uniform(-0.5, 0.5, size=(config.batch_size, dcgan.z_dim))
        samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
        save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_%s.png' % strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
    elif option == 1:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.random.uniform(-1, 1, size=(config.batch_size , dcgan.z_dim))
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            if config.dataset == "mnist":
                y = np.random.choice(10, config.batch_size)
                y_one_hot = np.zeros((config.batch_size, 10))
                y_one_hot[np.arange(config.batch_size), y] = 1

                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample, dcgan.y: y_one_hot})
            else:
                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})

            save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_arange_%s.png' % (idx))
    elif option == 2:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in [random.randint(0, dcgan.z_dim - 1) for _ in range(dcgan.z_dim)]:
            print(" [*] %d" % idx)
            z = np.random.uniform(-0.2, 0.2, size=(dcgan.z_dim))
            z_sample = np.tile(z, (config.batch_size, 1))
            #z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            if config.dataset == "mnist":
                y = np.random.choice(10, config.batch_size)
                y_one_hot = np.zeros((config.batch_size, 10))
                y_one_hot[np.arange(config.batch_size), y] = 1

                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample, dcgan.y: y_one_hot})
            else:
                samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})

            try:
                make_gif(samples, './samples/test_gif_%s.gif' % (idx))
            except:
                save_images(samples, [image_frame_dim, image_frame_dim], './samples/test_%s.png' % strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
    elif option == 3:
        values = np.arange(0, 1, 1./config.batch_size)
        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample):
                z[idx] = values[kdx]

            samples = sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample})
            make_gif(samples, './samples/test_gif_%s.gif' % (idx))
    elif option == 4:
        image_set = []
        values = np.arange(0, 1, 1./config.batch_size)

        for idx in range(dcgan.z_dim):
            print(" [*] %d" % idx)
            z_sample = np.zeros([config.batch_size, dcgan.z_dim])
            for kdx, z in enumerate(z_sample): z[idx] = values[kdx]

            image_set.append(sess.run(dcgan.sampler, feed_dict={dcgan.z: z_sample}))
            make_gif(image_set[-1], './samples/test_gif_%s.gif' % (idx))

        new_image_set = [merge(np.array([images[idx] for images in image_set]), [10, 10]) \
                         for idx in range(64) + range(63, -1, -1)]
        make_gif(new_image_set, './samples/test_gif_merged.gif', duration=8)



