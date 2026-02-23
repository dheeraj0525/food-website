const API_BASE_URL = "http://localhost:5000/api"; // backend later

async function apiRequest(endpoint, method = "GET", data = null, token = null) {
    const headers = {
        "Content-Type": "application/json"
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(API_BASE_URL + endpoint, {
        method: method,
        headers: headers,
        body: data ? JSON.stringify(data) : null
    });

    if (!response.ok) {
        throw new Error("API request failed");
    }

    return response.json();
}