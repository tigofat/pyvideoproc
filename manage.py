import pyvideoproc as vproc

vproc.add_videos('processed', 'pyvideoproc/videos', method='random', cut_size=25)

#videos = vproc.get_videos_from_dir('pyvideoproc/videos')

#videos[0].add(videos[1])

#vproc.write('output', videos[0])
