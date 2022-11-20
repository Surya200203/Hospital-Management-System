import signup as s
from tkinter import *
import random as rd
import string


def run():
    def insertinto():
        password=''.join(rd.choice(string.ascii_letters) for i in range(5))
        pn=pno.get()
        n=name.get()
        p=phone.get()
        plist=s.findbypno(pn)
        print("list:",plist)
        if pn in plist:
            alert=Tk()
            alert.title('Alert')
            Label(alert,text="Already exists",fg="#663399",font=(30,30)).pack(padx=100,pady=100)
            alert.mainloop()
        else:
            s.insert(int(pn),n,int(p),password)
            Password=Tk()
            Password.title("Password")
            Label(Password,text="Your Password is: ",fg="#663399",font=(25,25)).pack(padx=100,pady=10)
            Label(Password,text=password,font=(30,30)).pack(padx=100,pady=100)
            Password.mainloop()
        signup.destroy()


    signup=Tk()
    signup.title("Signup")

    Label(signup,text='Enter the Patient Number',fg="#663399").pack(padx=20,pady=20)
    pno=Entry(signup)
    pno.pack()
    Label(signup,text='Enter the Patient Name',fg="#663399").pack(padx=20,pady=20)
    name=Entry(signup)
    name.pack()
    Label(signup,text='Enter the Phone Number',fg="#663399").pack(padx=20,pady=20)
    phone=Entry(signup)
    phone.pack()

    sumbit=Button(signup,text='Sumbit',fg="orange",bg="black",command=insertinto).pack()

    signup.mainloop()


if __name__ == '__main__':
    run()
