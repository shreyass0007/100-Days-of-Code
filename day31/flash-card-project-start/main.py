from tkinter import *
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.minsize(width=800, height=526)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#canvas setup

canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR)
card_img = PhotoImage(file="card_front.png")
canvas.create_image(400,263,image=card_img)


wrong_img = PhotoImage(file="wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1,column=0)

Right_img = PhotoImage(file="right.png")
Right_button=Button(image=Right_img, highlightthickness=0)
Right_button.grid(row=1,column=1)

canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)
french_word=pd.read_csv("day31/flash-card-project-start/data/french_words.csv")


window.mainloop()
