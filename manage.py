import pyvideoproc as vproc

vproc.add_videos('work/processed', 'videos', method='random', cut_size=25)

vproc.get_audio('work/audio', 'audio/movie.mp4')

vproc.combine_video_and_audio('work/combined', 'work/processed.avi', 'work/audio.wav')
