from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

tim = Turtle()
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]  # Fixed typo in variable name


game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()