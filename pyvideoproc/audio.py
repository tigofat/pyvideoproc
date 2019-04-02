import os

import subprocess

def combine_video_and_audio(output_name, path_to_video, path_to_audio):
	command = f'ffmpeg -i {path_to_video} -i {path_to_audio} -vcodec copy -acodec copy {output_name}.avi'
	subprocess.call(command, shell=True)

def get_audio(output_audio_name, path_to_video):
	command = f"ffmpeg -i {path_to_video} -ab 160k -ac 2 -ar 44100 -vn {output_audio_name}.wav"
	subprocess.call(command, shell=True)
