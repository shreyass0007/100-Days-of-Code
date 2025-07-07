from turtle import Turtle, Screen
timmy=Turtle()
screen=Screen()
from turtle import Turtle, Screen
def dashed(lenght,dashed_length=10):
    for _ in range(int(lenght/dashed_length)):
        timmy.pendown()
        timmy.forward(dashed_length)
        timmy.penup()
        timmy.forward(dashed_length)
        timmy.penup()
dashed(200)
   
screen.exitonclick()
