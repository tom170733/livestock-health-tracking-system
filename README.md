# Livestock Health & Tracking System

## 📌 Project Overview
This Python application is an Object-Oriented Programming (OOP) solution developed for the **PROG211** module at Limkokwing University of Creative Technology[cite: 1, 2, 3]. It is designed to solve real-world agricultural challenges by managing livestock registrations, tracking individual animal health logs, assessing body temperature risks, and ensuring persistent data storage.

---

## 🚀 Key Features & OOP Concepts Applied
- **Classes and Objects**: Implements core classes (`Livestock` and `FarmManager`) with distinct attributes (tag ID, species, age, breed, origin data, and health logs) and interactive methods.
- **Python Data Structures (Task 2)**: Utilizes a **dictionary** data structure where unique animal tag IDs serve as keys for efficient, O(1) data retrieval and record management[cite: 2].
- **Tuples (Extra Marks)**: Implements an immutable **tuple** (`origin_info`) to securely store farm origin location and registration dates, preventing accidental data modification[cite: 2].
- **Methods Implementation (Task 3)**:
  - *Instance Methods*: `update_health_status()` and `display_info()` manage and display individual animal records[cite: 2].
  - *Class Method (`@classmethod`)*: `get_total_animals()` tracks system-wide animal statistics across the application[cite: 2].
  - *Static Method (`@staticmethod`)*: `assess_health_risk()` evaluates body temperature readings to provide immediate health risk diagnostics[cite: 2].

---

## 🌍 Digital Public Goods (DPG) Alignment
This project adheres strictly to Digital Public Goods principles:
1. **Open-Source**: Published publicly on GitHub to ensure transparency, community collaboration, and educational reusability[cite: 1, 2].
2. **Privacy-Respecting**: The system stores zero sensitive personal user data, focusing exclusively on pseudonymous agricultural asset tags and animal health records[cite: 1, 2].
3. **Inclusive & Accessible**: Designed with a lightweight, user-friendly command-line interface that requires minimal hardware resources, making it practical for rural farmers and local extension workers.
4. **Modular & Reusable**: Built using a decoupled object-oriented architecture (`Livestock` asset logic separated from `FarmManager` registry control) for seamless scalability[cite: 1, 2].

---

## 🛠️ How to Run the Program
1. Ensure you have Python installed on your machine.
2. Clone or download this repository.
3. Open your terminal or IDE (such as PyCharm) inside the project directory.
4. Run the main script:
   ```bash
   python main.py