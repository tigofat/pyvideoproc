import cv2
import numpy as np

from models import Video

class VideoEditor:

    def __init__(self):
        pass

    def create_video_writer(self, output_video_name, fps, width, height):
    	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    	return cv2.VideoWriter(f'{output_video_name}.avi', fourcc, fps, (width, height))

    def add_videos(self, output_video_name, videos):
        video_writer = self.create_video_writer(output_video_name, videos[0].fps, 
            videos[0].width, videos[0].height)

        for video in videos:
            self.__write(video_writer, video)

    def __write(self, video_writer, video):
        cap = video.cap
        frames = 0
        while cap.isOpened():

            ret, frame = cap.read()
            if ret:
                per = frames * 100 / video.frames
                print(f'Written {round(per, 1)} % from {video.path} video.')
                self.__write_frame(video_writer, frame)
                frames += 1
            else:
                break

    def __write_frame(self, video_writer, frame):
        video_writer.write(frame)