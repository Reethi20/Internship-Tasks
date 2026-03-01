function changeText() {
    var text = document.getElementById("changeText");
    var button = document.getElementById("textBtn");

    text.innerHTML = "The text has been changed using JavaScript.";
    text.style.color = "#880e4f";
    button.style.backgroundColor = "#1f3c88";
}

function getValues() {
    var n1 = document.getElementById("num1").value;
    var n2 = document.getElementById("num2").value;

    if (n1 === "" || n2 === "") {
        alert("Please enter both numbers.");
        return null;
    }

    return {
        num1: parseFloat(n1),
        num2: parseFloat(n2)
    };
}

function add() {
    var values = getValues();
    if (!values) return;
    document.getElementById("result").innerHTML =
        "Result: " + (values.num1 + values.num2);
}

function subtract() {
    var values = getValues();
    if (!values) return;
    document.getElementById("result").innerHTML =
        "Result: " + (values.num1 - values.num2);
}

function multiply() {
    var values = getValues();
    if (!values) return;
    document.getElementById("result").innerHTML =
        "Result: " + (values.num1 * values.num2);
}

function divide() {
    var values = getValues();
    if (!values) return;

    if (values.num2 === 0) {
        alert("Cannot divide by zero.");
        return;
    }

    document.getElementById("result").innerHTML =
        "Result: " + (values.num1 / values.num2);
}

function clearFields() {
    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";
    document.getElementById("result").innerHTML = "";
}

function validateForm() {

    var name = document.getElementById("name").value.trim();
    var email = document.getElementById("email").value.trim();
    var phone = document.getElementById("phone").value.trim();
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;
    var terms = document.getElementById("terms").checked;

    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var phonePattern = /^[0-9]{10}$/;

    if (name === "") {
        alert("Full Name is required.");
        return false;
    }

    if (!emailPattern.test(email)) {
        alert("Enter a valid email address.");
        return false;
    }

    if (!phonePattern.test(phone)) {
        alert("Enter a valid 10-digit phone number.");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters long.");
        return false;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    if (!terms) {
        alert("You must agree to the Terms & Conditions.");
        return false;
    }

    alert("Form submitted successfully.");
    return true;
}
