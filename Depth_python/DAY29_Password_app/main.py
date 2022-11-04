from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import pyperclip
import random
import os
# ------------- GENERATE PASSWORD -------------#


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letter = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passowrd_letter = [random.choice(letters) for _ in range(nr_letter)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    result = passowrd_letter + password_symbol + password_number

    my_result_str = ''.join(result)
    password_input.delete(0, END)
    password_input.insert(0, my_result_str)
    pyperclip.copy(my_result_str)
    print(my_result_str)


# ------------- SAVE PASSWORD -------------#
name_file = 'result.txt'
PATH_DIR = os.path.join(os.path.expanduser('~'), 'Documents', name_file)

print(PATH_DIR)


def add_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if website == '' or email == '' or password == '':
        messagebox.showerror(
            title='Error', message=f"Either {website}, {email}, and {password} are empty")
        return
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f'These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save')

        if is_ok:
            with open(PATH_DIR, mode='a') as file:
                file.write(f"{website} | {email} | {password}\n")
                # deleteing char after input from index zero to end
                website_input.delete(0, END)
                password_input.delete(0, END)  # deleteing char after input
                messagebox.showinfo(
                    title='Info', message=f"save on {PATH_DIR}")

    # ------------- UI SETUP -------------#
root = Tk()
root.title('Pasword Manager')
root.config(padx=50, pady=50)

# Adjust size
root.geometry("500x400")

# set minimum window size value
root.minsize(500, 400)

# set maximum window size value
root.maxsize(500, 400)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=r'Depth_python\DAY29_Password_app\logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = ttk.Label(text='Website:')
website_label.grid(column=0, row=1)
email_label = ttk.Label(text='Email/Username:')
email_label.grid(column=0, row=2)
password_label = ttk.Label(text='Password:')
password_label.grid(column=0, row=3)


# Entries
website_input = ttk.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="Nsew")
website_input.get()
website_input.focus()
email_input = ttk.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="Nsew")

email_input.insert(0, 'test@mail.com')
password_input = ttk.Entry(width=21)
password_input.grid(column=1, row=3, sticky="Nsew")
password_input.get()

# Btns
generate_btn = ttk.Button(text='Generate Password', command=generate_password)
generate_btn.grid(column=2, row=3, sticky="Nsew")
add_btn = ttk.Button(text='Add', width=36, command=add_to_file)
add_btn.grid(column=1, row=4, columnspan=2, sticky="Nsew")

root.mainloop()
