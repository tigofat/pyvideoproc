from .edit import VideoEditor, VideoProc, write
from .models import Video
from .manage import get_videos_from_dir

def add_videos(path, output_video_name, method='normal', cut_size=1):
	videos = get_videos_from_dir(path)
	video_editor = VideoEditor(videos[0])
	videos.pop(0)
	for video in videos:
		video_editor.add(video)
	if method == 'random': video_editor.shuffle(cut_size=cut_size)
	write(output_video_name, video_editor.video)
