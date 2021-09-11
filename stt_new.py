import os


credential_path="/home/pi/speech/speech-test-318806-3ae95ccff5d1.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

from google.cloud import speech
global target


def target_text() :
    file_text = open('textfile1.txt', 'r').read().split('\n')
    target = file_text[2].replace("Transcript: ","")
    print(target)
    
    return target

def day_add(target):
    if '추가' in target:
        if '일요일' in target:
            start = target.find('일요일에') + 5
            finish = target.rfind('추가')
            day_work = target[start:finish]
            
def day_check(target):
    if '월' in target:
        finish = target.rfind('월')
        month = target[0:finish]
        if '일' in target:
            start = target.find('월') + 2
            finish = target.rfind('일') - 2
            day = target[start:finish]
            if len(month) == 1:
                month = '0'+month
            if len(day) == 1:
                day = '0'+day
            dDay = '21'+month+day
            print(dDay)

def day_change(target):
    if '변경' in target:
        if '월요일' in target:
            start = target.find('월요일에') + 5
            finish = target.rfind('추가')
            day_work = target[start:finish]
            
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
    print('sucess')
        

        
        
    '''if '??' in target:
        day_add(target)
    else if '??' in target:
        day_change(target)
    else if '??' or '??' in target:
        day_change(target)'''
        
