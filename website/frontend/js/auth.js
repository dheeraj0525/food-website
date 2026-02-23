document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const inputs = form.querySelectorAll("input");

        let email = "";
        let password = "";

        if (inputs.length === 3) {
            // Register page
            email = inputs[1].value;
            password = inputs[2].value;
        } else {
            // Login page
            email = inputs[0].value;
            password = inputs[1].value;
        }

        if (email && password) {
            localStorage.setItem("token", "dummy-jwt-token");
            localStorage.setItem("user", JSON.stringify({ email }));

            alert("Login successful!");
            window.location.href = "index.html";
        } else {
            alert("Please fill all fields");
        }
    });
});