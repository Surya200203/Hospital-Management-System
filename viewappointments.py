import appointment
from tkinter import *

def run():
    window=Tk()
    window.title("View Appointment")
    cur=appointment.display()
    for i,j in enumerate(cur):
        (pno,compl)=j
        label=Label(window,text=f"Patient number:{pno} \n Reason :{compl}")
        label.grid(row=i+1,column=1)
        print(i,j)
    window.mainloop()



if __name__ == '__main__':
    run()

