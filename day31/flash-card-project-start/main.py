from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

data=pd.read_csv("day31/flash-card-project-start/data/french_words.csv")
to_learn=data.to_dict(orient="records")
current_card={}


def next_card():
    global current_card,flip_timer
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_img)
    flip_timer=window.after(2000,func=flip_card)
def flip_card():
    global current_card
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    
window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(2000,func=flip_card)

#canvas setup

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
card_img = PhotoImage(file="card_front.png")
card_background=canvas.create_image(400,263,image=card_img)
back_img=PhotoImage(file="card_back.png")

current_card={}




wrong_img = PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)

Right_img = PhotoImage(file="right.png")
Right_button=Button(image=Right_img, highlightthickness=0,command=is_known)
Right_button.grid(row=1,column=1)

card_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)

next_card()


window.mainloop()