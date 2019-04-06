import pyvideoproc as vproc

import numpy as np
import time

import random

video = vproc.Video('pyvideoproc/videos/screen.mp4')

video_editor = vproc.VideoProc(video)

start = time.time()
#cut_frames = video_editor.cut_to_videos(cut_size=40)

#random.shuffle(cut_frames)

#video.add_all(cut_frames)

lower_color = np.array([0, 0, 0])
upper_color = np.array([50, 255, 255])

frames_in_range = video_editor.cut_in_range(lower_color, upper_color, 0.6)

video.empty_frames()

video.add(frames_in_range)

vproc.write('Processed', video)
