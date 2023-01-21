import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="retretTRD$56d$%^D45d6456d354534"
)


mycursor = mydb.cursor()

mycursor.execute("show variables like 'innodb%';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0] ,":" , x[1])



#print(mydb)
