def is_disarium(number):
    # Convert the number to a string to easily loop through digits and track positions
    num_str = str(number)
    total_sum = 0
    
    # Loop through each digit with its 1-based position index
    for index, digit in enumerate(num_str):
        position = index + 1
        # Raise the digit to the power of its position and add to the sum
        total_sum += int(digit) ** position
        
    # Check if the calculated sum matches the original number
    return total_sum == number

# --- Main Program ---
def main():
    print("--- Disarium Number Checker ---")
    try:
        # Take input from the user
        user_input = int(input("Enter a number to check: "))
        
        # Call the function and print the result
        if is_disarium(user_input):
            print(f"Yes! {user_input} is a Disarium number. 🎉")
        else:
            print(f"No, {user_input} is not a Disarium number.")
            
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

# Run the program
if __name__ == "__main__":
    main()