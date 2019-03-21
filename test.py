""" Please don't pay attention to this file, it is for a quick tests and experiments! """

import cv2
import numpy as np
from copy import deepcopy
import time

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

		self.loaded = True

# video = Video('videos/scooby.mp4')

arr = np.random.rand(10000000)

start_time = time.time()
a = arr
print(time.time() - start_time)