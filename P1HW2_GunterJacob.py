#Jacob Gunter
#09/23/2025
#P1HW2
#Make a program that does basic math on numbers that are entered.



print ("This program calculates and displays travel expenses")
# Ask user to enter their budget
budget = float(input("Enter your travel budget: $"))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas_expense = float(input("Enter the amount you will spend on gas: $"))

# Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

# Ask user for amount they will spend on food
food_expense = float(input("Enter the amount you will spend on food: $"))

# Add all expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print("\n------ Budget Summary ------")
print(f"Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")


