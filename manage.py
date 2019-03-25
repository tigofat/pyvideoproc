import os
from models import Video

def get_videos_from_dir(path):
    return [
    	Video(f'{path}/{name}') 
    	for name in os.listdir(path) if not name == '.DS_Store'
    ]