from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title('Mile to Km')
root.config(pady=20, padx=20)


def calculate():
    miles = int(mile_input.get())
    result = round(miles*1.6, 2)
    km_result_text.config(text=f"{result}")


# labels
mile_text = ttk.Label(text="Miles", font=("Arial", 13))
mile_text.grid(column=2, row=0)

km_text = ttk.Label(text="Km", font=("Arial", 13))
km_text.grid(column=2, row=1)

equal_text = ttk.Label(text="is equal to", font=("Arial", 13))
equal_text.grid(column=0, row=1)

km_result_text = ttk.Label(text="0", font=("Arial", 13))
km_result_text.grid(column=1, row=1)

# Entry
mile_input = ttk.Entry(width=10)
print(mile_input.get())
mile_input.grid(column=1, row=0)

# Buttons
button_calculate = ttk.Button(text="Calculate", command=calculate)
button_calculate.grid(column=1, row=2)


root.mainloop()
