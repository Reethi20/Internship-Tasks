const API = "https://fullstack-fruit-project.onrender.com";

let basket = [];

function saveToken(token){
    localStorage.setItem("token", token);
}

function getToken(){
    return localStorage.getItem("token");
}

function logout(){
    localStorage.removeItem("token");
    alert("Logged out successfully");
    window.location.href = "index.html";
}

function showAlert(message){
    alert(message);
}

function validEmail(email){
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

async function register(){
    const username = document.getElementById("username").value.trim();
    const email = document.getElementById("reg_email").value.trim();
    const password = document.getElementById("reg_password").value.trim();

    if(!username || !email || !password){
        return showAlert("All fields are required");
    }

    if(!validEmail(email)){
        return showAlert("Enter valid email");
    }

    if(password.length < 5){
        return showAlert("Password must be at least 5 characters");
    }

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({username,email,password})
    });

    const data = await res.json();

    if(data.message){
        showAlert("Registration successful");
        window.location.href = "index.html";
    } else {
        showAlert(data.error);
    }
}

async function login(){
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    if(!email || !password){
        return showAlert("All fields are required");
    }

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({email,password})
    });

    const data = await res.json();

    if(data.token){
        saveToken(data.token);
        showAlert("Login successful");
        window.location.href = "dashboard.html";
    } else {
        showAlert(data.error);
    }
}

async function loadFruits(){
    const res = await fetch(`${API}/fruits`, {
        headers: {"Authorization": getToken()}
    });

    if(res.status === 401){
        showAlert("Session expired. Login again.");
        return logout();
    }

    const data = await res.json();
    const table = document.getElementById("fruitTable");
    table.innerHTML = "";

    data.forEach(fruit=>{
        table.innerHTML += `
        <tr>
            <td>${fruit.name}</td>
            <td>${fruit.quantity}</td>
            <td>${fruit.price}</td>
            <td>
                <button onclick="deleteFruit(${fruit.id})">Delete</button>
            </td>
            <td>
                <button onclick="addToBasket(${fruit.price})">Add</button>
            </td>
        </tr>`;
    });
}

async function addFruit(){
    const name = document.getElementById("fruit_name").value.trim();
    const quantity = document.getElementById("quantity").value;
    const price = document.getElementById("price").value;

    if(!name || !quantity || !price){
        return showAlert("All fruit fields are required");
    }

    if(quantity <= 0 || price <= 0){
        return showAlert("Quantity and price must be positive");
    }

    await fetch(`${API}/add`, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({name,quantity,price})
    });

    showAlert("Fruit added successfully");
    loadFruits();
}

async function deleteFruit(id){
    if(!confirm("Are you sure you want to delete this fruit?")){
        return;
    }

    await fetch(`${API}/delete/${id}`, {
        method: "DELETE",
        headers: {"Authorization": getToken()}
    });

    showAlert("Fruit deleted");
    loadFruits();
}

function addToBasket(price){
    basket.push(Number(price));
    let total = basket.reduce((sum,val)=> sum+val,0);
    document.getElementById("total").innerText = total;
}

if(window.location.pathname.includes("dashboard.html")){
    if(!getToken()){
        showAlert("Please login first");
        window.location.href = "index.html";
    } else {
        loadFruits();
    }
}