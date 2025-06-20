from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

 # Fixed typo in variable name


game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

   #Detect collison with food
    if snake.head.distance(food)<15:
        
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    
    #Detect collision with tail
    for segment in snake.segments[1:]:
      
        if snake.head.distance(segment)<10:
            game_is_on=False
            score.game_over

    #if head collides with any segment in the tail:
             #trigger game_over





screen.exitonclick()