import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/pi/speech/modal-dbe5e-firebase-adminsdk-k64o9-bf81f0cd3a.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://modal-dbe5e-default-rtdb.firebaseio.com/'})

credential_path="/home/pi/speech/modal-324900-dadc152185c5.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

ref = db.reference('김철수')
row = str(ref.get())

import schedule
import time
from datetime import datetime

from google.cloud import speech
global target
global emotion

def target_text() :
    file_text = open('textfile1.txt', 'r').read().split('\n')
    target = file_text[2].replace("Transcript: ","")
    print(target)
    
    return target

def day_add(target, change):
    dDay=month_day(target)
    start = target.find('일') + 1
    target_summarize=target[start:]
    print(dDay)
    users_ref=ref.child(dDay)
    users_ref.update({
        target_summarize:{
            '내용':target
           }
    })
    if change == 1:
        run_quickstart(target_summarize+"일정으로 변경되었습니다.")
        return 0
    else:
        run_quickstart(target_summarize+"일정이 추가되었습니다.")
        return 0
            
def day_check(target):
    dDay = month_day(target)
    users_ref = str(ref.child(dDay).get())
    print(users_ref)
    if users_ref == "None":
        run_quickstart("해당 날짜에는 일정이 존재하지 않습니다")
    elif users_ref != "None":
        start = users_ref.find('내용') + 6
        finish = users_ref.find('}') - 1
        said = users_ref[start:finish] + "일정이 있습니다."
        run_quickstart(said)
    

def day_change(target):
    dDay = month_day(target)
    users_ref = str(ref.child(dDay).get())
    if users_ref == "None":
        run_quickstart("해당 날짜에는 일정이 존재하지 않습니다")
        return 0
    elif users_ref != "None":
        day_delete(target, 1)
        run_quickstart("변경하고 싶은 일정을 말해주세요")
    return 1
        
        
def day_delete(target, change):
    dDay = month_day(target)
    print(dDay)
    users_ref = str(ref.child(dDay).get())
    if users_ref == "None":
        run_quickstart("해당 날짜에는 일정이 존재하지 않습니다")
    elif users_ref != "None":
        start = users_ref.find('내용') + 6
        finish = users_ref.find('}') - 1
        if change == 0:
            said = users_ref[start:finish] + " 일정이 삭제되었습니다."
            ref.child(dDay).delete()
            run_quickstart(said)
        elif change == 1:
            ref.child(dDay).delete()
                
def month_day(target):
    finish = target.rfind('월')
    month = target[0:finish]
    start = target.find('월') + 2
    finish = target.find('일')
    day = target[start:finish]
    if len(month) == 1:
        month = '0'+month
    if len(day) == 1:
        day = '0'+day
    dDay = '21'+month+day
    return dDay

def mood_add(emoji):
    d = datetime.now()
    month = str(d.month)
    day = str(d.day)
    if len(month) == 1:
        month = '0'+month
    if len(day) == 1:
        day = '0'+day
    dDay = '21'+month+day
    ref.child(dDay).set({'감정' : emoji})
        
def run_quickstart(tts_text):
    # [START tts_quickstart]
    """Synthesizes speech from the input string of text or ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/
    """
    from google.cloud import texttospeech

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text = tts_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    with open("output.wav", "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.wav"')
    # [END tts_quickstart]
    os.system("aplay output.wav")

def time_job_emotion():
    global emotion
    d = datetime.now()
    hour = d.hour
    minute = d.minute
    if hour == 10 and minute == 28 and emotion:
        run_quickstart("오늘의 기분은 어떠신가요?")
        return False
    elif hour != 10 or minute != 28 :
        return True
    
def time_job_check():
    global today
    d = datetime.now()
    hour = d.hour
    minute = d.minute
    if hour == 6 and minute == 14 and today:
        month = str(d.month) + "월 "
        day = str(d.day) + "일"
        print(month+day)
        day_check(month+day)
        return False
    elif hour != 6 or minute != 14 :
        return True
    
def advice(target):
    run_quickstart("저희가 지원하는 기능에는 일정 확인, 추가, 변경, 삭제가 있습니다.")
    run_quickstart("9월 29일 일정 추가")
    run_quickstart("처럼 원하시는 날짜와 함께 네 가지 기능 중 원하는 기능을 말씀해주세요")
    
def ai_train():
    global ai
    d = datetime.now()
    day = d.day
    nowTime = d.strftime('%H.%M')
    print(nowTime)
    if day == 7 and nowTime == "23.06" and ai:
        os.system("sudo python ai.py>day_return.txt")
        with open('day_return.txt', 'r') as file:
            b = file.readline()
        print(b)
        run_quickstart(b)
        return False
    elif nowTime != "23.06":
        return True
        

if __name__=="__main__":
    global target
    global emotion
    global today
    global ai
    ai = True
    emotion = True
    change = 0
    add = 0
    target = ""
    
    while True:
        if change == 0:
            emotion = time_job_emotion()
            today = time_job_check()
            ai = ai_train()
        
        os.system("sudo python stt_add.py>textfile1.txt")
        target = target_text()
        
        if change == 1:
            change = day_add(target, 1)
        elif add == 1:
            add = day_add(target, 0)
        
        if '호출' in target:
            print('부르셨나요')
        elif '추가' in target:
            run_quickstart("추가하고 싶은 일정을 말해 주세요")
            add = 1
        elif '확인' in target:
            day_check(target)
        elif '변경' in target:
            change = day_change(target)
        elif '삭제' in target:
            day_delete(target, 0)
        elif '도움말' in target:
            advice(target)
            
            
        if emotion == False:
            if '행복' in target:
                mood_add('행복')
            elif '신남' in target:
                mood_add('신남')
            elif '평범' in target:
                mood_add('평범')
            elif '슬픔' in target:
                mood_add('슬픔')
            elif '우울' in target:
                mood_add('우울')
            elif '분노' in target:
                mood_add('분노')
    
    print('sucess')
        

        
        
    '''if '추가' in target:
        day_add(target)
    else if '확인' in target:
        day_change(target)
    else if '삭제' or '수정' in target:
        day_change(target)'''
        