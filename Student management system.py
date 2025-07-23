print("\t\t\t\t\t\tWELCOME TO STUDENT MANAGEMENT SYSTEM\n")
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="root123")
mycursor = mydb.cursor()
db = input("Enter the name of your database :")
cdb = "create database if not exists %s" % (db,)
mycursor.execute(cdb)
print("Database Created Successfully...")
mycursor = mydb.cursor()
mycursor.execute(" use "+db)
table_name = input("Enter the name of the table that you want to create :")
query = "Create table if not exists " + table_name + "(Admno int(3) primary key,Name varchar(20),DOB date,Gender char(1))"
print("Your Table is", table_name, "Created Successfully...")
mycursor.execute(query)
while True:
    print("\n\n")
    print("*"*134)
    print("\t\t\t\t\t\t\t\t MAIN MENU")
    print("*"*134)
    print("\t\t\t\t1. Adding Students Records")
    print("\t\t\t\t2. For Displaying records of all students")
    print("\t\t\t\t3. For Displaying records of a particular student")
    print("\t\t\t\t4. For Deleting records of all students")
    print("\t\t\t\t5. For Deleting record of a particular student")
    print("\t\t\t\t6. For Updating a Record of a particular student")
    print("\t\t\t\t7. For Exit")
    ch = int(input("Enter your choice from the above :"))
    if ch == 1:
        try:
            print("Enter Student Information...")
            adm = int(input("Enter the Admission No. :"))
            sname = input("Enter Student Name :")
            dob = input("Enter Date Of Birth :")
            gender = input("Enter Gender M/F :")
            rec = (adm,sname,dob,gender)
            query = "insert into " + table_name + " values(%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print("Record Added Successfully...")
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 2:
        try:
            query = "select *from " + table_name
            mycursor.execute(query)
            result = mycursor.fetchall()
            for x in result:
                print(x)
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 3:
        try:
            ad = input("Enter the Admission no. of the record to be displayed :")
            query = "select * from " + table_name + " where admno=" + ad
            mycursor.execute(query)
            myrecord = mycursor.fetchone()
            print("Record of Admission No. " + ad)
            print(myrecord)
            c = mycursor.rowcount
            if c == -1:
                print("Nothing to display")
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 4:
        try:
            ch = input("Do you want to delete all the records(y/n")
            if ch == "y":
                mycursor.execute("delete from " + table_name)
                mydb.commit()
                print("All the records are deleted...")
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 5:
        try:
            ad = input("Enter the Admission no. of the record to be deleted :")
            query = "delete from " + table_name + " where admno=" + ad
            mycursor.execute(query)
            mydb.commit()
            c = mycursor.rowcount
            if c > 0:
                print("Deletion done")
            else:
                print("Admission no.", ad, "is not found")
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 6:
        try:
            ad = input("Enter the Admission no. of the record to be updated :")
            print("What you want to update ?")
            print("1:Student Name")
            print("2:Date Of Birth")
            ch = int(input("Enter the choice from above :"))
            if ch == 1:
                st_name = input("Enter the student name :")
                Gender = input("Enter the gender M/F :")
                query = "update " + table_name + " set Name = " + st_name + " ,Gender = "f + Gender + " where Admno = " + ad
                mycursor.execute(query)
                mydb.commit
            elif ch == 2:
                dob = input("Enter the new date of birth :")
                query = "update " + table_name + "set DOB = " + dob + " Where Admno = " + ad
                mycursor.execute(query)
                mydb.commit()
        except Exception as e:
            print("Something went wrong",e)
    elif ch == 7:
        break
    else:
        print("Wrong choice...")
                
