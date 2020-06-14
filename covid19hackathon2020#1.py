import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import random


def runPopup():
    popup = Tk()
    popup.geometry("300x200")
    popup.title("Journal Reminder")
    label1 = Label(popup, text="Don't forget to write in your daily journal today!")
    label1.pack()
    #photo = PhotoImage(file = "\Users\arham\book.jpeg" )
    #label2 = Label(popup, image=photo)
    #label2.pack()
    popup.mainloop()


    
hr = 1
mins = 59
sec = 59 

while True:
    print (str(hr) + ":" + str(min) + ":" + str(sec))
    if sec==60:
        sec=0
        mins+=1
    if mins==60:
        mins=0
        hr+=1
    if sec == 30 or sec == 0:
        runPopup()
    sec+=1
    time.sleep(1)
