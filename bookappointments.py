import appointment as a
from tkinter import *

def run(pno):
    def Submit():
        c=complaint.get()
        a.insert(pno,c)
        window.destroy()
    window=Tk()
    window.title("Book Appointment")

    Label(window,text='Enter the reason:',fg="#663399").pack(padx=20,pady=20)
    complaint=Entry(window)
    complaint.pack()
    submit=Button(window,text='Submit',fg="orange",bg="black",command=Submit).pack(padx=20,pady=20)

    window.mainloop()



if __name__ == '__main__':
    run()

