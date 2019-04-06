import pyvideoproc as vproc

import cv2
import numpy as np

video = vproc.Video('pyvideoproc/videos/alo.mp4')

video_editor = vproc.VideoProc(video)

lower_color = np.array([0, 0, 0])
upper_color = np.array([50, 255, 255])

#for frame in video.frames:
#	res = cv2.inRange(frame, lower_color, upper_color)
#	cv2.imshow('res', res)
	#cv2.imshow('frame', frame)
#	if cv2.waitKey(27) & 0xFF == ord('q'):
#		break

video_editor.cut_in_range(lower_color, upper_color, 0.7)
#video_editor.cut_in_range([0, 0, 0], [255, 255, 255])

vproc.write('Processed', video_editor.video)

#vproc.add_videos('processed', 'pyvideoproc/videos', method='random', cut_size=25)

#videos = vproc.get_videos_from_dir('pyvideoproc/videos')

#videos[0].add(videos[1])

#vproc.write('output', videos[0])
