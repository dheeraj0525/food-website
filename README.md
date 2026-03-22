# 🍽️ Food website — Full-Stack Food Ordering Web App

> A full-stack food ordering web application where users can register, log in, browse a menu, add items to a cart, and place orders — built with Flask, MySQL, and vanilla JavaScript.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![HTML CSS JS](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---
## 📸 Screenshots

### Home Page
![Home Page](website/images/home.png)

### Menu Page  
![Menu Page](website/images/menu.png)

### Cart Page
![Cart Page](screenshots/cart.png)

### Login Page
![login Page](screenshots/login.png)

### Register page
![Register Page](screenshots/register.png)

## ✨ Features

- 🔐 User registration and login with session management
- 🍕 Browse food menu with item categories
- 🛒 Add and remove items from cart
- 📦 Place and confirm orders
- 📱 Fully responsive UI across all screen sizes
- 🔌 REST API backend built with Flask
- 🗄️ Persistent data storage with MySQL

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3, JavaScript (ES6) |
| Backend | Python, Flask |
| Database | MySQL |
| Auth | Flask Session Management |
| Deployment | Render *(in progress)* |

---

## 📂 Project Structure
```
food-website/
│
├── website/
│   ├── backend/
│   │   ├── app.py           # Flask app entry point
│   │   ├── routes/          # Route handlers
│   │   ├── models/          # Database models
│   │   └── config.py        # App configuration
│   │
│   ├── frontend/
│   │   ├── index.html       # Main HTML entry
│   │   ├── css/             # Stylesheets
│   │   ├── js/              # Client-side logic
│   │   └── images/          # Static assets
│   │
│   └── database/
│       └── schema.sql       # MySQL table definitions
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.9+
- MySQL 8.0+
- pip

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/dheeraj0525/food-website.git
cd food-website

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up the database
# Create a MySQL database named foodhub
mysql -u root -p < website/database/schema.sql

# 5. Configure database credentials
# Edit website/backend/config.py and update:
# DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# 6. Run the Flask development server
python website/backend/app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## 🗄️ Database Schema

| Table | Purpose |
|-------|---------|
| `users` | Stores registered user accounts |
| `menu_items` | Food items with name, price, category |
| `cart` | User cart sessions and selected items |
| `orders` | Confirmed order records |

---

## 🔄 How It Works
```
User registers / logs in
        ↓
Browses menu → adds items to cart
        ↓
Flask API handles all requests
        ↓
MySQL stores users, cart, orders
        ↓
Order confirmed and saved to DB
```

---

## 🚧 Planned Improvements

- [ ] JWT-based authentication
- [ ] Payment gateway integration (Razorpay)
- [ ] Admin dashboard for order management
- [ ] Order status tracking
- [ ] Deploy on Render

---

## 👤 Author

**Dheeraj Aryan**  
BCA — Artificial Intelligence & Data Science  

[![GitHub](https://img.shields.io/badge/GitHub-dheeraj0525-black?style=flat-square&logo=github)](https://github.com/dheeraj0525)
## 📄 License

This project is open source and available under the [MIT License](LICENSE).
