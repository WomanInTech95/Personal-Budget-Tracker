class BudgetTracker:
    def __init__(self, initial_budget):
        self.budget = initial_budget
        self.expenses = []

    def add_expense(self, amount, description):
        if amount <= 0:
            print("Expense must be a positive amount.")
            return
        self.expenses.append({'amount': amount, 'description': description})
        print(f"Added expense: {description} - ${amount:.2f}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("\nExpenses:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['description']}: ${expense['amount']:.2f}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")
        return total

    def budget_balance(self):
        total = self.total_expenses()
        balance = self.budget - total
        print(f"Budget Balance: ${balance:.2f}")
        return balance

def main():
    initial_budget = float(input("Enter your initial budget: "))
    tracker = BudgetTracker(initial_budget)

    while True:
        print("\nBudget Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Budget Balance")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter expense amount: "))
            description = input("Enter expense description: ")
            tracker.add_expense(amount, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            tracker.budget_balance()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
