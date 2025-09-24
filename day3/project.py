# how to connect py to mysql database

# pre requisites
# python
# sql
# pip install mysql-connector-python

# structured of database table
# database -> table 

# create a file import mysql.connector
import mysql.connector

# create a connection object
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='teja123',
    database='demo'
    )

# create a cursor object- like a pointer - which exeutes the sql queries
mycursor=mydb.cursor()

# execute sql queries
# mycursor.execute("select * from emp")
# results=mycursor.fetchall()
# print(results)

# # close the connection
# mydb.close()

# insert data into table-add


def adddata():
    id=int(input("enter id:"))
    name=input("enter name:")
    age =int(input("enter age:"))
    mycursor.execute(f'insert into emp values ({id},"{name}",{age})')
    mydb.commit()

def getdata():
    mycursor.execute("select * from emp")
    results=mycursor.fetchall()
    for i in results:
        print(i)

def updatedata():
    id=int(input("enter id:"))
    name=input("enter name:")
    mycursor.execute(f"update emp set name='{name}' where id={id}")
    mydb.commit()

# 'delete from emp where id={id}'
def deldata():
    id=int(input("enter id:"))
    mycursor.execute(f"delete from emp where id={id}")
    mydb.commit()

# deldata()
# # updatedata()
# getdata()
def menu():
    while True:
        print("1. add data")
        print("2. get data")
        print("3. update data")
        print("4. delete data")
        print("5. exit")

        choice=int(input("enter your choice:"))
        if choice==1:
            adddata()
        elif choice==2:
            getdata()
        elif choice==3:
            updatedata()
        elif choice==4:
            deldata()
        elif choice==5:
            break
        else:
            print("invalid choice")


menu()