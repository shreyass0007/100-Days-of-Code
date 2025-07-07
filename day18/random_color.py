from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)  # This is needed to use RGB values in 0-255 range

timmy.shape("arrow")

def random_choice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

move = [0, 90, 180, 270]

for i in range(400):
    timmy.pensize(10)
    timmy.color(random_choice())
    timmy.speed(10)
    timmy.forward(30)
    timmy.setheading(random.choice(move))

screen.exitonclick()