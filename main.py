# Function to calculate the bonus based on the productivity score
def calculate_bonus(name, num_shifts, num_transactions, transaction_value):
    # Calculate the productivity score
    productivity_score = (transaction_value / num_transactions) / num_shifts
    
    # Determine the bonus based on the productivity score
    if productivity_score <= 30:
        bonus = 50.00
    elif 31 <= productivity_score <= 69:
        bonus = 75.00
    elif 70 <= productivity_score <= 199:
        bonus = 100.00
    else:
        bonus = 200.00
    
    # Print the employee's name and bonus
    print(f"Employee Name: {name}")
    print(f"Productivity Score: {productivity_score:.2f}")
    print(f"Bonus: ${bonus:.2f}")


# Input values
employee_name = "Kim Smith"
num_shifts = 25
num_transactions = 75
transaction_value = 40000.00

# Call the function to calculate the bonus
calculate_bonus(employee_name, num_shifts, num_transactions, transaction_value)
