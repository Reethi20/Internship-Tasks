function validateRegister() {
    var name = document.getElementById("regName").value.trim();
    var email = document.getElementById("regEmail").value.trim();
    var password = document.getElementById("regPassword").value;

    if (name === "" || email === "" || password === "") {
        alert("All fields are required.");
        return false;
    }

    alert("Registration Successful!");
    return true;
}

function validateLogin() {
    var email = document.getElementById("loginEmail").value.trim();
    var password = document.getElementById("loginPassword").value;

    if (email === "" || password === "") {
        alert("Enter both email and password.");
        return false;
    }

    alert("Login Successful!");
    return true;
}

function validateContact() {
    var name = document.getElementById("contactName").value.trim();
    var message = document.getElementById("contactMessage").value.trim();

    if (name === "" || message === "") {
        alert("Please fill all required fields.");
        return false;
    }

    alert("Message Sent Successfully!");
    return true;
}
