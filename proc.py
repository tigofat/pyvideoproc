import cv2
import numpy as np
import time

from models import Video

class VideoEditor:

    def __init__(self):
        pass

    def write(self, output_video_name, video):
        video_writer = self.__create_video_writer(output_video_name, video.fps, 
            video.width, video.height)
        frames_count = 0
        for frame in video.frames:
            self.__write_frame(video_writer, frame)
            frames_count += 1
            per = frames_count * 100 / video.frames_count
            print(f'\rWritten {round(per, 1)} %', end='')

        print('')

    def __create_video_writer(self, output_video_name, fps, width, height):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        return cv2.VideoWriter(f'{output_video_name}.avi', fourcc, fps, (width, height))

    def __write_frame(self, video_writer, frame):
        video_writer.write(frame)