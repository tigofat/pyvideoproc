import cv2
import numpy as np

class Video:

	""" Video class is for string video related data. """

	def __init__(self, path):

		""" '__init__' function takes video path as param and stores its info using VideoCapture class. """

		self.cap = cv2.VideoCapture(path)
		self.frames_count = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))

		self.load()

	def load(self):
		self.frames = np.empty(self.frames_count, dtype=np.ndarray)
		for i in range(self.frames_count):
			ret, frame = self.cap.read()
			self.frames[i] = frame

	def __add__(self, other):
		video = self
		video.frames = np.hstack((self.frames, other.frames))
		video.frames_count = video.frames.shape[0]
		return video