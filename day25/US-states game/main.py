import turtle
import pandas as pd
screen=turtle.Screen()
screen.title("U.S.States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pd.read_csv("50_states.csv")

answer_State=screen.textinput(title="Guess the State",prompt="what's another state's name?")
print(answer_State)
screen.exitonclick()