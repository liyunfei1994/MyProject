import os
import cv2
import time


videos_src_path = "E:/new data/video_6/video/"
video_formats = [".cine"]
frames_save_path = "E:/PycharmProjects/wide_scope/schlieren_pictures/"
width = 800
height = 504
time_interval = 1


def video2frame(video_src_path, formats, frame_save_path, frame_width, frame_height, interval):
    """
    将视频按固定间隔读取写入图片
    :param video_src_path: 视频存放路径
    :param formats:　包含的所有视频格式
    :param frame_save_path:　保存路径
    :param frame_width:　保存帧宽
    :param frame_height:　保存帧高
    :param interval:　保存帧间隔
    :return:　帧图片
    """
    videos = os.listdir(video_src_path)
    # videos-->['6400.cine'],列表里是字符串
    print("videos", videos)
    each_video = videos[0]
    print ("正在读取视频：", each_video)

    # 取出视频名字，去掉.cine后缀名 6400
    each_video_name = each_video[:-5]
    if not os.path.exists(frame_save_path + each_video_name):
        os.mkdir(frame_save_path + each_video_name)
    # "E:/PycharmProjects/pictures/6400"
    # 每一个视频存放照片的地址
    each_video_save_full_path = os.path.join(frame_save_path, each_video_name) + "/"
    # each_video_save_full_path E:/PycharmProjects/wide_scope/schlieren_pictures/6400/
    print("each_video_save_full_path",each_video_save_full_path)
    # 每一个视频的地址
    each_video_full_path = os.path.join(video_src_path, each_video)
    # each_video_full_path E:/new data/video/6400.cine
    print("each_video_full_path", each_video_full_path)

    cap = cv2.VideoCapture(each_video_full_path)
    # cap <VideoCapture 000001DE8706CEF0> type <class 'cv2.VideoCapture'>
    print("cap", cap, "type", type(cap))
    "frame_index指的是第几帧，目的是间隔多少帧取一个"
    frame_index = 0
    "frame_count指的是保存照片的时候的顺序"
    frame_count = 0

    if cap.isOpened():
        success = True
    else:
        success = False
        print("读取失败!")

    while(success):
        success, frame = cap.read()
        print ("---> 正在读取第%d帧:" % frame_index, success)

        # 1411是红灯亮的第一张照片
        if frame_index>=2580 and frame_index < 32400:
            resize_frame = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_AREA)
            # cv2.imwrite(each_video_save_full_path + each_video_name + "_%d.jpg" % frame_index, resize_frame)
            print("---> 正在写入第%d帧：" % frame_index)
            cv2.imshow('input', resize_frame)
            cv2.waitKey(100)
            cv2.imwrite(each_video_save_full_path + "%d.jpg" % frame_count, resize_frame)
            frame_count += 1

        frame_index += 1

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start_time = time.time()
    video2frame(videos_src_path, video_formats, frames_save_path, width, height, time_interval)
    end_time = time.time()
    print("end, during time is %.2f minutes" % ((end_time - start_time)/60.0))

