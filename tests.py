#!/usr/bin/env python3

import os
import time

import proc
import edit
import manage
from models import Video

print(f'Using {os.name} os.') ## Note that Mac OS is posix

videos = manage.get_videos_from_dir('videos')

video_editor = edit.VideoEditor(videos[0])
videos.pop(0)

for video in videos:
	video_editor.add(video.frames)

video_editor.cut_to_videos()

edit.write('processed', video_editor.video)

# or

# videos = []
# for name in os.listdir('videos'):
    # if not name == '.DS_Store':
#         videos.append(Video(f'videos/{name}'))

# video_editor.add_videos('processed', videos, method='random', cut_size=24)
