import json
import os

# File to store expense data
DATA_FILE = "expenses.json"

# Load data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add a new expense
def add_expense(expenses):
    category = input("Enter category (e.g., Food, Travel, Entertainment): ").strip()
    amount = float(input("Enter amount: "))
    description = input("Enter description: ").strip()
    expenses.append({"category": category, "amount": amount, "description": description})
    save_data(expenses)
    print("Expense added successfully!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']} - ₹{expense['amount']:.2f} ({expense['description']})")

# Analyze expenses by category
def analyze_expenses(expenses):
    if not expenses:
        print("No expenses to analyze.")
        return
    category_totals = {}
    for expense in expenses:
        category_totals[expense['category']] = category_totals.get(expense['category'], 0) + expense['amount']
    
    print("\nExpense Analysis:")
    for category, total in category_totals.items():
        print(f"{category}: ₹{total:.2f}")

# Main menu
def main():
    expenses = load_data()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            analyze_expenses(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
