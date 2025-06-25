import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/ 50 States correct", prompt="What's another state's name?").title()
    print(answer_state)

    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state=="Exit":
        missing_states=[]
        for  state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in all_states:
        # If they got it right:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]  # Fixed: lowercase 'state' to match CSV
        t.goto(int(state_data.x), int(state_data.y))  # Fixed: access x and y values correctly
        t.write(state_data.state.item())  # Just write the state name we already have


#states to learn.csv
