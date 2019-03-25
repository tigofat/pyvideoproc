import os
from models import Video

def get_videos_from_dir(path):
        # videos = []
        # for name in os.listdir(path):
        #     if not name == '.DS_Store':
        #         videos.append(Video(f'{path}/{name}'))
        # return videos
    return [
    	Video(f'{path}/{name}') 
    	for name in os.listdir(path) if not name == '.DS_Store'
    ]