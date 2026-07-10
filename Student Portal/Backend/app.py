from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Alpha@123",
    database="student_placement_system"
)

cursor = connection.cursor()

# ---------------- Register API ----------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    regNo = data["regNo"]
    fname = data["fname"]
    lname = data["lname"]
    email = data["email"]
    password = data["password"]

    sql = """
    INSERT INTO students
    (regNo, fname, lname, email, password)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (regNo, fname, lname, email, password)

    cursor.execute(sql, values)
    connection.commit()

    return jsonify({"message": "Student Registered Successfully"})


# ---------------- Login API ----------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    sql = "SELECT * FROM students WHERE email=%s AND password=%s"

    cursor.execute(sql, (email, password))

    student = cursor.fetchone()

    if student:
        return jsonify({"message": "Login Successful"})
    else:
        return jsonify({"message": "Invalid Email or Password"})


# ---------------- Run Flask ----------------
if __name__ == "__main__":
    app.run(debug=True)