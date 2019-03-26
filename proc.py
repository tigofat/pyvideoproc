from .edit import write, VideoProc
from .manage import get_videos_from_dir
from .models import Video

def get_videos(source):
	return (
		get_videos_from_dir(source) if type(source) == str
		else source
	)

def add_videos(video_source, output_video_name, method='normal', cut_size=25):
	videos = get_videos(video_source)
	video = videos.pop(0)
	for vid in videos:
		video.add(vid)
	video_proc = VideoProc(video)
	if method == 'random': video_proc.shuffle(cut_size=cut_size)
	write(output_video_name, video_proc.video)
