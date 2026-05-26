# 1. Take three numbers and store them in the variables
num1 = float(input("Enter the first number (num1): "))
num2 = float(input("Enter the second number (num2): "))
num3 = float(input("Enter the third number (num3): "))

# 2. Firstly check if num1 is greater than num2
if num1 > num2:
    # 3. If it is, then check if it is greater than num3
    if num1 > num3:
        # 4. If it is, then display the output
        print("num1 is the greatest among three")
    else:
        print("num3 is the greatest among three")
else:
    # If num1 was not greater than num2, check if num2 is greater than num3
    if num2 > num3:
        print("num2 is the greatest among three")
    else:
        print("num3 is the greatest among three")