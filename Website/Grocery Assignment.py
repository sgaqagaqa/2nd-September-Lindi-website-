class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    def search_expenses(self, query):
        matching_expenses = []
        for expense in self.expenses:
            if (query.lower() in expense['Item'].lower() or
                query.lower() in expense['Category'].lower() or
                query.lower() in str(expense['Price'])):
                matching_expenses.append(expense)
        return matching_expenses
        
    def add_expense(self, item_name, price, category):
        self.expenses.append({'Item': item_name, 'Price': price, 'Category': category})
        
    def save_to_file(self):
        with open("expenses.txt", "w") as file: 
            for expense in self.expenses:
                file.write(f"Item: {expense['Item']}, Price: {expense['Price']}, Category: {expense['Category']}\n")

    def load_from_file(self):
        with open("expenses.txt", "r") as file:
            for line in file:
                if line.strip():  # Check if line is not empty
                    item, price, category = line.strip().split(", ")
                    item_name = item.split(": ")[1]
                    price = float(price.split(": ")[1]) 
                    category = category.split(": ")[1] 
                    self.expenses.append({'Item': item_name, 'Price': price, 'Category': category})

    def calculate_total_expenses(self):
        return sum(expense['Price'] for expense in self.expenses)

    def generate_summary_report(self):
        categories = set(expense['Category'] for expense in self.expenses)
        summary = {category: 0 for category in categories} 
        for expense in self.expenses:
            summary[expense['Category']] += expense['Price']
        return summary

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Item: {expense['Item']}, Price: R{expense['Price']}, Category: {expense['Category']}")

    
    def test_add_expense():
        tracker = ExpenseTracker()
        tracker.add_expense("Banana", 15, "Fruits")
        assert len(tracker.expenses) == 1
        assert tracker.expenses[0]['Item'] == "Banana"
        assert tracker.expenses[0]['Price'] == 15
        assert tracker.expenses[0]['Category'] == "Fruits"
        print("Test case add expense has passed")
        

    def test_calculate_total_expenses():
        tracker = ExpenseTracker()
        tracker.add_expense("Banana", 15, "Fruits")
        tracker.add_expense("Spinach", 35, "Vegetable")
        tracker.add_expense("Inkhomazi", 30, "Dairy")
        assert tracker.calculate_total_expenses() == 80
        print("Total expense function has passed")
        
    
    def test_generate_summary_report():
        tracker = ExpenseTracker()
        tracker.add_expense("Banana", 15, "Fruits")
        tracker.add_expense("Spinach", 35, "Vegetable")
        tracker.add_expense("Inkhomazi", 30, "Dairy")
        summary = tracker.generate_summary_report()
        assert len(summary) == 3
        assert summary["Fruits"] == 15
        assert summary["Vegetable"] == 35
        assert summary["Dairy"] == 30
        print("Generate summary report passed")

def main(): 
    tracker = ExpenseTracker()
    tracker.load_from_file()

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Search Expenses\n4. Generate Summary Report\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            item_name = input("Enter the item name: ")
            price = float(input("Enter the price: "))
            category = input("Enter the category: ")
            tracker.add_expense(item_name, price, category)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            query = input("Enter search query: ")
            matching_expenses = tracker.search_expenses(query)
            if matching_expenses:
                print("Matching Expenses:")
                for expense in matching_expenses:
                    print(f"Item: {expense['Item']}, Price: R{expense['Price']}, Category: {expense['Category']}")
            else:
                print("No matching expenses found.")
        elif choice == '4':
            summary = tracker.generate_summary_report()
            for category, total in summary.items():
                print(f"{category}: R{total}")
            print(f"Total Expenses: R{tracker.calculate_total_expenses()}")
        elif choice == '5':
            tracker.save_to_file()
            print("Exiting Program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
