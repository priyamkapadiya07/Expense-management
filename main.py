from file_handler import FileHandler
from expense_manager import ExpenseManager
from report_generator import ReportGenerator
from generate_pdf import ExpensesPDFGenerator
from send_email import EmailSender

def main():
    expense_manager = ExpenseManager()
    file_handler = FileHandler()
    pdf_generator = ExpensesPDFGenerator()
    email_sender = EmailSender()
    expense_manager.expenses = file_handler.load_expenses()

    while True:
        # print("\nExpense Management System")
        # print("1. Add Expense")
        # print("2. View Expenses")
        # print("3. Search Expenses")
        # print("4. Generate Report")
        # print("5. Export report")
        # print("6. Send Report")
        # print("7. Save data and Exit")
        print("                 ----------------------------------------------------------------------")
        print("                 | ------------------------------------------------------------------  |")
        print("                 | |                      *💸 EXPENSE TRACKER 💸*                    | |")
        print("                 | |                                                                 | |")
        print("                 | |     1.  Add Expense                                             | |")
        print("                 | |                                                                 | |")
        print("                 | |     2.  View Expenses                                           | |")
        print("                 | |                                                                 | |")
        print("                 | |     3.  Search Expenses                                         | |")
        print("                 | |                                                                 | |")
        print("                 | |     4.  Generate Report                                         | |")
        print("                 | |                                                                 | |")
        print("                 | |     5.  Export report                                           | |")
        print("                 | |                                                                 | |")
        print("                 | |     6.  Send Report                                             | |")
        print("                 | |                                                                 | |")
        print("                 | |     7.  Save data and Exit                                      | |")
        print("                 | |                                                                 | |")
        print("                 | ------------------------------------------------------------------  |")
        print("                 ----------------------------------------------------------------------")
        choice = input("\nEnter choice: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").lower()
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            expense_manager.add_expense(amount, category, date, description)
            print("Expense added successfully!")

        elif choice == "2":
            expense_manager.list_expenses()

        elif choice == "3":
            # print("Search Expenses by:")
            # print("1. Category")
            # print("2. Date")
            # print("3. Amount")
            # print("4. Multiple filters (Category, Date, Amount)")
            print("                   ----------------------------------------------------------------- ")
            print("                  |                      *🔍 Search Expenses by : *                 |")
            print("                  |                                                                 |")
            print("                  |     1.  Category                                                |")
            print("                  |     2.  Date                                                    |")
            print("                  |     3.  Amount                                                  |")
            print("                  |     4.  Multiple filters (Category, Date, Amount)               |")
            print("                  |                                                                 |")
            print("                   -----------------------------------------------------------------")
            search_choice = input("\nEnter search choice: ")

            if search_choice == "1":
                category = input("\nEnter category to search: ")
                results = expense_manager.search_expenses(category=category)
                if results:
                    for expense in results:
                        print(expense)
                else:
                    print(f"No expenses found for category: {category}")
            
            elif search_choice == "2":
                date = input("\nEnter date (YYYY-MM-DD) to search: ")
                results = expense_manager.search_expenses(date=date)
                if results:
                    for expense in results:
                        print(expense)
                else:
                    print(f"No expenses found for date: {date}")

            elif search_choice == "3":
                amount = float(input("Enter amount to search: "))
                results = expense_manager.search_expenses(amount=amount)
                if results:
                    for expense in results:
                        print(expense)
                else:
                    print(f"No expenses found for amount: {amount}")

            elif search_choice == "4":
                category = input("Enter category to search: ")
                date = input("Enter date (YYYY-MM-DD) to search: ")
                amount = float(input("Enter amount to search: "))
                results = expense_manager.search_expenses(amount=amount, category=category, date=date)
                if results:
                    for expense in results:
                        print(expense)
                else:
                    print(f"No expenses found with the filters: Category: {category}, Date: {date}, Amount: {amount}")

        elif choice == "4":
            report_generator = ReportGenerator(expense_manager)
            print("1. Generate Pie Chart")
            print("2. Generate Bar Chart")
            print("3. Generate Summary")
            report_choice = input("Enter choice: ")

            if report_choice == "1":
                report_generator.generate_pie_chart()
            elif report_choice == "2":
                report_generator.generate_bar_chart()
            elif report_choice == "3":
                report_generator.generate_summary()
        
        elif choice=="5":
                pdf_generator.generate_pdf()
                print("\n📄 PDF generated successfully")
        
        elif choice == "6":
            email_sender.send_email()

        elif choice == "7":
            file_handler.save_expenses(expense_manager.expenses)
            print("\nExpenses saved. Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
