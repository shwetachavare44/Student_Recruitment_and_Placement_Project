// Check Login
let studentData = localStorage.getItem("loggedUser");

if (studentData == null) {
    alert("Please Login First!");
    window.location.href = "login.html";
}else{

// Get Student Details
let student = JSON.parse(studentData);

// Welcome Message
document.getElementById("welcome").innerHTML =
"Welcome, " + student.firstName;

// Student Name Below Profile Image
document.getElementById("studentName").innerHTML =
student.firstName + " " + student.lastName;

}
// Sidebar Functions

function profile(){

alert("Profile Page Coming Soon");

// window.location.href="profile.html";

}

function editProfile() {

alert("Edit Profile Page Coming Soon");

    // window.location.href = "editProfile.html";

}

function jobs(){

alert("Job Openings Page Coming Soon");

// window.location.href="job-opening.html";

}

function applications(){

alert("Application Status Page Coming Soon");

// window.location.href="application-status.html";

}

function logout(){

if(confirm("Are you sure you want to logout?")){

window.location.href="login.html";

}

}