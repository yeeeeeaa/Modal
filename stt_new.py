import os

credential_path="/home/pi/speech/speech-test-318806-3ae95ccff5d1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

from google.cloud import speech


if __name__=="__main__":
    os.system("sudo python stt_add.py>textfile1")