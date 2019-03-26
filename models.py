import time

import cv2
import numpy as np
import copy
import time

class Video:

	def __init__(self, path=''):

		try:
			cap = cv2.VideoCapture(path)
		except:
			return

		self.path = path
		self.name = path.split('/')[-1]
		self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.__load(cap)

	def __load(self, cap):
		frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

		self.frames = np.empty(frames_count, dtype=np.ndarray)
		for i in range(frames_count):
			ret, frame = cap.read()
			self.frames[i] = frame

	def add(self, other):
		frames = other.frames if isinstance(other, Video) else other
		self.frames = np.hstack((self.frames, frames))

	def mul(self, times):
		original_frames = self.frames
		for ii in range(1, times):
			self.frames = np.hstack((self.frames, original_frames))

	def cut(self, places):
		self.frames = np.hstack((self.frames[:places[0]], 
								self.frames[places[1]:]))
		return self.frames[places[0]:places[1]]

		## It is also possible to use list comprehensions, but performance is slower in this case.
		## self.frames = np.array([cap.read()[1] for i in range(frames_count)])
	
	# @classmethod
	# def instance():

	# def cut(self, places):
	# 	video = copy.deepcopy(self)
	# 	video.name = 'cut'
	# 	video.frames = self.frames[places[0]:places[1]]
	# 	video.frames_count = video.frames.shape[0]
	# 	return video

	# def __add__(self, other):
	# 	video = copy.deepcopy(self)
	# 	video.name = 'combined'
	# 	video.frames = 
	# 	video.frames_count += other.frames_count
	# 	return video

	# def __mul__(self, number):
	# 	if type(number) != int:
	# 		raise Exception("Multiplier must be of type 'int'.")

	# 	video = copy.deepcopy(self)
	# 	original_video_frames = video.frames
	# 	original_video_frames_count = video.frames_count
	# 	video.name = 'repeated'
	# 	for i in range(1, number):
	# 		video.frames = np.hstack((video.frames, original_video_frames))
	# 		video.frames_count += original_video_frames_count
	# 		video.read_frames_count = video.frames_count

	# 	return videox
