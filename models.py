import time

import cv2
import numpy as np
import copy

class Video:

	""" Video class is for string video related data. """

	def __init__(self, path):

		""" '__init__' function takes video path as param and stores its info using VideoCapture class. """

		self.name = path.split('/')[-1]
		cap = cv2.VideoCapture(path)
		self.frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.read_frames_count = self.frames_count

		self.__load(cap)

	def __load(self, cap):
		self.frames = np.empty(self.frames_count, dtype=np.ndarray)
		for i in range(self.frames_count):
			ret, frame = cap.read()
			self.frames[i] = frame

	def cut(self, places):
		video = copy.deepcopy(self)
		video.name = 'cut'
		video.frames = self.frames[places[0]:places[1]]
		video.frames_count = video.frames.shape[0]
		return video

	def __add__(self, other):
		video = copy.deepcopy(self)
		video.name = 'combined'
		video.frames = np.hstack((video.frames, other.frames))
		video.frames_count += other.frames.shape[0]
		return video

	def __mul__(self, number):
		if type(number) != int:
			raise Exception("Multiplier must be of type 'int'.")

		video = copy.deepcopy(self)
		original_video_frames = video.frames
		original_video_frames_count = video.frames_count
		video.name = 'repeated'
		for i in range(1, number):
			video.frames = np.hstack((video.fram1es, original_video_frames))
			video.frames_count += original_video_frames_count
			video.read_frames_count = video.frames_count

		return video