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

	def add(self, video_writer):
		pass

	def __write(self, video_writer, cap):

		while cap.isOpened():

			ret, frame = cap.read()

			if ret:
				cv2.imshow('Frame', frame)
				self.__write_frame(video_writer, frame)
			else:
				break

	def __write_frame(self, video_writer, frame):
		video_writer.write(frame)