import pyaudio
import wave
import time
import os

credential_path="/home/pi/Labs/gongmojun-0cad85a2f781.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

import sys



SAMPLE_RATE=44100
FORMAT=pyaudio.paInt16
CHANNELS=1
CHUNK=512
RECORD_SECONDS=5
WAVE_OUTPUT_FILENAME="output-chatbot.wav"

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

#print("녹음을 시작합니다 :)")

stream.start_stream()

cnt=0
while stream.is_active():
    time.sleep(0.1)
    cnt+=1
    if cnt > RECORD_SECONDS*10:
        break
#print("녹음 끝!")

stream.stop_stream()
stream.close()
p.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(SAMPLE_RATE)
wf.writeframes(b''.join(frames))


def run_quickstart():
    import io

    from google.cloud import speech


  
    client=speech.SpeechClient()

    file_name=os.path.join(os.path.dirname(__file__),".","output-chatbot.wav")

    with io.open(file_name,"rb") as audio_file:
        content=audio_file.read()
        audio=speech.RecognitionAudio(content=content)

        config=speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="ko-KR",
            )

        response=client.recognize(config=config, audio=audio)

        for result in response.results:
            print(result.alternatives[0].transcript)

if __name__=="__main__":
    run_quickstart()
    os.system("sudo touch textfile1-chatbot")
    
