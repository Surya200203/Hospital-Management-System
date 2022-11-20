from dis import dis
import sqlite3

conn=sqlite3.connect("C:/Users\Admin\OneDrive\Desktop\db\mydb.db")

cur=conn.cursor()

def create(c):
    if(c=='Y'):
        cur.execute("create table appointment (pno integer ,reason string,foreign key (pno) references Patient(pno))")

def insert(id,reason):
    cur.execute("insert into appointment values(?,?)",(id,reason))
    conn.commit()

def deletebyid(patient_id):
    cur.execute("delete from appointment where pno=(?)",patient_id)

def display():
    l=[]
    cur.execute("select * from appointment")
    for i in cur:
        l.append(i)
    return l

def drop():
    cur.execute("drop table appointment")

if __name__ == '__main__':
    create('Y')




