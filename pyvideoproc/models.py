import time

import cv2
import numpy as np
import copy
import time
from pathlib import Path

from .logger import log

class Video:

	def __init__(self, path):

		path_obj = Path(path)

		try:
			cap = cv2.VideoCapture(str(path_obj))
		except:
			raise Exception(f'{path} file does not exist.')

		self._name = path_obj.name
		self._width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self._height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self._fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.__load(cap)

	@log('Loading {}')
	def __load(self, cap):
		frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		self.frames = np.empty(frames_count, dtype=np.ndarray)
		for i in range(frames_count):
			ret, frame = cap.read()
			self.frames[i] = frame

	@log('Adding all to {}')
	def add_all(self, others):
		for other in others:
			self.add(other)

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

	def empty_frames(self):
		self.frames = np.empty(shape=self.frames[0].shape, dtype=np.ndarray)

	@property
	def name(self):
		return self._name
	
	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@property
	def fps(self):
		return self._fps

	@property
	def frames(self):
		return self._frames

	@name.setter
	def name(self, other):
		self._name = other

	@width.setter
	def width(self, other):
		self._width = other

	@height.setter
	def height(self, other):
		self._height = other

	@fps.setter
	def fps(self, other):
		self._fps = other

	@frames.setter
	def frames(self, other):
		self._frames = other

	def __str__(self):
		return self._name
