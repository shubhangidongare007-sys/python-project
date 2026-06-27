# Project 3 : Personal Expense Tracker

# Create empty expense list
expenses = []

# Input monthly budget
budget = float(input("Enter Monthly Budget: Rs. "))

while True:

    # Display Menu
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    # Add Expense
    if choice == "1":
        desc = input("Enter Description: ")
        category = input("Enter Category (Food/Travel/Bills/Entertainment/Other): ")
        amount = float(input("Enter Amount: "))
        date = input("Enter Date (DD-MM-YYYY): ")

        expense = {
            "description": desc,
            "category": category,
            "amount": amount,
            "date": date
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

    # View All Expenses
    elif choice == "2":

        print("\n----- Expense List -----")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for i, e in enumerate(expenses, start=1):
                print(i, e["description"], e["category"],
                      e["amount"], e["date"])

    # Category Summary
    elif choice == "3":

        summary = {}

        for e in expenses:
            cat = e["category"]

            if cat in summary:
                summary[cat] += e["amount"]
            else:
                summary[cat] = e["amount"]

        print("\n----- Category Summary -----")

        for cat, total in summary.items():
            print(cat, ":", total)

    # Budget Report
    elif choice == "4":

        total = 0

        for e in expenses:
            total += e["amount"]

        remaining = budget - total
        percent = (total / budget) * 100

        print("\n----- BUDGET REPORT -----")
        print("Total Spent :", total)
        print("Budget Limit :", budget)
        print("Remaining :", remaining)
        print("Used :", round(percent, 2), "%")

        if percent >= 100:
            print("WARNING : Budget Exceeded!")

        elif percent >= 80:
            print("WARNING : You have used 80% of your budget!")

        # Top Spending Category
        summary = {}

        for e in expenses:
            cat = e["category"]

            if cat in summary:
                summary[cat] += e["amount"]
            else:
                summary[cat] = e["amount"]

        if len(summary) > 0:
            top_category = max(summary, key=summary.get)
            print("Top Category :", top_category,
                  "(Rs.", summary[top_category], ")")

    # Exit Program
    elif choice == "5":
        print("Thank You!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice!")