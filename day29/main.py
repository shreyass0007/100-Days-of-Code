from tkinter import*
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
lock_img=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1,row=0,padx=20,pady=20)

web_label=Label(text="Website:")
web_label.grid(column=0,row=1)

mail_label=Label(text="Email/Username:")
mail_label.grid(column=0,row=2)

pass_label=Label(text="Password:")
pass_label.grid(column=0,row=3)

web_entry = Entry(width=35)
web_entry.insert(END,string="")

print(web_entry.get())
web_entry.grid(column=1,row=1,columnspan=2)


email_entry = Entry(width=35)
email_entry.insert(END, string="")

print(email_entry.get())
email_entry.grid(column=1,row=2,columnspan=2)

pass_entry = Entry(width=21)
pass_entry.insert(END, string="")

print(pass_entry.get())
pass_entry.grid(column=1,row=3)

pass_button = Button(text="Generate Password")
pass_button.grid(column=2,row=3)

add_button = Button(text="Add",width=36)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()