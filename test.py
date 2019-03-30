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
		self.cap = cv2.VideoCapture(path)
		# self.frames_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
		# self.width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		# self.height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		# self.fps = int(cap.get(cv2.CAP_PROP_FPS))

		self.loaded = True


def my_logger(orig_func):

	def wrapper_logger(*args, **kwargs):
		print(f'{orig_func.__name__} logger: Run with args {args} and kwargs {kwargs}.')
		return orig_func(*args, **kwargs)

	return wrapper_logger

def my_timer(orig_func):

	def wrapper_timer(*args, **kwargs):
		start = time.time()
		result = orig_func(*args, **kwargs)
		print(f'{orig_func.__name__} run in {time.time() - start} seconds.')
		return result

	return wrapper_timer

@my_timer
@my_logger
def display_info(name, age):
	time.sleep(0.5)
	print(f'display_info prints: {name} and {age}')

# display_info('Tigran', 18)

from itertools import accumulate

l = [1, 2, 3]

from functools import partial

def cal(prices, callback):
	return callback(sum(prices))

#price_log = partial(print, 'The total proce is')
#cal([1, 2, 3, 4, 5], price_log)

import logging
import logging.config

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#logging.debug('This is an error message.')
#logging.info('This is an error message.')
#logging.warning('This is an error message.')
#logging.error('This is an error message.')
#logging.critical('This is an error message.')

try:
	c = 10 / 1
except:
	## logging.error('Exception occurred', exc_info=True) as same as
	logging.exception('Exception occurred')

#logging.config.fileConfig(fname='file.conf', disable_existing_loggers=False)

#logger = logging.getLogger(__name__)

#logger.warning('This is supposted to be an error, but it is not.')

#c_handler = logging.StreamHandler()
#f_handler = logging.FileHandler('file.log')
#c_handler.setLevel(logging.WARNING)
#f_handler.setLevel(logging.ERROR)

#c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#c_handler.setFormatter(c_format)
#f_handler.setFormatter(f_format)

#logger.addHandler(c_handler)
#logger.addHandler(f_handler)

#logger.warning('This is a warring.')
#logger.error('This is an error')

import subprocess
command = "ffmpeg -i videos/man.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav"
subprocess.call(command, shell=True)
