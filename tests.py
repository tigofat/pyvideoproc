#!/usr/bin/env python3

from os import listdir

import proc
from models import Video

video_editor = proc.VideoEditor()

videos = []
path = "videos"
for name in listdir(path):
    if not name == 'DS.Store':
        videos.append(Video(f'{path}/{name}'))

video_editor.add_videos('output', videos)