from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Home Page - View Records
@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    conn.close()
    return render_template("index.html", students=students)

# Add Record
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    course = request.form["course"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, course) VALUES (?, ?)", (name, course))
    conn.commit()
    conn.close()

    return redirect("/")

# Delete Record
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

# Edit Record Page
@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template("edit.html", student=student)

# Update Record
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    course = request.form["course"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Students SET name=?, course=? WHERE id=?", (name, course, id))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
