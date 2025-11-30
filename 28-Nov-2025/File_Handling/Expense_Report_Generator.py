"""2. Expense Report Generator
 Create a function that accepts multiple expense items (name, amount) and writes a formatted expense
 report into report.txt """

write_line = lambda item,amount : f"{item}: Rs {amount}"

def write_expense_report(expense):
    total = sum(amount for item, amount in expense)

    with open("expense_report.txt", "w") as file:
        file.write("Expense Report\n")
        for item, amount in expense:
            file.write(write_line(item, amount) + "\n")
        file.write(f"Total: {total}\n")

expense = [("Food",200),("Clothes",800),("Travel",500)]
write_expense_report(expense)
print("Expense Report created")
