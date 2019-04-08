# __all__ = ['proc', 'edit', 'models']

import logging

from .edit import VideoProc
from .writer import write
from .models import Video
from .audio import get_audio, combine_video_and_audio
from .manage import get_videos_from_dir

logging.basicConfig(format='%(asctime)s: %(message)s', level=logging.DEBUG)
