from tkinter import *

window = Tk()
window.title('App')
window.minsize(width=500, height=500)

# label
my_label = Label(text="I\'m label", font=("Arial", 24, "bold"))
my_label.config(text='New text')
# my_label.pack(pady=1)
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)


# button
def button_handler():
    new_input = input.get()
    my_label.config(text=new_input)


button_1 = Button(text="Click me", command=button_handler)
# button.pack(pady=1)
button_1.grid(column=1, row=1)

button_2 = Button(text="New button", command=button_handler)
# button.pack(pady=1)
button_2.grid(column=2, row=0)


# entry
input = Entry(width=10)
print(input.get())
# input.pack(pady=1)
input.grid(column=3, row=3)


window.mainloop()
