import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
spiro = turtle.Turtle()
spiro.speed(0)  # Fastest drawing speed
turtle.colormode(255)  # Use RGB color mode

def draw_spirograph(size_of_gap):
    for angle in range(0, 360, size_of_gap):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        spiro.pencolor(r, g, b)
        spiro.circle(100)
        spiro.setheading(angle)

# Call the function
draw_spirograph(5)

# Exit on click
screen.exitonclick()
