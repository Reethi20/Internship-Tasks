const API = "https://YOUR_RENDER_URL.onrender.com";

async function loadFruits() {
    const res = await fetch(`${API}/fruits`);
    const data = await res.json();

    const table = document.getElementById("fruitTable");
    table.innerHTML = "";

    data.forEach(fruit => {
        table.innerHTML += `
            <tr>
                <td>${fruit.id}</td>
                <td>${fruit.name}</td>
                <td>${fruit.quantity}</td>
                <td>${fruit.price}</td>
                <td>
                    <button onclick="deleteFruit(${fruit.id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

async function addFruit() {
    const name = document.getElementById("name").value;
    const quantity = document.getElementById("quantity").value;
    const price = document.getElementById("price").value;

    await fetch(`${API}/add`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, quantity, price })
    });

    loadFruits();
}

async function deleteFruit(id) {
    await fetch(`${API}/delete/${id}`, { method: "DELETE" });
    loadFruits();
}

loadFruits();