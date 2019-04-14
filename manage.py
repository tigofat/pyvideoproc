#!/usr/bin/env python3

import pyvideoproc as vproc

import cv2
import numpy as np

import time
import random

import pprint as pp
import copy

pprint = pp.PrettyPrinter().pprint

video = vproc.Video('pyvideoproc/videos/man.mp4', True)
video2 = vproc.Video('pyvideoproc/videos/scooby.mp4', True)
screen = vproc.Video('pyvideoproc/videos/screen.mp4', load=False)

video_editor = vproc.VideoProc(screen)

#cut_frames = video_editor.cut_to_videos(cut_size=40)

#random.shuffle(cut_frames)

#video.add_all(cut_frames)

lower_color = np.array([50, 0, 0])
upper_color = np.array([255, 255, 255])

#frames_in_range = video_editor.cut_in_range(lower_color, upper_color, 0.6)

#vproc.show(frames_in_range)

start = time.time()

#print(screen.frames.shape)

#screen.empty_frames()

#print(screen.frames.shape)

video.add(video2)

#video.resize_black(688, 1290)

#video.add(screen)

#print(video.frames.shape)

print(time.time() - start)

vproc.write('Processed.avi', video)
