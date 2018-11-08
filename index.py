import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="HMRITM123@",
  database="demoPython"
)

mycursor = mydb.cursor()

mycursor.execute("Insert into student_master values(120,'Ravan','12')")
print(mycursor)

