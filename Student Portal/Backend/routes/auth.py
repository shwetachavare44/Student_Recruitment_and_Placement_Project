@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    registration_no = data.get("regNo")
    first_name = data.get("fname")
    last_name = data.get("lname")
    dob = data.get("dob")
    location = data.get("location")
    education = data.get("education")
    experience = data.get("experience")
    skills = data.get("skills")
    technical_skills = data.get("technical")
    soft_skills = data.get("soft")
    hobbies = data.get("hobbies")
    interest = data.get("interest")
    job_position = data.get("job")
    preferred_location = data.get("jobLocation")
    email = data.get("email")
    contact = data.get("mobile")
    password = data.get("password")

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM students WHERE email=%s", (email,))
    student = cur.fetchone()

    if student:
        return jsonify({
            "success": False,
            "message": "Email already registered"
        }), 400

    sql = """
    INSERT INTO students
    (
        rNo,
        fname,
        lname,
        dob,
        location,
        education,
        experience,
        skills,
        technical_skills,
        soft_skills,
        hobbies,
        interest,
        job_position,
        preferred_location,
        email,
        contact,
        password
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        regNo,
        fname,
        lname,
        dob,
        location,
        education,
        experience,
        skills,
        technical_skills,
        soft_skills,
        hobbies,
        interest,
        job_position,
        preferred_location,
        email,
        contact,
        password
    )

    cur.execute(sql, values)
    mysql.connection.commit()
    cur.close()

    return jsonify({
        "success": True,
        "message": "Student Registered Successfully"
    })