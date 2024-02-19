# importing all the necessary libraries to form the alarm clock 

from tkinter import *
import datetime
import time
import pydub

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H : %M : %S")
        date = current_time.strftime("%d - %m  - %Y")
        print('The Set Date is ',date)
        print(now)
        if now == set_alarm_timer:
            print("Time to wake up..")
            
