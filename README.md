User Registration & Authentication System

A modular Python-based authentication system demonstrating Object-Oriented Programming (OOP) principles and the separation of application logic from data persistence.
🚀 Overview

This project serves as a foundational backend system. It splits the responsibility of user management into two distinct layers:

    Registration Logic: Handles user input and credential gathering.

    Database Management: Handles the storage and retrieval of user records.

By decoupling these components, the system mimics real-world backend architectures (like Django's model-view structure), making the code easier to debug, test, and scale.
🛠️ Project Structure

The project is organized into a package for better modularity:
Plaintext

User_Registration_and_login/
├── UserRegistration.py  # Contains logic for user input & validation
├── Database.py          # Handles data persistence (save/load)
└── main.py              # Entry point for the application

✨ Features

    Separation of Concerns: Distinct classes for UI/Registration and Database storage.

    OOP Implementation: Uses Python classes to manage state and behavior.

    Data Persistence: Saves registered user credentials to a simulated database.

    Clean Authentication Flow: A simple CLI interface for users to choose between login and registration.

💻 Usage

To run the project, ensure you are in the root directory and execute:
Bash

python main.py

Example Flow:

    Run the script.

    Type register when prompted.

    Enter your desired username and password (validated by the UserRegistration class).

    The Database class will then capture and store your credentials.

🛡️ Security Roadmap (Red Team Goals)

As part of my journey into cybersecurity, I plan to enhance this project with:

    [ ] Password Hashing: Implementing bcrypt or argon2 to avoid storing plain-text passwords.

    [ ] Paranoid Validation: Integrating my Password Validator project to enforce high-entropy credentials.

    [ ] SQL Injection Prevention: Transitioning to a SQL-based backend using prepared statements.

👤 Author

Srikant Panda

    B.Tech Student (4th Semester)

    Aspiring Red Team / Cybersecurity Professional

    Python & Django Enthusiast