from turtle import Turtle, Screen
timmy=Turtle()
screen=Screen()
from turtle import Turtle, Screen
timmy.shape("turtle")
timmy.color("cyan")
timmy.teleport(60)
for i in range(0,4):
    timmy.forward(100)
    timmy.right(90)
   
screen.exitonclick()
