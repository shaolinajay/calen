import mysql.connector
from tabulate import tabulate
co=mysql.connector.connect(host="localhost",user="Ajay",password="root",database="py")
def insert(name,age,city):
    cur = co.cursor()
    h="insert into student (name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    cur.execute(h,user)
    co.commit()
    print("sucessful")
def update(id,name,age,city):
    cur = co.cursor()
    hh="update student set name=%s,age=%s,city=%s where id=%s"
    aaa=(name,age,city,id)
    cur.execute(hh,aaa)
    co.commit()
    print("sucessful")
def show():
    cur = co.cursor()
    a="select * from student"
    cur.execute(a)
    result=cur.fetchall()
    print(tabulate(result,headers=["id","name","age","city","std","hel"]))
def delete(id):
    cur=co.cursor()
    f="delete from student where id=%s"
    g=(id,)
    cur.execute(f,g)
    co.commit()
    print("sucessful deleted")
def hole():
    cur=co.cursor()
    hp="delete from student"
    cur.execute(hp)
    co.commit()
def alter(city):
    cur=co.cursor()
    c="alter table student add %s char(20)"%city
    cur.execute(c)
    co.commit()
while (1):
    print("1.show tables")
    print("2.insert data")
    print("3.update data")
    print("4.delete data")
    print("5.exit")
    ch=int(input("enter the choice you want"))
    if ch==1:
        show()
    elif ch==2:
        name=input("enter the name of the student")
        age=int(input("enter the age of the student"))
        city=input("city enter")
        insert(name,age,city)
    elif ch==3:
        id=int(input("enter the id of the data want to update"))
        name=input("enter the name")
        age=int(input("enter the age"))
        city = input("city enter")
        update(id,name,age,city)
    elif ch==4:
        id=int(input("which one you want to delete"))
        delete(id)
    elif ch==5:
        break

