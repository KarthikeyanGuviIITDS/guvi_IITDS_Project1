import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="project1")
cursor = connection.cursor()

print("1.Add new student")
print("2.Get student")
print("3.Get all student")
print("4.Edit a student")
print("5.Delete a student")
print("6.Exit")

option=int(input("Enter value: "))
print(option)

if option==1:
    id=int(input("Enter student id: "))
    name=input("Enter student name: ")
    dept=input("Enter student dept: ")
    mark1=int(input("Enter student mark1: "))
    mark2=int(input("Enter student mark2: "))
    mark3=int(input("Enter student mark3: "))
    mark4=int(input("Enter student mark4: "))
    mark5=int(input("Enter student mark5: "))
    ins_query="insert into marklist values("+str(id)+",'"+name+"','"+dept+"',"+str(mark1)+","+str(mark2)+","+str(mark3)+","+str(mark4)+","+str(mark5)+")"
    #print(ins_query)
    cursor.execute(ins_query)
    connection.commit()
elif option==2:
    id=int(input("Enter student id: "))
    sel_query="select *, (mark1+mark2+mark3+mark4+mark5) as total, cast(((mark1+mark2+mark3+mark4+mark5)/5) as float) as average from marklist where Id="+str(id)
    cursor.execute(sel_query)
    result = cursor.fetchall()
    for i in result:
        print(i)
elif option==3:
    cursor.execute("SELECT * FROM marklist")
    result = cursor.fetchall()
    for i in result:
        print(i)
elif option==4:
    id=int(input("Enter student id: "))
    field=input("Enter column to edit: ")
    value=int(input("Enter new value: "))
    upd_query="update marklist set "+field+"="+str(value)+" where Id="+str(id)
    #print(upd_query)
    cursor.execute(upd_query)
    connection.commit()
elif option==5:
    id=int(input("Enter student id: "))
    del_query="delete from marklist where Id="+str(id)
    cursor.execute(del_query)
    connection.commit()
elif option==6:
    print("Exiting")
elif option==7:
    cursor.execute("SELECT *, (mark1+mark2+mark3+mark4+mark5) as total, cast(((mark1+mark2+mark3+mark4+mark5)/5) as float) as average FROM marklist")
    result = cursor.fetchall()
    for i in result:
        print(i)
else:
    print("Choose option as displayed above")

cursor.close()
connection.close()