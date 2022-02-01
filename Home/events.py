import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  password="123456789",
  database="books"
)

mycursor = mydb.cursor()

sql = "INSERT INTO events (title, start_date, end_date) VALUES (%s, %s, %s)"
val = ("Always With You: An Evening with Debbie Malone", "2018-09-26", "2018-09-26")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")