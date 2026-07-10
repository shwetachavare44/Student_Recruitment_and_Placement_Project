# from flask import Blueprint, request, jsonify
# from database import mysql

# student_bp = Blueprint("student", __name__)

# @student_bp.route("/register", methods=["POST"])
# def register():

#     data = request.json

#     first_name = data["first_name"]
#     last_name = data["last_name"]
#     email = data["email"]
#     password = data["password"]

#     cursor = mysql.connection.cursor()

#     sql = """
#     INSERT INTO students(first_name,last_name,email,password)
#     VALUES(%s,%s,%s,%s)
#     """

#     cursor.execute(sql, (first_name, last_name, email, password))

#     mysql.connection.commit()

#     cursor.close()

#     return jsonify({
#         "message":"Student Registered Successfully"
#     })


from flask import Blueprint, request, jsonify
from database import mysql
from werkzeug.security import generate_password_hash

student_bp = Blueprint("student", __name__)


@student_bp.route("/register", methods=["POST"])
def register():

    try:

        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        # Validation
        if not first_name or not last_name or not email or not password:
            return jsonify({
                "success": False,
                "message": "All fields are required"
            }), 400

        cursor = mysql.connection.cursor()

        # Check Email Exists
        cursor.execute(
            "SELECT * FROM students WHERE email=%s",
            (email,)
        )

        student = cursor.fetchone()

        if student:
            cursor.close()
            return jsonify({
                "success": False,
                "message": "Email already exists"
            }), 409

        # Hash Password
        hashed_password = generate_password_hash(password)

        sql = """
        INSERT INTO students(first_name,last_name,email,password)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(
            sql,
            (
                first_name,
                last_name,
                email,
                hashed_password
            )
        )

        mysql.connection.commit()

        cursor.close()

        return jsonify({
            "success": True,
            "message": "Student Registered Successfully"
        }), 201

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500