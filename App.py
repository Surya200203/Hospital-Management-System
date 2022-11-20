import Signupgui
import logingui
from tkinter import *

def signup():
    Signupgui.run()

def login():
    logingui.run()

window=Tk()
window.title('SYS Hospitals')

frame=LabelFrame(window).pack()

description="Welcome to the SYS Hospital.\n\nGood health and good sense are two of life's greatest blessings."

label1=Label(frame,text='**** SYS Hospital ****',font=(30,30),fg="#663399")
label2=Label(frame,text=description,font=(20,20),fg="#663399")

label1.pack(padx=100,pady=100,fill=X)
label2.pack()
button1=Button(window,text='SignUp',fg="orange",bg="black",font=(20,20),command=signup,relief=RAISED).pack(side=LEFT,padx=150,pady=100)
button2=Button(window,text='Login',fg="orange",bg="black",font=(20,20),command=login).pack(side=LEFT,padx=100,pady=80)

window.mainloop()