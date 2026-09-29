expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item: ")
        amount = int(input("Enter amount: "))

        expenses.append({
            "item": item,
            "amount": amount
        })

    elif choice == "2":
        for expense in expenses:
            print(expense["item"], "-", expense["amount"])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total:", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
