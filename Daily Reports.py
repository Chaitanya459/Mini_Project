
import matplotlib.pyplot as plt

import time

import pandas as pd

import schedule

def job():
    df = pd.read_csv("FinalAttendance.csv", header=None)
    df.head()
    dicto = {}
    for i in df.iterrows():
        if i[1][0] in dicto:
            dicto[i[1][0]] += 1
        else:
            dicto[i[1][0]] = 1
    dicto
    l1 = []
    l2 = []
    for i in dicto:
        l1.append(i)
        l2.append(dicto[i])
    dict = {'Name': l1, 'Present': l2}
    nf = pd.DataFrame(dict)
    nf.head()
    k = dicto.keys()
    v = dicto.values()
    plt.bar(k, v)
    plt.ylim(0, 6)

    from firebase import firebase

    firebase = firebase.FirebaseApplication("https://miniprojectdb-761be-default-rtdb.firebaseio.com/", None)
    for i in dicto:
        x = firebase.get('miniprojectdb-761be-default-rtdb/Student/-McPJqATQTE9Z_H34vB6', i)
        firebase.put('miniprojectdb-761be-default-rtdb/Student/-McPJqATQTE9Z_H34vB6', i, dicto.get(i) + x)

schedule.every(10).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
file=open('')
