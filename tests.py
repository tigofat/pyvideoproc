#!/usr/bin/env python3

import os
import time

import proc
from models import Video

print(f'Using {os.name} os.') ## Note that Mac OS is posix

video_editor = proc.VideoEditor()

# video_editor.add_videos_in_folder('processed', 'videos')

video = Video('videos/scooby.mp4')
video_editor.write('output', video * 3)

# videos = []
# path = "videos"
# for name in os.listdir(path):
#     if not name == '.DS_Store':
#     	videos.append(Video(f'{path}/{name}'))

# output = videos[-1]
# del videos[-1]
# for i in range(len(videos)):
# 	output += videos[i]

# video_editor.write('prcessed', output)