import signup
from tkinter import *
import signup

def run():
    window=Tk()
    window.title("View Patients")
    cur=signup.display()
    for i,j in enumerate(cur):
        (pno,name,Phone)=j
        label=Label(window,text=f"Patient no:{pno} \n Name:{name} \n Phone Number:{Phone}",fg="#663399")
        label.grid(row=i+1,column=1)
    window.mainloop()



if __name__ == '__main__':
    run()

