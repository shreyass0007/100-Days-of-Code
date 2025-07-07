from tkinter import *
window=Tk()
window.title("My First GUI")
window.minsize(width=500,height=300)
#label
my_label=Label(text="I am a label",font=("Arial",24,"bold"))
# my_label.pack()

my_label["text"]="New text"
my_label.config(text="New text")
my_label.grid(column=0,row=0)

input=Entry(width=10)
#button 
def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label['text']=new_text
button=Button(text="Click me",command=button_clicked)
button.grid(column=1,row=1)

button_1=Button(text="Click me",command=button_clicked)
button_1.grid(column=2,row=0)
#Entry
input.grid(column=3,row=3)

window.mainloop()