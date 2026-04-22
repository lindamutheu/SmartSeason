const API_BASE = "http://127.0.0.1:8000/api";

// LOGIN
async function loginUser(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API_BASE}/login/`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (res.ok) {
        localStorage.setItem("token", data.token);
        localStorage.setItem("role", data.role);

        window.location.href = "/dashboard/";
    } else {
        document.getElementById("error").innerText = "Invalid login";
    }
}

// LOAD FIELDS
async function loadFields() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_BASE}/fields/`, {
        headers: {
            "Authorization": `Token ${token}`
        }
    });

    const data = await res.json();
    const container = document.getElementById("fields");

    container.innerHTML = "";

    data.forEach(field => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <h3>${field.name}</h3>
            <p>Size: ${field.size_hectares} ha</p>
        `;
        container.appendChild(div);
    });
}

// LOAD CROPS
async function loadCrops() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_BASE}/crops/`, {
        headers: {
            "Authorization": `Token ${token}`
        }
    });

    const data = await res.json();
    const container = document.getElementById("crops");

    container.innerHTML = "";

    data.forEach(crop => {
        const div = document.createElement("div");
        div.className = "card";
        div.innerHTML = `
            <h3>${crop.name}</h3>
            <p>Stage: ${crop.growth_stage}</p>
        `;
        container.appendChild(div);
    });
}
