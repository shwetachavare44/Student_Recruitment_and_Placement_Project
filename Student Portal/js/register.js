function showPassword(){

    let password=document.getElementById("password");

    if(password.type==="password")
        password.type="text";
    else
        password.type="password";

}

document.getElementById("resume").addEventListener("change",function(){

    if(this.files.length>0){

        document.getElementById("resumeName").innerHTML=
        "Selected File : "+this.files[0].name;

    }

});

let inputs=document.querySelectorAll("input,textarea,select");

inputs.forEach(function(input){

    input.addEventListener("input",updateProgress);

});

function updateProgress(){

    let total=inputs.length;

    let filled=0;

    inputs.forEach(function(input){

        if(input.value.trim()!="")

            filled++;

    });

    let percent=(filled/total)*100;

    document.getElementById("progressBar").style.width=percent+"%";

}

document.getElementById("registerForm").addEventListener("submit",function(e){

    e.preventDefault();

    let email=document.getElementById("email").value;

    if(localStorage.getItem(email)!=null){

        alert("Email already registered!");

        return;

    }

    let mobile=document.getElementById("mobile").value;

    if(mobile.length!=10){

        alert("Enter valid 10 digit Mobile Number");

        return;

    }

    let password=document.getElementById("password").value;

    let confirm=document.getElementById("confirmPassword").value;

    if(password.length<6){

        alert("Password should contain minimum 6 characters");

        return;

    }

    if(password!=confirm){

        alert("Passwords do not match");

        return;

    }

    let student={

        regNo:document.getElementById("regNo").value,

        firstName:document.getElementById("firstName").value,

        lastName:document.getElementById("lastName").value,

        dob:document.getElementById("dob").value,

        location:document.getElementById("location").value,

        email:email,

        mobile:mobile,

        password:password,

        experience:document.getElementById("experience").value,

        job:document.getElementById("job").value,

        jobLocation:document.getElementById("jobLocation").value,

        skills:document.getElementById("skills").value,

        technical:document.getElementById("technical").value,

        soft:document.getElementById("soft").value,

        hobbies:document.getElementById("hobbies").value,

        interest:document.getElementById("interest").value

    };

    localStorage.setItem(email,JSON.stringify(student));

    document.getElementById("message").style.color="green";

    document.getElementById("message").innerHTML="✅ Registration Successful!";

    setTimeout(function(){

        window.location.href="login.html";

    },2000);

});