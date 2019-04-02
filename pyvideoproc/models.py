import time

import cv2
import numpy as np
import copy
import time
from pathlib import Path

from .logger import log

name = 'bitch'

class Video:

	def __init__(self, path):

		path_obj = Path(path)

		try:
			cap = cv2.VideoCapture(str(path_obj))
		except:
			raise Exception(f'{path} file does not exist.')

		self.name = path_obj.name
		self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.__load(cap)

	@log('Loading {}')
	def __load(self, cap):
		frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		self.frames = np.empty(frames_count, dtype=np.ndarray)
		for i in range(frames_count):
			ret, frame = cap.read()
			self.frames[i] = frame

	@log('Adding video to {}')
	def add(self, other):
		frames = other.frames if isinstance(other, Video) else other
		self.frames = np.hstack((self.frames, frames))

	@log('Repeating {}')
	def rep(self, times):
		original_frames = self.frames
		for i in range(1, times):
			self.frames = np.hstack((self.frames, original_frames))

	@log('Cutting {}')
	def cut(self, places):
		self.frames = np.hstack((self.frames[:places[0]], 
								self.frames[places[1]:]))
		return self.frames[places[0]:places[1]]

	def __str__(self):
		return self.name
