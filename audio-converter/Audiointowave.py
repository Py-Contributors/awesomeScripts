# import required modules 

from os import path 

from pydub import AudioSegment 

  
# assign files 

input_file = "hello.mp3"

output_file = "result.wav"

  
# convert mp3 file to wav file 

sound = AudioSegment.from_mp3(input_file) 

sound.export(output_file, format="wav") 
