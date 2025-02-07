# 📊 Personal Finance Tracker

A **Personal Finance Tracker** built using Python and Tkinter, designed to help users efficiently manage their income, expenses, and budget. The application provides a **simple yet powerful** interface to track financial transactions and visualize spending habits.

---

## 🚀 Features

### 📌 **1. Add Transaction**
- Allows users to add a new transaction.
- Requires input fields:
  - **Amount** – Enter the transaction amount.
  - **Category** – Select or input a category (e.g., Food, Transport, Salary, etc.).
  - **Subcategory** – Further refine your transaction details.
  - **Type** – Choose between `Income` or `Expense`.
- The transaction is stored in an SQLite database.
- If an **expense exceeds the budget limit**, a warning is displayed.

### 📌 **2. View Summary**
- Displays a summary of:
  - **Total Income**
  - **Total Expenses**
  - **Net Balance (Income - Expenses)**

### 📌 **3. Delete Transaction**
- Allows users to **delete a specific transaction** by entering its unique ID.
- Ensures accidental deletion is avoided.

### 📌 **4. Delete All Transactions**
- Provides an option to **clear all transaction history**.
- Asks for confirmation before performing this action.

### 📌 **5. Visualize Pie Chart**
- Generates a **pie chart of expenses** categorized by spending areas.
- Helps users identify where most of their money is being spent.

### 📌 **6. Set Budget Limit**
- Allows users to **set a monthly budget limit**.
- If an added expense **exceeds this limit**, a warning message appears.

### 📌 **7. Transaction List**
- Displays all transactions in a structured format:
  - `ID - Type: Amount (Category - Subcategory) on Date`
- Automatically updates after adding or deleting transactions.

---

## 📦 Installation

### 🖥 Requirements
Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

### ⚙️ Setup
1. **Clone the Repository** (or Download ZIP):
   ```sh
   git clone https://github.com/your-username/finance-tracker.git
   cd finance-tracker
   ```
2. **Install Required Libraries:**
   ```sh
   pip install matplotlib
   ```
3. **Run the Application:**
   ```sh
   python transactions.py
   ```

---

## 📸 Screenshots
(Add images of the application interface here)

---

## 🛠️ Technologies Used
- **Python** – Core application logic
- **Tkinter** – GUI for user interaction
- **SQLite** – Database for storing transactions
- **Matplotlib** – Visualization (Pie Chart)

---

## 📝 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature-xyz`).
3. Commit your changes.
4. Push to the branch and submit a PR.

---

## 📧 Contact
For any queries or suggestions, feel free to contact me .

---

⭐ **If you like this project, don't forget to star the repository!** ⭐
