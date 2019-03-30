import time

import cv2
import numpy as np
import copy
import time

class Video:

	""" Video class is for string video related data. """

	def __init__(self, path=''):

		""" '__init__' function takes video path as param and stores its info using VideoCapture class. """

		try:
			self.cap = cv2.VideoCapture(path)
		except:
			return

		self.path = path
		self.name = path.split('/')[-1]
		self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

		self.load()

	def load(self):
		frames_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

		self.frames = np.empty(frames_count, dtype=np.ndarray)
		for i in range(frames_count):
			ret, frame = self.cap.read()
			self.frames[i] = frame

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