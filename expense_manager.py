from expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, date, description):
        new_expense = Expense(amount, category, date, description)
        self.expenses.append(new_expense)

    # def remove_expense(self, index):
    #     if 0 <= index < len(self.expenses):
    #         del self.expenses[index]
    #     else:
    #         print("Invalid index")

    def list_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        for i, expense in enumerate(self.expenses):
            print(f"{i + 1}. {expense}")

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def filter_expenses(self, category=None, date=None):
        filtered_expenses = self.expenses
        if category:
            filtered_expenses = [e for e in filtered_expenses if e.category.lower() == category.lower()]
        if date:
            filtered_expenses = [e for e in filtered_expenses if e.date == date]
        return filtered_expenses
    
    def search_expenses(self, amount=None, category=None, date=None):
        # Use filter_expenses to simplify
        filtered_expenses = self.filter_expenses(category, date)
        
        if amount:
            filtered_expenses = [e for e in filtered_expenses if e.amount == amount]
        
        return filtered_expenses
