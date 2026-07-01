from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_text_box.delete(0, END)
    password_text_box.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site_entry = site_text_box.get()
    email_entry = email_text_box.get()
    new_password = password_text_box.get()

    if len(site_entry) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=site_entry, message=f"These are the details entered: "
                                                                 f"\nWebsite: {site_entry}"
                                                                 f"\nEmail: {email_entry}"
                                                                 f"\nPassword: {new_password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{site_entry} | {email_entry} | {new_password}\n")

            site_text_box.delete(0, END)
            site_text_box.focus()
            password_text_box.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

site_text = Label(text="Website:")
site_text.grid(column=0, row=1)

email_user_text = Label(text="Email/Username:")
email_user_text.grid(column=0, row=2)

password_text = Label(text="Password:")
password_text.grid(column=0, row=3)

site_text_box = Entry(width=38)
site_text_box.focus()
site_text_box.grid(column=1, row=1, columnspan=2)

email_text_box = Entry(width=38)
email_text_box.insert(0, "jose.agostinho.111@gmail.com")
email_text_box.grid(column=1, row=2, columnspan=2)

password_text_box = Entry(width=21)
password_text_box.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()