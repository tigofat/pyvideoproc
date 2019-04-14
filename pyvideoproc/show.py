import cv2
from .logger import log

@log('Showing.')
def show(frames):
	for frame in frames:
		cv2.imshow('frame', frame)
		if cv2.waitKey(27) & 0xFF == ord('q'):
			break
