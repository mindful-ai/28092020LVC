import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()


print('Database creation')
#mycursor.execute("CREATE DATABASE mydatabase2")



print('\n\nShowing databases')


mycursor.execute("SHOW DATABASES")


for x in mycursor:
  print(x)
