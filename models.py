import cv2

class Video:

	""" Video class is for string video related data. """

	def __init__(self, path):

		""" '__init__' function takes video path as param and stores its info using VideoCapture class. """

		self.path = path
		self.cap = cv2.VideoCapture(path)
		self.frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))