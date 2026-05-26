# Accept a number from the user
user_input = input("Enter a number to check: ")

# Use try-except to handle cases where the user doesn't enter a valid number
try:
    # Convert the input to a float first to handle decimals
    number = float(user_input)
    
    # Check if the number is a positive integer greater than 0
    # is_integer() checks if a float value has no fractional part (e.g., 5.0 is an integer)
    if number > 0 and number.is_integer():
        print(f"Yes! {int(number)} is a natural number.")
    else:
        print(f"No! {user_input} is NOT a natural number.")

except ValueError:
    print("Invalid input! Please enter a valid number.")