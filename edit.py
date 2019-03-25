import cv2
import numpy as np
import time
import os
import pprint as pp
from copy import deepcopy

from models import Video

pprint = pp.PrettyPrinter().pprint

def create_video_writer(output_video_name, fps, width, height):
	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
	return cv2.VideoWriter(f'{output_video_name}.avi', fourcc, fps, (width, height))


def write(output_video_name, video):
	video_writer = create_video_writer(output_video_name, video.fps, 
		video.width, video.height)
	for frame in video.frames:
		video_writer.write(frame)


class VideoProc:
	
	def __init__(self, frames):
		self._frames = frames

	@property
	def video(self):
		return self._video


class VideoEditor:

	def __init__(self, video):
		self._video = video
		self._frames = video.frames

	def add(self, other):
		frames = other.frames if isinstance(other, Video) else other
		self._frames = np.hstack((self._frames, frames))

	def mul(self, times):
		original_video_frames = self._frames
		for i in range(1, times):
			self._frames = np.hstack((self._frames, original_video_frames))

	def cut(self, places):
		cut = self._frames[places[0]:places[1]]
		self._frames = np.hstack((self._frames[:places[0]], self._frames[places[1]:]))
		return cut

	def replace(self):
		pass

	def cut_to_videos(self, cut_size):
		# cut_video_list = []
		# for cut in range(self._video.frames_count)[::cut_size]:
		# 	video = copy.deepcopy(self._video)
		# 	video.frames = self.frames[cut, cut + cut_size]
		# 	video.frames_count = video.frames.shape[0]
		# 	cut_video_list.append()
		# return videos
		return [
			self._frames[cut, cut + cut_size]
			for cut in range(self._frames.shape[0])[::cut_size]
		]

	@property
	def video(self):
		self._video.frames = self._frames
		return self._video
	
