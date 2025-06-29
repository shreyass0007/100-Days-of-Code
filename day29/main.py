from tkinter import *
from tkinter import messagebox


#--------------------SAVE PASSWORD-------------------
def save():
    website=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    if len(website)==0 or len(password) or len(email):
        messagebox.showinfo(title="Oops",message="Please make sure you have't left any fiels empty.")
    else:
        #messagebox.showinfo(title="Title",message="Message")
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}\nPassword:{password}\nIs it ok to save ?")
        
        if is_ok:
            with open("data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0,END)
                pass_entry.delete(0,END)

#---------------------UI SETUP-----------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)  # Added padding around the entire window

# Logo (centered properly)
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)  # Fixed y-position (100 instead of 112)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
web_label.grid(column=0, row=1, sticky="e", padx=5, pady=5)  # Right-aligned

mail_label = Label(text="Email/Username:")
mail_label.grid(column=0, row=2, sticky="e", padx=5, pady=5)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, sticky="e", padx=5, pady=5)

# Entries (aligned and consistent width)
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, padx=5, pady=5)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=5)
email_entry.insert(0,"shreshshende@gmail.com")
pass_entry= Entry(width=21)
pass_entry.grid(column=1, row=3, padx=5, pady=5,sticky="e")  # Left-aligned

# Buttons
pass_button = Button(text="Generate Password",width=21)
pass_button.grid(column=2, row=3, padx=5, pady=5, sticky="w")  # Left-aligned

add_button = Button(text="Add", width=36,command=save)
add_button.grid(column=1, row=4, columnspan=2, padx=5, pady=5)


window.mainloop()