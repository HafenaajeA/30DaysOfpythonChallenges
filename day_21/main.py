from statistics_class import Statistics
from person_account import PersonAccount

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.var())
print('Frequency Distribution: ', data.freq_dist())

# Create a new account
person = PersonAccount("John", "Doe")

# Add some incomes
person.add_income(3000, "Monthly Salary")
person.add_income(500, "Freelance Work")
person.add_income(200, "Online Sales")

# Add some expenses
person.add_expense(1200, "Rent")
person.add_expense(200, "Utilities")
person.add_expense(500, "Groceries")
person.add_expense(300, "Transportation")

# Print account information
print(person.account_info())

# Print specific calculations
print(f"Total Income: ${person.total_income():.2f}")
print(f"Total Expenses: ${person.total_expense():.2f}")
print(f"Account Balance: ${person.account_balance():.2f}")