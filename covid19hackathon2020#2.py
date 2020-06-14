import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import random

past_num = []
act = {
 1 : "Deep Breathing",
 2 : "Meditation",
 3 : "Biking",
 4 : "Swimming",
 5 : "Jogging",
 6 : "Walking",
 7 : "Facetime Family",
 8 : "Organizing",
 9 : "Smile Now",
 10 : "Nap"
}
hr = 1
mins = 59
sec = 59 
def runAction(activity):
    action = Tk()
    action.geometry("300x200")
    action.title("Random Action Time!")
    label1 = Label(action, text= activity)
    label1.pack()
    action.mainloop()

while True:
    print (str(hr) + ":" + str(min) + ":" + str(sec))
    if sec==60:
        sec=0
        mins+=1
    if mins==60:
        mins=0
        hr+=1
    if sec == 30 or sec == 0:
        num = random.randrange(1,11)
        if num not in past_num:
            past_num.append(num)
            runAction (act[num])
        elif len(past_num) == "10": break
        else: continue
    sec+=1
    time.sleep(1) 
if len(past_num) == "10": runAction("You ran out of options")
else: print("Good Luck!")