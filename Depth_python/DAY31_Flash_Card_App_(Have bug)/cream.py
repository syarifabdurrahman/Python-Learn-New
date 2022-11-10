import tkinter.ttk as ttk
from tkinter import *
import pandas
import random

FRONT_BG = r'Depth_python\DAY31_Flash_Card_App\images\card_front.png'
BACK_BG = r'Depth_python\DAY31_Flash_Card_App\images\card_back.png'
data_dict = {}
# ---------------------------- Setup ------------------------------------ #

try:
    csv_file = pandas.read_csv(
        r'Depth_python\DAY31_Flash_Card_App\data\words_to_learn.csv')
except FileNotFoundError:
    print('file not found, create one ..............!')
    # Creating new one
    csv_file = pandas.read_csv(
        r'Depth_python\DAY31_Flash_Card_App\data\french_words.csv')
    data_dict = csv_file.to_dict()
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv(
        r'Depth_python\DAY31_Flash_Card_App\data\words_to_learn.csv', index=False)
finally:
    print('do this')
    csv_file = pandas.read_csv(
        r'Depth_python\DAY31_Flash_Card_App\data\words_to_learn.csv')
    data_dict = csv_file.to_dict(orient='records')

rand_word = None


def next_word():
    global rand_word, flip_timer, data_dict
    root.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=image_holder_front)

    rand_word = random.choice(data_dict)
    canvas.itemconfig(title_teks, text='French', fill='black')
    canvas.itemconfig(word_teks, text=rand_word['French'], fill='black')
    flip_timer = root.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=image_holder_back)
    canvas.itemconfig(title_teks, text='English', fill='white')
    canvas.itemconfig(word_teks, text=rand_word['English'], fill='white')


def is_known():
    global rand_word, data_dict
    if len(data_dict) <= 0:
        data_dict = [{"French": "Tu as appris\ntous les mots!",
                      "English": "You learned all the words!"}]
    else:
        random_word_index = data_dict.index(rand_word)
        # del data_dict[random_word_index]

    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv(
        r'Depth_python\DAY31_Flash_Card_App\data\words_to_learn.csv', index=False)

    next_word()


# ---------------------------- UI ------------------------------------ #
root = Tk()
root.title('Flashy')
root.geometry('900x720')
root.resizable(False, False)
root.config(background='#B1DDC6', padx=50, pady=50)

flip_timer = root.after(3000, flip_card)

# canvas
canvas = Canvas(width=800, height=526,
                highlightthickness=0, background='#B1DDC6')
image_holder_front = PhotoImage(file=FRONT_BG)
image_holder_back = PhotoImage(file=BACK_BG)
canvas_image = canvas.create_image(800/2, 526/2, image=image_holder_front)
canvas.grid(column=0, row=0, columnspan=2)

# Teks
title_teks = canvas.create_text(
    800/2, 150, text='', font=('Arial', 40, 'italic'))
word_teks = canvas.create_text(
    800/2, 526/2, text='', font=('Arial', 60, 'bold'))

# buttons
false_image = PhotoImage(
    file='Depth_python\DAY31_Flash_Card_App\images\wrong.png')
false_button = Button(
    image=false_image, highlightthickness=0, command=next_word)
false_button.grid(column=0, row=1)

true_image = PhotoImage(
    file=r'Depth_python\DAY31_Flash_Card_App\images\right.png')
true_button = Button(image=true_image, highlightthickness=0, command=is_known)
true_button.grid(column=1, row=1)

next_word()

root.mainloop()
