#!/usr/bin/env python3

import os
import time

import proc
from models import Video

print(f'Using {os.name} os.') ## Note that Mac OS is posix

video_editor = proc.VideoEditor()

videos = []
path = "videos"
for name in os.listdir(path):
    if not name == '.DS_Store':
    	videos.append(Video(f'{path}/{name}'))

video1 = Video('videos/man.mp4')
video2 = Video('videos/scooby.mp4')

output = video1 + video2

video_editor.write('prcessed', output)