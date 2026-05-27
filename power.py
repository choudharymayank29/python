# --- Power Series Printer ---

def print_power_series():
    try:
        # Step 1: Accept the number of terms (n) from the user
        n = int(input("Enter the number of terms you want to print: "))
        
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
            return
            
        print(f"\nPower series up to {n} terms:")
        
        # Step 2: Use a for loop to calculate and print each term
        # range(1, n + 1) generates numbers from 1 up to n
        for i in range(1, n + 1):
            term = i ** i  # Raises the number to the power of itself
            
            # Formatting to print terms on the same line separated by commas
            if i < n:
                print(term, end=", ")
            else:
                print(term) # Prints the last term cleanly without a trailing comma
                
    except ValueError:
        print("Invalid input! Please enter a valid whole number.")

# Run the program
if __name__ == "__main__":
    print_power_series()