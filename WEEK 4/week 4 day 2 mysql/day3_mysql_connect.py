import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prashant@2002",
    database="college_db"
)

cursor = conn.cursor()

print("Connected Successfully!")

query = "INSERT INTO students (name, course) VALUES (%s, %s)"
values = ("Rahul", "BCA")

cursor.execute(query, values)
conn.commit()

print("Record Inserted")

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

query = "UPDATE students SET course=%s WHERE name=%s"
values = ("BSc", "Rahul")

cursor.execute(query, values)
conn.commit()

print("Record Updated")

query = "DELETE FROM students WHERE name=%s"
values = ("Rahul",)

cursor.execute(query, values)
conn.commit()

print("Record Deleted")

conn.close()
