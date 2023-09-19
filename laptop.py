import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shaheen")
    cursor = mydb.cursor()
    cursor.execute("Create database contactbook1")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shaheen",
        database="contactbook1"
    )
    cursor = mydb.cursor()
    cursor.execute("Create table phonebook(name varchar(25),phoneno bigint)")
except:
    print("DB already exists!!!")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shaheen",
    database="contactbook1"
)
cursor = mydb.cursor()


def insert(name, phno):
    cursor.execute("select name from phonebook")
    names = cursor.fetchall()
    f = 0
    for i in names:
        if name == i[0]:
            f = 1
    if f == 0:
        cursor.execute("Insert into phonebook(name,phoneno) values(%s,%s)", (name, phno))
        mydb.commit()
    else:
        print("Name already exists!!")
        cursor.execute("update phonebook set phoneno=%s where name=%s", (phno, name))
        mydb.commit()


def update(data):
    if (data == "name"):
        oldname = input("Enter old name:")
        cursor.execute("select name from phonebook where name=%s", (oldname,))
        selname = cursor.fetchall()

        print(selname)
        newname = input("Enter new name:")
        if newname in selname:
            print("Name exists!!!")
        else:
            cursor.execute("update phonebook set name=%s where name=%s", (newname, oldname))
            mydb.commit()
            print("Updated Successfully")
    else:
            print("can't update")


def delete(item):
    cursor.execute("Select name from phonebook")
    itemlis = cursor.fetchall()
    f = True
    for i in itemlis:
        if item in i[0]:
            cursor.execute("delete from phonebook where name=%s", (item,))
            mydb.commit()
            f = False
    if f:
        print("Contact not found")


def display():
    cursor.execute("select * from phonebook")
    cntcts = cursor.fetchall()
    print(cntcts)


while (True):
    print("---------MENU---------")
    print("1.Insertion\n2.Updation\n3.Deletion\n4.Display\n5.Exit")
    ch = int(input("Enter your choice:"))
    if (ch == 1):
        print("Insert new contact")
        name = input("Enter Name:")
        phno = input("Enter no:")
        insert(name, phno)
    elif (ch == 2):
        print("Updation")
        data = input("Update name??")
        update(data)
    elif (ch == 3):
        print("Deletion")
        item = input("Enter name:")
        delete(item)
    elif (ch == 4):
        display()
    elif (ch == 5):
        break
    else:
        print("wrong choice")


