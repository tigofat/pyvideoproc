import cv2
import numpy as np
import time
import os
import pprint as pp
import copy

from models import Video
from logic import shuffle, loading_

pprint = pp.PrettyPrinter().pprint

class VideoEditor:

    def __init__(self):
        pass

    def add_videos(self, output_video_name, videos, method='normal', cut_size=1):
        video_list = videos
        if method == 'random':
            print('▷ Randomizing...')
            cut_video_list = []
            for i in range(len(videos)):
                for j in range(videos[i].frames_count // cut_size):
                    cut_video_list.append(videos[i].cut((j*cut_size, j*cut_size+cut_size)))

            shuffle(cut_video_list, 5000)
            video_list = cut_video_list
        elif not method == 'normal':
            raise Exception("Method variable must be 'nomral' or 'random', depending on the way you would like to add videos together.")

        print('Combining...')
        combined_video = video_list[-1]
        del video_list[-1]
        for i in range(len(video_list)):
            combined_video += video_list[i]

        self.write_video(output_video_name, combined_video)

    def add_videos_from_dir(self, output_video_name, path, method='normal', cut_size=1):
        video_list = self.get_videos_from_dir(path)

        self.add_videos(output_video_name, video_list, method, cut_size)

    def write_video(self, output_video_name, video):
        start_time = time.time()
        video_writer = self.__create_video_writer(output_video_name, video.fps, 
            video.width, video.height)

        frames_count = 0
        for frame in video.frames:
            self.__write_frame(video_writer, frame)
            frames_count += 1
            per = frames_count * 100 / video.frames_count
            print(f'\rWriting {round(per, 1)} % Complete', end='')

        print('')
        print(f'Writing took {round(time.time()-start_time, 4)}s.')

    def get_videos_from_dir(self, path):
        videos = []
        for name in os.listdir(path):
            if not name == '.DS_Store':
                videos.append(Video(f'{path}/{name}'))
        return videos

    def __create_video_writer(self, output_video_name, fps, width, height):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        return cv2.VideoWriter(f'{output_video_name}.avi', fourcc, fps, (width, height))

    def __write_frame(self, video_writer, frame):
        video_writer.write(frame)