# Create the dictionary as specified in the story
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Print the dictionary so the user knows what keys are available
print("Available keys in the dictionary:", list(d.keys()))

# Take the key input from the user and convert it to an integer
user_input = input("Enter the key to find its value: ")

try:
    key = int(user_input)
    
    # Check if the key exists in the dictionary
    if key in d:
        # Return and print the value of the key
        print(f"The value for key {key} is: {d[key]}")
    else:
        print(f"Key {key} is not found in the dictionary.")
        
except ValueError:
    print("Invalid input! Please enter a valid integer key.")