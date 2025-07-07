from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)  # Set color mode to accept 0-255 RGB values

timmy.shape("arrow")

def random_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.speed("fastest")  # Alternative to timmy.speed(10)
def draw_spirograph(sizeofcircle):
    for i in range(int(360/sizeofcircle)):
        timmy.color(random_choice())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+sizeofcircle)
draw_spirograph(5)

screen.exitonclick()  # Use the screen object we created