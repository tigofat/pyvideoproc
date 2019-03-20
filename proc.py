import cv2
import numpy as np
import time
import os

from models import Video

class VideoEditor:

    def __init__(self):
        pass

    def add_videos_in_folder(self, output_video_name, path):
        videos = []
        for name in os.listdir(path):
            if not name == '.DS_Store':
                videos.append(Video(f'{path}/{name}'))

        combined_video = videos[-1]
        del videos[-1]
        for i in range(len(videos)):
            combined_video += videos[i]

        self.write(output_video_name, combined_video)

    def write(self, output_video_name, video):
        start_time = time.time()
        video_writer = self.__create_video_writer(output_video_name, video.fps, 
            video.width, video.height)
        frames_count = 0
        for frame in video.frames:
            self.__write_frame(video_writer, frame)
            frames_count += 1
            per = frames_count * 100 / video.frames_count
            print(f'\rWritten {round(per, 1)} %', end='')

        print('')
        print(f'Writing took {round(time.time()-start_time, 4)}s.')

    def __create_video_writer(self, output_video_name, fps, width, height):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        return cv2.VideoWriter(f'{output_video_name}.avi', fourcc, fps, (width, height))

    def __write_frame(self, video_writer, frame):
        video_writer.write(frame)