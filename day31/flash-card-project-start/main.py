from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#canvas setup

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
card_img = PhotoImage(file="card_front.png")
canvas.create_image(400,263,image=card_img)
data=pd.read_csv("day31/flash-card-project-start/data/french_words.csv")
data_dict=data.to_dict(orient="records")
print(data_dict)
def next_card():
    current_card=random.choice(data_dict)
    current_card=current_card["French"]
    canvas.itemconfig(card_title,text="French")
    canvas.itemconfig(card_word,text=current_card)



wrong_img = PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

Right_img = PhotoImage(file="right.png")
Right_button=Button(image=Right_img, highlightthickness=0,command=next_card)
Right_button.grid(row=1,column=1)

card_title=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)
french_word=pd.read_csv("day31/flash-card-project-start/data/french_words.csv")




window.mainloop()
