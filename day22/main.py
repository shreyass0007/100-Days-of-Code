from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title("pong",)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
#top_paddle=Paddle((100,100))

ball=Ball()
scoreboard=Scoreboard()




screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #Detecte collision wiht wall
    if ball.ycor()>370 or ball.ycor()<-370:
        #need bounce
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>348 or ball.distance(l_paddle)<50 and ball.xcor()<-348  :
       ball.bounce_x()
    
    #dected R paddle misses
    if ball.xcor()>380:
        
        ball.reset_position()
        scoreboard.l_point()
   #dected L paddle
    if ball.xcor()<-380:
        
        ball.reset_position()
        scoreboard.r_point()
       

screen.exitonclick()