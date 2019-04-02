import time
import os
import random
from copy import deepcopy

import cv2
import numpy as np
import pprint as pp

from .models import Video
from .logger import log

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

	@log("Cutting {} to videos")
	def cut_to_videos(self, cut_size):
		return [
			self._video.frames[cut_size * i : cut_size * i + cut_size]
			for i in range(self._video.frames.shape[0] // cut_size - 1)
		]

	@log("Shuffling and adding cut videos together from {}")
	def shuffle(self, frames):
		random.shuffle(frames)
		self._video.frames = np.empty(shape=0, dtype=np.ndarray)
		for frame in frames:
			self._video.frames = np.hstack((self._video.frames, frame))

	@property
	def video(self):
		return self._video

	def __str__(self):
		return self._video.name
