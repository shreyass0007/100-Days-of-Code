from tkinter import*
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
lock_img=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,112,image=lock_img)
canvas.grid(column=1,row=1,padx=20,pady=20)
window.mainloop()