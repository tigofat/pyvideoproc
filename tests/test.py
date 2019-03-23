""" Please don't pay attention to this file, it is for a quick tests and experiments! """

import cv2
import numpy as np
from copy import deepcopy
import time
import pprint as p

pprint = p.PrettyPrinter().pprint

class Video:

	""" Video class is for string video related data. """

	def __init__(self, path):

		""" '__init__' function takes video path as param and stores its info using VideoCapture class. """

		self.name = path.split('/')[-1]
		cap = cv2.VideoCapture(path)
		# self.frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		# self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		# self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		# self.fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.loaded = True

video = Video('videos/scooby.mp4')
# print(deepcopy(video))
# arr = np.random.rand(10000000)

# start_time = time.time()
# a = arr
# print(time.time() - start_time)

np.random.seed(0)

a = np.random.rand(200)

d = deepcopy(a)

b = np.random.rand(100)

# c = np.empty(shape=a.shape[0] + b.shape[0])
# print(c.shape)

start_time = time.time()
for i in range(10000):
	d = np.hstack(b)
	# for i in range(b.shape[0]):
	# 	# c[i] = 
	# 	pass
	# a = np.append(a, b)

print(a)
print(d)
print(time.time() - start_time)

