from turtle import Turtle,Screen
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title("pong",)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
top_paddle=Paddle((100,100))




screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()
screen.exitonclick()