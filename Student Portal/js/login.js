function togglePassword(){

    let password=document.getElementById("password");

    if(password.type==="password"){

        password.type="text";

    }
    else{

        password.type="password";

    }

}

document.getElementById("loginForm").addEventListener("submit",function(e){

    e.preventDefault();

    let email=document.getElementById("email").value.trim();

    let password=document.getElementById("password").value;

    let message=document.getElementById("message");

    let student=JSON.parse(localStorage.getItem(email));

    if(student==null){

        message.style.color="red";

        message.innerHTML="Email is not registered.";

        return;

    }

    if(student.password!==password){

        message.style.color="red";

        message.innerHTML="Incorrect Password.";

        return;

    }

    localStorage.setItem("loggedUser", JSON.stringify(student));

    message.style.color="green";

    message.innerHTML="Login Successful...";

    setTimeout(function(){

        window.location.href="dashboard.html";

    },1500);

});
