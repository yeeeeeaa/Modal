import json
import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import time
from datetime import datetime

ref = db.reference('김철수')


day = []
total_day = [0]*31
list_day = 0

ai_data = [[l] for l in zip(df)]
ai_train_day = list(range(len(ai_data)))
ai_day = list(range(len(ai_data)))

result_day = ["0"]

for i in range (len(ai_data)):
    target = str(ai_data[i])
    start = target.find('21') + 4
    finish = target.rfind(')') - 2
    ai_train_day[i] = target[start:finish]
    start = target.find('21')
    finish = target.rfind(')') - 2
    ai_data[i] = target[start:finish]
    for k in range (31):
        if len(str(k)) == 1:
            k = "0" + str(k)
        day.append(ai_train_day[i].count(str(k)))
    total_day = [total_day[j] + day[j] for j in range(31)]
    day = []
for k in range (31):
    if total_day[k] >= 4:
        result_day = str(total_day.index(total_day[k]))
day_index = [i for i in range(len(ai_train_day)) if result_day in ai_train_day[i]]
users_ref = str(ref.child(df.columns[int(day_index[0])]).get())
d = datetime.now()
month = str(d.month) + "월 "
start = users_ref.find('내용') + 9
finish = users_ref.find('}') - 1
said = month + users_ref[start:finish] + " 일정을 추가해드릴까요?"
print(said)