# Function to add two numbers
def addition(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def multiplication(num1, num2):
    return num1 * num2

# 1. Accept two numbers from the user
# We use float() so the calculator can handle both whole numbers and decimals
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# 2. Give the user the option to choose an operation
print("\nChoose an operation:")
print("1. Addition")
print("2. Multiplication")

choice = input("Enter your choice (1 or 2): ")

# 3. Perform the calculation based on the user's choice using conditional statements
if choice == '1':
    result = addition(number1, number2)
    print(f"\nThe sum of {number1} and {number2} is: {result}")
    
elif choice == '2':
    result = multiplication(number1, number2)
    print(f"\nThe product of {number1} and {number2} is: {result}")
    
else:
    print("\nInvalid choice! Please run the program again and select either 1 or 2.")
    