import tkinter as tk
window=tk.Tk()
window.title("My First GUI")
window.minsize(width=500,height=300)
#label
my_label=tk.Label(text="I am a label",font=("Arial",24,"bold"))
my_label.pack(expand=True)
window.mainloop()