import mysql.connector

mydb = mysql.connector.connect(
  host="host.docker.internal",
  user="root",
  password="****"
  
)
mycursor=mydb.cursor()
mycursor.execute("select * from gununsozu.sozler")

for i in mycursor:
    print(i)
   