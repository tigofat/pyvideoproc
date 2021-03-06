import cv2
import numpy as np
import copy
import time
import logging
from pathlib import Path

from .logger import log

class Video:

	def __init__(self, path, load=True):
		self.path = Path(path)
		self.name = self.path.name
		if load: self.load()

	@log('Loading {}.')
	def load(self):

		try:
			cap = cv2.VideoCapture(str(self.path))
		except:
			raise Exception(f'{path} file does not exist.')

		self._width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self._height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self._fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.__store_frames(cap)

	@log('Storing frames of {}.')
	def __store_frames(self, cap):
		frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		frames = []
		for i in range(frames_count):
			ret, frame = cap.read()
			frames.append(frame)
		try:
			# Note that this operation will consume a lot of memory and CPU, so consider using a strog computer to lead bigger videos
			self._frames = np.array(frames, dtype=np.uint8)
		except MemoryError:
			raise Exception(f'WARNING: Memory Error has occured while loading {self._name}.')

	@log('Adding frame to {}.')
	def add_frame(self, frame):
		self.frames = np.concatenate((self.frames, np.array([frame])))

	@log('Adding video to {}.')
	def add(self, other):
		frames = other.frames if isinstance(other, Video) else other
		#print(self.frames.shapei)
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

	@log('Resizing {}')
	def resize_black(self, height, width):
		pass

	@log('Resizing {}.')
	def resize(self, width, height, background):
		pass

	@log('Emptying frames of {}.')
	def empty_frames(self):
		self.frames = np.empty(shape=0, dtype=np.uint8)

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
