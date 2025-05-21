import matplotlib.pyplot as plt
import numpy as np

class ReportGenerator:
    def __init__(self, expense_manager):
        self.expense_manager = expense_manager

    def generate_pie_chart(self):
        categories = np.array([expense.category for expense in self.expense_manager.expenses])
        unique_categories = np.unique(categories)
        category_totals = np.array([sum(expense.amount for expense in self.expense_manager.expenses if expense.category == category) for category in unique_categories])

        labels = unique_categories
        sizes = category_totals

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.show()

    # def generate_bar_chart(self):
    #     categories = np.array([expense.category for expense in self.expense_manager.expenses])
    #     unique_categories = np.unique(categories)
    #     category_totals = np.array([sum(expense.amount for expense in self.expense_manager.expenses if expense.category == category) for category in unique_categories])

    #     plt.bar(unique_categories, category_totals)
    #     plt.xlabel('Categories')
    #     plt.ylabel('Total Expense')
    #     plt.title('Expenses by Category')
    #     plt.grid()
    #     plt.show()
        
    def generate_bar_chart(self):
        categories = np.array([expense.category for expense in self.expense_manager.expenses])
        unique_categories = np.unique(categories)
        category_totals = np.array([sum(expense.amount for expense in self.expense_manager.expenses if expense.category == category) for category in unique_categories])

        max_index = np.argmax(category_totals)
        colors = ['blue'] * len(unique_categories)
        colors[max_index] = 'red'

        plt.bar(unique_categories, category_totals, color=colors)
        plt.xlabel('Categories')
        plt.ylabel('Total Expense')
        plt.title('Expenses by Category')
        plt.grid()
        plt.show()

    def generate_summary(self):
        total_expenses = np.sum([expense.amount for expense in self.expense_manager.expenses])
        print(f"Total Expenses: {total_expenses}")
