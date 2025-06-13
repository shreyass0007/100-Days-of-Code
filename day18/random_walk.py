from turtle import Turtle, Screen
import random
timmy=Turtle()
screen=Screen()
from turtle import Turtle, Screen
timmy.shape("arrow")
timmy.color("cyan")
Colors=['light cyan','spring green','magenta','deep pink','orange red','blue','yellow','snow']

move=[0,90,180,270]

for i in range(400):
    timmy.pensize(10)
    timmy.color(random.choice(Colors))
    timmy.speed(10)
    timmy.forward(30)
    timmy.setheading(random.choice(move))
        


screen.exitonclick()
