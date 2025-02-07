import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from datetime import datetime
import csv
import matplotlib.pyplot as plt

class TransactionManager:
    def __init__(self):
        self.budget_limit = None  # Budget limit feature

    def get_connection(self):
        return sqlite3.connect("transactions.db")
    
    def create_table(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL,
                category TEXT,
                subcategory TEXT,
                type TEXT,
                date TEXT
            )
        """)
        conn.commit()
        conn.close()
    
    def add_transaction(self):
        add_window = tk.Toplevel(root)
        add_window.title("Add Transaction")
        
        tk.Label(add_window, text="Amount:").pack()
        amount_var = tk.StringVar()
        tk.Entry(add_window, textvariable=amount_var).pack()
        
        tk.Label(add_window, text="Category:").pack()
        category_var = tk.StringVar()
        tk.Entry(add_window, textvariable=category_var).pack()
        
        tk.Label(add_window, text="Subcategory:").pack()
        subcategory_var = tk.StringVar()
        tk.Entry(add_window, textvariable=subcategory_var).pack()
        
        tk.Label(add_window, text="Type:").pack()
        type_var = tk.StringVar(value="income")
        tk.OptionMenu(add_window, type_var, "income", "expense").pack()
        
        def save_transaction():
            amount = float(amount_var.get())
            category = category_var.get()
            subcategory = subcategory_var.get()
            type = type_var.get()
            date = datetime.now().strftime("%Y-%m-%d")
            
            if self.budget_limit and type == "expense" and amount > self.budget_limit:
                messagebox.showwarning("Budget Alert", "Expense exceeds the budget limit!")
            
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO transactions (amount, category, subcategory, type, date) VALUES (?, ?, ?, ?, ?)",
                           (amount, category, subcategory, type, date))
            conn.commit()
            conn.close()
            add_window.destroy()
            update_transaction_list()
            messagebox.showinfo("Success", "Transaction Added Successfully!")
        
        tk.Button(add_window, text="Save", command=save_transaction).pack()
    
    def get_transactions(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        transactions = cursor.fetchall()
        conn.close()
        return transactions
    
    def get_summary(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        total_income = cursor.fetchone()[0] or 0
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        total_expense = cursor.fetchone()[0] or 0
        conn.close()
        messagebox.showinfo("Summary", f"Total Income: {total_income}\nTotal Expense: {total_expense}\nNet Balance: {total_income - total_expense}")
    
    def delete_transaction(self):
        transaction_id = simpledialog.askinteger("Delete Transaction", "Enter transaction ID to delete:")
        if transaction_id:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Transaction deleted.")
            update_transaction_list()
    
    def delete_all_transactions(self):
        if messagebox.askyesno("Delete All Transactions", "Are you sure you want to delete all transactions?"):
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions")
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "All transactions deleted.")
            update_transaction_list()
    
    def visualize_pie_chart(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
        data = cursor.fetchall()
        conn.close()
        if data:
            categories, amounts = zip(*data)
            plt.figure(figsize=(6, 6))
            plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90)
            plt.title("Expense Breakdown")
            plt.show()
        else:
            messagebox.showinfo("No Data", "No expense data available to visualize.")
    
    def set_budget_limit(self):
        limit = simpledialog.askfloat("Set Budget", "Enter your monthly budget limit:")
        if limit:
            self.budget_limit = limit
            messagebox.showinfo("Success", f"Budget limit set to {limit}")

def update_transaction_list():
    transaction_list.delete(0, tk.END)
    transactions = manager.get_transactions()
    for transaction in transactions:
        transaction_list.insert(tk.END, f"{transaction[0]} - {transaction[4].capitalize()}: {transaction[1]:,.2f} ({transaction[2]} - {transaction[3]}) on {transaction[5]}")

manager = TransactionManager()
manager.create_table()
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("450x650")
root.configure(bg="#2C2F33")  # Dark Mode Background

transaction_list = tk.Listbox(root, width=55, height=15, bg="#23272A", fg="white")
transaction_list.pack(padx=10, pady=10)

tk.Button(root, text="Add Transaction", command=manager.add_transaction, bg="#7289DA", fg="white").pack()
tk.Button(root, text="View Summary", command=manager.get_summary, bg="#99AAB5", fg="black").pack()
tk.Button(root, text="Delete Transaction", command=manager.delete_transaction, bg="#F04747", fg="white").pack()
tk.Button(root, text="Delete All Transactions", command=manager.delete_all_transactions, bg="#F04747", fg="white").pack()
tk.Button(root, text="Visualize Pie Chart", command=manager.visualize_pie_chart, bg="#FAA61A", fg="black").pack()
tk.Button(root, text="Set Budget Limit", command=manager.set_budget_limit, bg="#43B581", fg="white").pack()

update_transaction_list()
root.mainloop()
