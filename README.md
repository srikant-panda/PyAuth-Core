````md
# 🔐 PyAuth-Core

PyAuth-Core is a modular **Python CLI authentication system** built to practice **OOP concepts** and backend-style architecture.

It supports user authentication features like registration, login, password validation, password change, and an admin panel using a JSON-based database.

---

## ✨ Features

### 👤 User
- Register
- Login
- Change Password
- Strong password validation rules

### 🛡️ Admin
- Admin login/register (limited)
- List users
- Delete users

### 📦 Storage
- JSON-based persistent database (`user.json`, `admin.json`)

---

## 🛠 Run Project

```bash
python main.py
````

---

## 📌 Project Structure

```plaintext
PyAuth-Core/
├── User_Resitration_and_login/
│   ├── UserRegistration.py
│   ├── Database.py
│   ├── Admin.py
│   └── __init__.py
├── main.py
└── README.md
```

---

## 🚀 Roadmap

* [ ] Password hashing (bcrypt/argon2)
* [ ] Brute-force protection
* [ ] Logging system
* [ ] Convert to Django REST Framework API
* [ ] React + Tailwind frontend

---

## ⚠️ Note

This project is for learning purposes. Passwords are currently stored in plain text.

---

## 👤 Author

**Srikant Panda**