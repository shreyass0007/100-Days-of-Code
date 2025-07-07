from tkinter import *

def miles_to_km():
    miles=float((miles_input.get()))
    km=miles*1.609
    kilometer_label.config(text=f"{km}")
window=Tk()
window.title("My First GUI")
window.config(padx=20,pady=20)
window.minsize(width=350,height=180)
#label

# my_label.pack()
miles_input=Entry(width=7)
miles_label=Label(text="Miles")
miles_input.grid(column=1,row=0)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)
my_label_3=Label(text="  is equal to")
my_label_3.grid(column=0,row=1)

my_label = Label(text="0")
my_label.grid(column=1,row=1)

input=Entry(width=15)
#button 


button=Button(text="Calculate",command=miles_to_km,padx=20,pady=5)
button.grid(column=1,row=2)


#Entry
input.grid(column=1,row=0,padx=20,pady=5)

window.mainloop()