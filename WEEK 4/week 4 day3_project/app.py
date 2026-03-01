Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from flask import Flask, render_template, request
... import sqlite3
... 
... app = Flask(__name__)
... 
... @app.route("/")
... def home():
...     return render_template("form.html")
... 
... @app.route("/submit", methods=["POST"])
... def submit():
...     name = request.form["name"]
...     age = request.form["age"]
...     course = request.form["course"]
... 
...     conn = sqlite3.connect("student.db")
...     cursor = conn.cursor()
... 
...     cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, course TEXT)")
...     cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (name, age, course))
... 
...     conn.commit()
...     conn.close()
... 
...     return "Data Stored Successfully!"
... 
... @app.route("/students")
... def students():
...     conn = sqlite3.connect("student.db")
...     cursor = conn.cursor()
... 
...     cursor.execute("SELECT * FROM students")
...     data = cursor.fetchall()
... 
...     conn.close()
... 
...     return str(data)
... 
... if __name__ == "__main__":
