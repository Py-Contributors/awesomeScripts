import pyaudio
import wave

chunk = 1024

sample_format = pyaudio.paInt16
chanels = 2

smpl_rt = 44400
seconds = 4
filename = "path_of_file.wav"

pa = pyaudio.PyAudio()

stream = pa.open(format=sample_format, channels=chanels,
				rate=smpl_rt, input=True,
				frames_per_buffer=chunk)

print('Recording...')


frames = []
for i in range(0, int(smpl_rt / chunk * seconds)):
	data = stream.read(chunk)
	frames.append(data)

 
stream.stop_stream()
stream.close()

pa.terminate()

print('Done !!! ')
sf = wave.open(filename, 'wb')
sf.setnchannels(chanels)
sf.setsampwidth(pa.get_sample_size(sample_format))
sf.setframerate(smpl_rt)
sf.writeframes(b''.join(frames))
sf.close()
