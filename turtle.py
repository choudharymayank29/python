import turtle

# Set up the screen and the turtle
screen = turtle.Screen()
screen.bgcolor("white") # Sets a clean background color

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(2) # Sets a smooth drawing speed


# --- 1. DRAW A TRIANGLE ---
my_turtle.color("blue") # Set the color for the triangle
my_turtle.pensize(3)

print("Drawing a triangle...")
for _ in range(3):
    my_turtle.forward(100)  # Length of each side
    my_turtle.left(120)     # Exterior angle for an equilateral triangle


# --- Move the turtle away so the shapes don't overlap ---
my_turtle.penup()
my_turtle.goto(-150, -50) 
my_turtle.pendown()


# --- 2. DRAW A RECTANGLE ---
my_turtle.color("red") # Set a different color for the rectangle
my_turtle.pensize(3)

print("Drawing a rectangle...")
for _ in range(2):
    my_turtle.forward(150) # Width of the rectangle
    my_turtle.left(90)
    my_turtle.forward(80)  # Height of the rectangle
    my_turtle.left(90)


# Keep the window open until you click on it
screen.exitonclick()