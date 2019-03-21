#!/usr/bin/env python3

import os
import time

import proc
from models import Video

print(f'Using {os.name} os.') ## Note that Mac OS is posix

""" Init VideoEditor object. """
video_editor = proc.VideoEditor()

video_editor.add_videos_from_dir('processed', 'videos', method='random', cut_size=20)

# or

# videos = []
# for name in os.listdir('videos'):
#     if not name == '.DS_Store':
#         videos.append(Video(f'videos/{name}'))

# video_editor.add_videos('processed', videos, method='random', cut_size=24)
