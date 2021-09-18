import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("/home/pi/speech/modal-dbe5e-firebase-adminsdk-k64o9-bf81f0cd3a.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://modal-dbe5e-default-rtdb.firebaseio.com/'})

ref = db.reference('김철수')
row = str(ref.get())

credential_path="/home/pi/speech/speech-test-318806-3ae95ccff5d1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

from google.cloud import speech
global target
global said


def target_text() :
    file_text = open('textfile1.txt', 'r').read().split('\n')
    target = file_text[2].replace("Transcript: ","")
    print(target)
    
    return target

def day_add(target):
    dDay=month_day(target)
    month=month_day(target)
    day=month_day(target)
    print(dDay)
    if '추가' in target:
        r=open('textfile1.txt',mode='rt',encoding='utf-8')
        users_ref=ref.child(dDay)
        users_ref.set({
            '축구하기':{
                    '내용':r.read(100)
                        }
        })
            
def day_check(target):
    dDay = month_day(target)
    users_ref = str(ref.child(dDay).get())
    start = users_ref.find('내용') + 6
    finish = users_ref.find('}') - 1
    schedule = users_ref[start:finish] + "이 있습니다."
    run_quickstart(schedule)

def day_change(target):
    if '변경' in target:
        if '월요일' in target:
            start = target.find('월요일에') + 5
            finish = target.rfind('추가')
            day_work = target[start:finish]
        
def day_delete(target):
    dDay = month_day(target)
    print(dDay)
    users_ref = str(ref.child(dDay).get())
    print(users_ref)
    start = users_ref.find('내용') + 6
    finish = users_ref.find('}') - 1
    schedule = users_ref[start:finish] + " 일정이 삭제되었습니다."
    ref.child(dDay).delete()
    print("확인해보자")
    run_quickstart(schedule)

    """
            if dDay in row:
                start = target.find('일') + 2
                finish = target.rfind('일') - 2
                delete_day = target[start:finish]
                print(delete_day)
            
                users_ref = ref.child(dDay).get()
                users_ref.child(delete_day).remove()
                schedule = delete_day + " 일정이 삭제되었습니다."
                run_quickstart(schedule)
                """
                
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

if __name__=="__main__":
    global target
    target = ""
    ask = 1
    while(ask):
        os.system("sudo python stt_add.py>textfile1.txt")
        target = target_text()
        
        if '호출' in target:
            print('부르셨나요')
        if '추가' in target:
            day_add(target)
        if '확인' in target:
            day_check(target)
            ask = 0
        if '변경' in target:
            day_change(target)
        if '삭제' in target:
            day_delete(target)
            ask = 0
    
    os.system("aplay output.wav")
    print('sucess')
        

        
        
    '''if '추가' in target:
        day_add(target)
    else if '확인' in target:
        day_change(target)
    else if '삭제' or '수정' in target:
        day_change(target)'''
        