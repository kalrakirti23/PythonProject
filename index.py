import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="HMRITM123@",
  database="demoPython"
)

mycursor = mydb.cursor()

def insert():
   roll = int(input("Enter Roll Number:\n"))
   name = input("Enter your Name:\n")
   className = input("Enter your Class (10/11/12):\n")
   mycursor.execute("Insert into student_master values("+roll+""+name+""+className+")")
   return "Data Inserted Successfully!"

def show():
   mycursor.execute("select * from Student_Master")
   for x in mycursor:
     print(x)
   return "Data Fetched Successfully!"


def delete():
   rollNo = int(input("Enter Roll Number you want to Delete:\n"))
   mycursor.execute("delete from student_master where Roll_No="+rollNo+";")
   return "Data Deleted Successfully!"


print("Select operation:")
print("1.Insert Data")
print("2.Show Data")
print("3.Delete Data")

# Take input from the user 
choice = input("Enter choice(1/2/3):")


if choice == '1':
   print(insert())

elif choice == '2':
   print(show())

elif choice == '3':
   print(delete())

else:
   print("Invalid input")



