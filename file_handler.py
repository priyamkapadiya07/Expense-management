import json
import os
from expense import Expense

class FileHandler:
    @staticmethod
    def save_expenses(expenses, filename="expenses.json"):
        with open(filename, 'w') as file:
            json.dump([expense.__dict__ for expense in expenses], file)

    @staticmethod
    def load_expenses(filename="expenses.json"):
        expenses = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    expenses.append(Expense(item['amount'], item['category'], item['date'], item['description']))
        return expenses
