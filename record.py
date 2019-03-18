try:
	from PIL import ImageGrab
except:
	import pyscreenshot as ImageGrab
import cv2
import numpy as np

import gui
import proc

class VideoRecorder:

	def __init__(self):
		pass

	def record(self, x, y, width, height, length=-1, fps=30):
		video_writer = proc.VideoEditor().create_video_writer('recorded', fps, width, height)
		window = gui.Window()
		window.running = True

		rec_sec = 0
		frames = 0
		while window.running:

			if rec_sec >= length:
				break

			grab = np.array(ImageGrab.grab(bbox=(x, y, width, height)))
			frame = cv2.cvtColor(grab, cv2.COLOR_BGR2RGB)

			video_writer.write(frame)

			frames += 1
			rec_sec = frames / fps

			print(f'Seconds : {round(rec_sec, 1)}')

			# window.show()