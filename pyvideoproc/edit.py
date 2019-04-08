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
	i = 0
	for frame in video.frames:
		print(frame.shape, i)
		i += 1
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

	@log("Cutting in range.")
	def cut_in_range(self, lower_color, upper_color, threshhold, places=None):
		frames = []
		for frame in self._video.frames:
			mask = cv2.inRange(frame, 
								np.array(lower_color), 
								np.array(upper_color))
			shape_of_matching_colors = np.argwhere(mask != 0).shape[0]
			mask_shape = mask.shape[0] * mask.shape[1]
			if shape_of_matching_colors / mask_shape >= threshhold:
				frames.append(frame)
		return np.array(frames)

	@property
	def video(self):
		return self._video

	@property
	def frames(self):
		return self._video.frames

	def __str__(self):
		return self._video.name
