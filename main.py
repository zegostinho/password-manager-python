from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        site_entry: {
            "email": email_entry,
            "password": new_password
        }
    }

    if len(site_entry) == 0 or len(new_password) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty!")
    else:
        try:
            with open("my_passwords.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("my_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("my_passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            site_text_box.delete(0, END)
            site_text_box.focus()
            password_text_box.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = site_text_box.get()
    try:
        with open("my_passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(message=f"Website: {website}\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showerror(message=f"No details for {website} exists.")

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

site_text_box = Entry(width=21)
site_text_box.focus()
site_text_box.grid(column=1, row=1)

email_text_box = Entry(width=38)
email_text_box.grid(column=1, row=2, columnspan=2)

password_text_box = Entry(width=21)
password_text_box.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()