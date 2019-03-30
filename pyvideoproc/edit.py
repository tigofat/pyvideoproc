import time
import os
import random
from copy import deepcopy

import cv2
import numpy as np
import pprint as pp

from .models import Video

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
	
	def __init__(self, video):
		self._video = video
		self._frames = video.frames

	def to_gray(self):
		self._frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) for frame in self._frames]
		#self._frames = cv2.cvtColor(self._frames, cv2.COLOR_BGR2GRAY)

	@property
	def video(self):
		self._video.frames = self._frames
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

	def cut_to_videos(self, cut_size):
		return [
			self._frames[cut_size * i : cut_size * i + cut_size]
			for i in range(self._frames.shape[0] // cut_size - 1)
		]

	def shuffle(self, cut_size):
		frames = self.cut_to_videos(cut_size)
		random.shuffle(frames)
		self._frames = np.empty(shape=0, dtype=np.ndarray)
		for frame in frames:
			self._frames = np.hstack((self._frames, frame))

	@property
	def video(self):
		self._video.frames = self._frames
		return self._video
