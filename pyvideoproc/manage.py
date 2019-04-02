from pathlib import Path

from .models import Video

def get_videos_from_dir(path):
    return [
   		Video(f'{p}')
    	for p in Path(path).iterdir() if p.is_file()
	]

