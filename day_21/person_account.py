class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List of tuples (amount, description)
        self.expenses = []  # List of tuples (amount, description)

    def add_income(self, amount, description):
        """Add income with its description"""
        self.incomes.append((amount, description))
        return True

    def add_expense(self, amount, description):
        """Add expense with its description"""
        self.expenses.append((amount, description))
        return True

    def total_income(self):
        """Calculate total income"""
        return sum([income[0] for income in self.incomes])

    def total_expense(self):
        """Calculate total expense"""
        return sum([expense[0] for expense in self.expenses])

    def account_balance(self):
        """Calculate account balance"""
        return self.total_income() - self.total_expense()

    def account_info(self):
        """Return account information"""
        info = f"Account Information:\n"
        info += f"Name: {self.firstname} {self.lastname}\n"
        info += f"Total Income: ${self.total_income():.2f}\n"
        info += f"Total Expenses: ${self.total_expense():.2f}\n"
        info += f"Balance: ${self.account_balance():.2f}\n"
        info += "\nIncome Details:\n"
        for amount, desc in self.incomes:
            info += f"- ${amount:.2f}: {desc}\n"
        info += "\nExpense Details:\n"
        for amount, desc in self.expenses:
            info += f"- ${amount:.2f}: {desc}\n"
        return info