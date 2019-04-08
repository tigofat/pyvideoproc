#!/usr/bin/env python3

import pyvideoproc as vproc

import numpy as np

import time
import random

import pprint as pp

pprint = pp.PrettyPrinter().pprint

video = vproc.Video('pyvideoproc/videos/man.mp4')
video2 = vproc.Video('pyvideoproc/videos/scooby.mp4')

video_editor = vproc.VideoProc(video)

#cut_frames = video_editor.cut_to_videos(cut_size=40)

#random.shuffle(cut_frames)

#video.add_all(cut_frames)

lower_color = np.array([50, 0, 0])
upper_color = np.array([205, 255, 255])

frames_in_range = video_editor.cut_in_range(lower_color, upper_color, 0.6)

start = time.time()

#video.add(video2)

#video.cut((200, 300))

pprint(frames_in_range[0])
print('Frames')
pprint(video.frames[0])

video.add_all(frames_in_range)

#print(video.frames.shape)

#print(time.time() - start)

vproc.write('Processed', video)
