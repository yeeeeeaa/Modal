                
                import pyaudio
import wave
import time

SAMPLE_RATE=44100
FORMAT=pyaudio.paInt16
CHANNELS=1
CHUNK=512
RECORD_SECONDS=5
WAVE_OUTPUT_FILENAME="output.wav"

p=pyaudio.PyAudio()

frames=[]

def callback(in_data, frame_count, time_info, status):
    frames.append(in_data)
    return(None, pyaudio.paContinue)

stream=p.open(format=FORMAT,
              channels=CHANNELS,
              rate=SAMPLE_RATE,
              input=True,
              frames_per_buffer=CHUNK,
              stream_callback=callback)

print("녹음을 시작합니다 :)")

stream.start_stream()

cnt=0
while stream.is_active():
    time.sleep(0.1)
    cnt+=1
    if cnt > RECORD_SECONDS*10:
        break
print("녹음 끝!")

stream.stop_stream()
stream.close()
p.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b''.join(frames))
