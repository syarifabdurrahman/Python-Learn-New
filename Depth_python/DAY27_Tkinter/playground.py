import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
root.title('Widget example')
root.minsize(width=500, height=500)

# root.tk.call('source', 'azure/azure.tcl')
# style.theme_use('azure')
# style.configure("Accentbutton", foreground='white')
# style.configure("Togglebutton", foreground='white')

# # label
my_label = ttk.Label(text="Hello world", font=("Arial", 24))
my_label.pack()

# my_label['text'] = "new text"
my_label.config(text='New text')  # Updating label

# # Buttons


def button_clicked():
    input_result = input.get()
    my_label.config(text=input_result)


button = ttk.Button(text='Click me', command=button_clicked)
button.pack(pady=3)

# # Entry / input
input = ttk.Entry()
print(input.get())
input.pack()

# Text
text = tk.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tk.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.pack(pady=2)

# Spinbox


def spinbox_used():
    # gets the current value in spinbox.
    print(f"this is spinbox: {spinbox.get()}")


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(f"this is scale: {value}")


scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(f"This is checked button: {checked_state.get()}")


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1,
                              variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2,
                              variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


root.mainloop()  # keeping on screen
