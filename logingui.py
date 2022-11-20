import signup
import choices
from tkinter import *

def run():
    def check():
        global id
        pn=pno.get()
        p=password.get()
        ans=signup.findbypassword(pn,p)
        print(ans)
        if(len(ans)==0):
            alert=Tk()
            alert.title('Alert')
            Label(alert,text='Alert!!! Wrong Password').pack()
        else:
            choices.run(pn)
    login=Tk()
    login.title("Login")

    frame1=LabelFrame(login).pack()

    Label(login,text='Enter the Patient Number',fg="#663399").pack(padx=20,pady=20)
    pno=Entry(login)
    pno.pack()
    Label(login,text='Enter the Password',fg="#663399").pack(padx=20,pady=20)
    password=Entry(login)
    password.pack()
    sumbit=Button(login,text='Sumbit',fg="orange",bg="black",command=check)
    sumbit.pack()

    login.mainloop()


if __name__ == '__main__':
    run()