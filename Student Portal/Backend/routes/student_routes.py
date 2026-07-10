from flask import Blueprint, request, jsonify

student = Blueprint("student", __name__)

@student.route("/register", methods=["POST"])
def register():

    data = request.json

    return jsonify({
        "message": "Student Registered Successfully"
    })