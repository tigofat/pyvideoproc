import cv2
from .logger import log

def create_video_writer(output_video_name, fps, width, height):
	fourcc = cv2.VideoWriter_fourcc(*'MJPG')
	return cv2.VideoWriter(f'{output_video_name}', fourcc, fps, (width, height))

@log('Writing video "{}".')
def write(output_video_name, video):
	video_writer = create_video_writer(output_video_name, video.fps, 
		video.width, video.height)
	for frame in video.frames:
		video_writer.write(frame)
