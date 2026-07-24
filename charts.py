import csv
import matplotlib.pyplot as plt


# Pie Chart for Expense Categories
def show_pie_chart():
    categories = {}
    
    with open("transactions.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[2] == "Expense":
                category = row[3]
                amount = float(row[4])

                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

    if len(categories) == 0:
        print("No expense data available.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Expense Distribution by Category")
    plt.show()


# Bar Chart for Income vs Expense
def show_bar_chart():
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

    labels = ["Income", "Expense"]
    amounts = [income, expense]

    plt.figure(figsize=(6, 5))
    plt.bar(labels, amounts)
    plt.title("Income vs Expense Comparison")
    plt.xlabel("Type")
    plt.ylabel("Amount (₹)")
    plt.show()