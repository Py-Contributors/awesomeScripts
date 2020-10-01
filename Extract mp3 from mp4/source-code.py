import moviepy
video = moviepy.editor.VideoFilePath("")#Give the path of the the required file
audio=video.audio 
audio.write_audiofile('1.mp3')#give the name of desired mp3
