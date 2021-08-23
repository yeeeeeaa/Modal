import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=\
                                               "/home/pi/Labs/gongmojun-0cad85a2f781.json"

from google.cloud import speech

RATE=44100
CHUNK=int(RATE/10)

if __name__=="__main__":
    os.system("sudo python3 stt-chatbot-ex.py")


language_code='ko-KR'

f=open('textfile1-chatbot','r')
mystring=f.read()

if mystring=="안녕하세요":
    os.system("aplay hello.wav")
else:
    print("what?!")
    
print(mystring)

