import math

class Circle:
    # Constructor to initialize the radius of the circle
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate and return the area of the circle
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate and return the perimeter (circumference)
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# --- Main Program Execution ---
def main():
    print("--- Circle Area & Perimeter Calculator ---")
    
    try:
        # Taking radius input from the user
        user_radius = float(input("Enter the radius of the circle: "))
        
        if user_radius < 0:
            print("Radius cannot be negative! Please enter a valid positive number.")
            return

        # Creating an object (instance) of the Circle class
        my_circle = Circle(user_radius)

        # Calculating results using the object's methods
        area = my_circle.calculate_area()
        perimeter = my_circle.calculate_perimeter()

        # Displaying the results rounded to 2 decimal places
        print("\n--- Results ---")
        print(f"Radius: {user_radius}")
        print(f"Area of the Circle: {area:.2f}")
        print(f"Perimeter of the Circle: {perimeter:.2f}")
        
    except ValueError:
        print("Invalid input! Please enter a numeric value for the radius.")

# Run the program
if __name__ == "__main__":
    main()