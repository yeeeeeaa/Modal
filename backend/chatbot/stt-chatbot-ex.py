import os

credential_path="/home/pi/Labs/gongmojun-0cad85a2f781.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

from google.cloud import speech


if __name__=="__main__":
    os.system("sudo python stt-chatbot.py>textfile1-chatbot")
