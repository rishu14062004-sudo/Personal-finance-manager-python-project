import csv
import os
from datetime import datetime
from charts import show_pie_chart, show_bar_chart


# Create CSV file
def create_file():
    if not os.path.exists("transactions.csv"):
        with open("transactions.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Type", "Category", "Amount"])


# Display Menu
def main_menu():
    print("\n" + "=" * 45)
    print("     SMART PERSONAL FINANCE TRACKER")
    print("=" * 45)
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Check Balance")
    print("5. Show Expense Distribution (Pie Chart)")
    print("6. Show Income vs Expense Comparison (Bar Chart)")
    print("7. Exit")
    print("=" * 45)


# Add Income
def add_income():
    try:
        amount = float(input("Enter Income Amount: ₹"))
    except ValueError:
        print("Invalid Amount!")
        return

    category = input("Enter Income Category: ")

    date = datetime.now().strftime("%d-%m-%Y")

    with open("transactions.csv", "r") as file:
        transaction_id = sum(1 for row in file)

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_id, date, "Income", category, amount])

    print("Income Added Successfully!")


# Add Expense
def add_expense():
    try:
        amount = float(input("Enter Expense Amount: ₹"))
    except ValueError:
        print("Invalid Amount!")
        return

    category = input("Enter Expense Category: ")

    date = datetime.now().strftime("%d-%m-%Y")

    with open("transactions.csv", "r") as file:
        transaction_id = sum(1 for row in file)

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_id, date, "Expense", category, amount])

    print("Expense Added Successfully!")


# View Transactions
# View Transactions
def view_transactions():
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)

        # Skip the header
        next(reader)

        # Store all transactions in a list
        transactions = list(reader)

        # Check if there are any transactions
        if len(transactions) == 0:
            print("\nNo transactions found.")
            return

        print("\n")
        print("{:<5} {:<12} {:<10} {:<15} {:<10}".format(
            "ID", "Date", "Type", "Category", "Amount"))
        print("-" * 60)

        # Display all transactions
        for row in transactions:
            print("{:<5} {:<12} {:<10} {:<15} ₹{:<10}".format(
                row[0], row[1], row[2], row[3], row[4]))

# Check Balance
def check_balance():
    income = 0
    expense = 0

    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[2] == "Income":
                income += float(row[4])
            elif row[2] == "Expense":
                expense += float(row[4])

    balance = income - expense

    print("\n" + "=" * 40)
    print("         FINANCIAL SUMMARY")
    print("=" * 40)
    print(f"Total Income   : ₹{income:.2f}")
    print(f"Total Expense  : ₹{expense:.2f}")
    print("-" * 40)
    print(f"Current Balance: ₹{balance:.2f}")
    print("=" * 40)
# Main Program
create_file()

while True:
    main_menu()

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        print("Option 4 Selected")
        check_balance()

    elif choice == "5":
        show_pie_chart()

    elif choice == "6":
        show_bar_chart()

    elif choice == "7":
        print("\nThank you for using Personal Finance Manager.")
        break

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")