const API = "https://YOUR_RENDER_URL.onrender.com";

let basket = [];

function saveToken(token){
    localStorage.setItem("token", token);
}

function getToken(){
    return localStorage.getItem("token");
}

function logout(){
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

async function register(){
    const username = document.getElementById("username").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;

    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({username,email,password})
    });

    const data = await res.json();
    document.getElementById("reg_message").innerText = data.message || data.error;
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
        saveToken(data.token);
        window.location.href = "dashboard.html";
    } else {
        document.getElementById("message").innerText = data.error;
    }
}

async function loadFruits(){
    const res = await fetch(`${API}/fruits`, {
        headers: {"Authorization": getToken()}
    });
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
    const name = document.getElementById("fruit_name").value;
    const quantity = document.getElementById("quantity").value;
    const price = document.getElementById("price").value;

    await fetch(`${API}/add`, {
        method: "POST",
        headers: {
            "Content-Type":"application/json",
            "Authorization": getToken()
        },
        body: JSON.stringify({name,quantity,price})
    });

    loadFruits();
}

async function deleteFruit(id){
    await fetch(`${API}/delete/${id}`, {
        method: "DELETE",
        headers: {"Authorization": getToken()}
    });
    loadFruits();
}

function addToBasket(price){
    basket.push(Number(price));
    let total = basket.reduce((sum,val)=> sum+val,0);
    document.getElementById("total").innerText = total;
}

if(window.location.pathname.includes("dashboard.html")){
    if(!getToken()){
        window.location.href = "index.html";
    } else {
        loadFruits();
    }
}