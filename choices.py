from tkinter import *
import viewpatients as vp
import viewappointments as va
import bookappointments as ba
def run(pno):
    def viewrecord():
        vp.run()

    def viewappointment():
        va.run()

    def bookappointment():
        ba.run(pno)

    choices=Tk()
    Label(choices,text="Choose your option",font=(30,30),padx=20,pady=20,fg="#663399").pack(padx=50,pady=50)
    viewpatient=Button(choices,text='View Patients',font=(15,15),fg="orange",bg="black",command=viewrecord,padx=20,pady=20).pack(side=LEFT,padx=100,pady=100)
    viewcomplaints=Button(choices,text='View Appointment',font=(15,15),fg="orange",bg="black",command=viewappointment,padx=20,pady=20).pack(side=LEFT,padx=100,pady=100)
    logdecomplaints=Button(choices,text='Book Appointment',font=(15,15),fg="orange",bg="black",command=bookappointment,padx=20,pady=20).pack(side=LEFT,padx=100,pady=100)

    choices.mainloop()


if __name__ == '__main__':
    run()