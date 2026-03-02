const API = "https://fullstack-fruit-project.onrender.com";

function saveToken(token, role, username){
    localStorage.setItem("token", token);
    localStorage.setItem("role", role);
    localStorage.setItem("username", username);
}

function getToken(){
    return localStorage.getItem("token");
}

function logout(){
    localStorage.clear();
    window.location.href = "index.html";
}

async function register(){
    const username = document.getElementById("username").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;
    const role = document.getElementById("role").value;

    await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({username,email,password,role})
    });

    alert("Registered successfully");
    window.location.href = "index.html";
}

async function login(){
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({email,password})
    });

    const data = await res.json();

    if(data.token){
        saveToken(data.token, data.role, data.username);
        window.location.href = "dashboard.html";
    } else {
        alert(data.error);
    }
}

async function loadFruits(){
    const res = await fetch(`${API}/fruits`);
    const data = await res.json();

    const table = document.getElementById("fruitTable");
    table.innerHTML = "";

    const role = localStorage.getItem("role");

    data.forEach(fruit=>{
        let action = "";

        if(role === "owner"){
            action = `<button onclick="deleteFruit(${fruit.id})">Delete</button>`;
        } else {
            action = `
                <input type="number" id="qty${fruit.id}" placeholder="Qty" style="width:60px;">
                <button onclick="addToBasket(${fruit.id})">Add</button>
            `;
        }

        table.innerHTML += `
        <tr>
            <td>${fruit.name}</td>
            <td>₹ ${fruit.price}</td>
            <td>${fruit.quantity}</td>
            <td>${action}</td>
        </tr>`;
    });
}

async function addFruit(){
    const name = document.getElementById("fruit_name").value;
    const price = document.getElementById("fruit_price").value;
    const quantity = document.getElementById("fruit_quantity").value;

    await fetch(`${API}/add_fruit`, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({name,price,quantity})
    });

    loadFruits();
}

async function deleteFruit(id){
    await fetch(`${API}/delete_fruit/${id}`, {
        method: "DELETE",
        headers: {"Authorization": getToken()}
    });

    loadFruits();
}

async function addToBasket(id){
    const qty = document.getElementById("qty"+id).value;

    await fetch(`${API}/add_to_basket`, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({fruit_id:id,quantity:qty})
    });

    loadBasket();
}

async function loadBasket(){
    const res = await fetch(`${API}/view_basket`, {
        headers: {"Authorization": getToken()}
    });

    const data = await res.json();

    let html = "";

    data.items.forEach(item=>{
        html += `
            <div>
                <strong>${item.name}</strong><br>
                Quantity: ${item.quantity}<br>
                Price: ₹${item.price}<br>
                Subtotal: ₹${item.subtotal}<br>
                <button onclick="removeFromBasket(${item.id})">Remove</button>
                <hr>
            </div>
        `;
    });

    html += `<div class="total-box">Total: ₹ ${data.total}</div>`;

    document.getElementById("basketData").innerHTML = html;
}

async function removeFromBasket(id){
    await fetch(`${API}/remove_from_basket/${id}`, {
        method: "DELETE",
        headers: {"Authorization": getToken()}
    });

    loadBasket();
}

if(window.location.pathname.includes("dashboard.html")){
    if(!getToken()){
        window.location.href = "index.html";
    }

    document.getElementById("welcome").innerText =
        "Welcome " + localStorage.getItem("username");

    const role = localStorage.getItem("role");

    if(role === "owner"){
        document.getElementById("ownerSection").style.display = "block";
        document.getElementById("actionHeader").innerText = "Action";
    } else {
        document.getElementById("basketSection").style.display = "block";
        document.getElementById("actionHeader").innerText = "Select";
    }

    loadFruits();
}