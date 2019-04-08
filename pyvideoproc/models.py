import cv2
import numpy as np
import copy
import time
import logging
from pathlib import Path

from .logger import log

class Video:

	def __init__(self, path):

		path_obj = Path(path)

		try:
			cap = cv2.VideoCapture(str(path_obj))
			self.cap = cap
		except:
			raise Exception(f'{path} file does not exist.')

		self._name = path_obj.name
		self._width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self._height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self._fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.__load(cap)

	@log('Loading {}.')
	def __load(self, cap):
		frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		frames = []
		for i in range(frames_count):
			ret, frame = cap.read()
			frames.append(frame)

		self.__store_frames(frames, 6)

	@log('Storing frames of {}.')
	def __store_frames(self, frames, cut_size=2):
		cut = len(frames)//cut_size
		try:
			self._frames = np.array(frames[:cut], dtype=np.uint8)
			for c in range(cut, len(frames))[::cut]:
				self._frames = np.concatenate((self._frames, frames[c:c + cut]))
		except MemoryError:
			logging.warning(f'Memory Error has occured while loading {self._name}, ')
			self.__load_slowely(frames, 7)

	@log('Adding frame to {}.')
	def add_frame(self, frame):
		self.frames = np.concatenate((self.frames, np.array([frame])))

	@log('Adding video to {}.')
	def add(self, other):
		frames = other.frames if isinstance(other, Video) else other
		#print(self.frames.shape)
		#print(frames.shape)
		self.frames = np.concatenate((self.frames, frames))

	@log('Repeating {}.')
	def rep(self, times):
		original_frames = self.frames
		for i in range(1, times):
			self.frames = np.hstack((self.frames, original_frames))

	@log('Cutting {}.')
	def cut(self, places):
		self.frames = np.hstack((self.frames[:places[0]], 
								self.frames[places[1]:]))
		return self.frames[places[0]:places[1]]

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
