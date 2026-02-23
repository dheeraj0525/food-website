function getCart() {
    return JSON.parse(localStorage.getItem("cart")) || [];
}

function saveCart(cart) {
    localStorage.setItem("cart", JSON.stringify(cart));
}

function addToCart(item) {
    const cart = getCart();
    const existing = cart.find(i => i.id === item.id);

    if (existing) {
        existing.quantity += 1;
    } else {
        cart.push({ ...item, quantity: 1 });
    }

    saveCart(cart);
    alert("Item added to cart!");
}

/* MENU PAGE */
document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".menu-card button");

    buttons.forEach((btn, index) => {
        btn.addEventListener("click", () => {
            const card = btn.parentElement;

            const item = {
                id: index + 1,
                name: card.querySelector("h3").innerText,
                price: parseInt(card.querySelector("span").innerText.replace("₹", ""))
            };

            addToCart(item);
        });
    });

    renderCart();
});

/* CART PAGE */
function renderCart() {
    const cartPage = document.querySelector(".cart-page");
    if (!cartPage) return;

    const cart = getCart();
    const container = cartPage.querySelector(".container");
    if (!container) return;

    container.innerHTML = ""; // FIXED (prevents duplication)

    let total = 0;

    cart.forEach(item => {
        total += item.price * item.quantity;
        container.innerHTML += `
            <div class="cart-item">
                <h3>${item.name}</h3>
                <p>Price: ₹${item.price}</p>
                <p>Quantity: ${item.quantity}</p>
            </div>
        `;
    });

    container.innerHTML += `
        <div class="cart-summary">
            <h3>Total: ₹${total}</h3>
            <button class="btn-primary">Checkout</button>
        </div>
    `;
}