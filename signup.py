import sqlite3

conn=sqlite3.connect("C:/Users\Admin\OneDrive\Desktop\db\mydb.db")
# conn=sqlite3.connect("mydb.db")

cur=conn.cursor()

def create(c):
    print("IN create")
    if(c=='Y'):
        cur.execute("create table Patient (pno integer primary key,name string, phoneNumber integer, password string)")
    conn.commit()

def insert(pno,name,phoneNumber,password):
    cur.execute("insert into Patient values(?,?,?,?)",(pno,name,phoneNumber,password))
    conn.commit()

def deletebyid(patient_pno):
    cur.execute("delete from Patient where flatno==(?)",(patient_pno,))
    conn.commit()

def display():
    l=[]
    cur.execute("select pno,name,phoneNumber from Patient")
    for i in cur:
        l.append(i)
    return l

def displaypassword(pno):
    l=[]
    cur.execute("select password from (select * from Patient where pno==(?))",(pno,))
    for i in cur:
        l.append(i)
    return l

def findbypassword(patient_pno,password):
    l=[]
    cur.execute("select * from Patient where pno==(?) and password==(?)",(patient_pno,password))
    for i in cur:
        l.append(i)
    return l

def findbypno(patient_pno):
    l=[]
    cur.execute("select pno from Patient where pno==(?)",(patient_pno,))
    l.append(cur)
    return l

def drop():
    cur.execute("drop table Patient")

if __name__ == '__main__':
    print("In __name__")
    create('Y')


