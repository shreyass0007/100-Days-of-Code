from turtle import Turtle, Screen
import random
timmy=Turtle()
screen=Screen()
from turtle import Turtle, Screen
timmy.shape("arrow")
timmy.color("cyan")
Colors=['light cyan','spring green','magenta','deep pink','orange red','blue','yellow','snow']

def Shape(shape):
    angle=360/shape
    for i in range (shape):
        timmy.forward(100)
        timmy.right(angle)
        

for i in range(3,10):
    timmy.color(random.choice(Colors))
    Shape(i)
 
screen.exitonclick()
