from tkinter import *
import tkinter.ttk as ttk
import math

# ------ CONSTANTS --------- #
PINK = '#FF9F9F'
RED = '#E97777'
GREEN = '#90A17D'
YELLOW = '#FCDDB0'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ------ TIMER RESET --------- #


def reset_timer():
    global reps

    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', foreground=GREEN, background=YELLOW,
                       font=(FONT_NAME, 40, 'bold'))
    check_mark.config(text='')
    reps = 0


# ------ TIMER MECHANISM --------- #


def start_timer():
    global reps

    reps += 1

    if reps % 2 == 0:
        if reps == 8:

            long_break_sec = LONG_BREAK_MIN * 60
            title_label.config(text='Long Break', foreground=RED, background=YELLOW,
                               font=(FONT_NAME, 40, 'bold'))

            print(f"{reps}: long break")
            count_down(long_break_sec)
            reps = 0
        else:

            short_break_sec = SHORT_BREAK_MIN * 60
            title_label.config(text='Short Break', foreground=PINK, background=YELLOW,
                               font=(FONT_NAME, 40, 'bold'))

            print(f"{reps}: short break")
            count_down(short_break_sec)
    else:
        title_label.config(text='Work', foreground=GREEN, background=YELLOW,
                           font=(FONT_NAME, 40, 'bold'))

        work_sec = WORK_MIN * 60
        print(f"{reps}: work")
        count_down(work_sec)

    # count_down(5*60)  # because main loop so its looping

# ------ COUNTDOWN MECHANISM --------- #


def count_down(count):
    global reps, timer
    # "01:35"
    # 300/60 = 5 minutes
    # 300 % 60 = 0 second
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = root.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(0, work_sessions):
            marks += '✔️'
        check_mark.config(text=marks)


# ------ UI SETUP --------- #
root = Tk()
root.title("Pomodoro")
root.minsize(width=600, height=600)
root.maxsize(width=700, height=700)
root.config(padx=10, pady=30, bg=YELLOW)

title_label = ttk.Label(text='Timer', foreground=GREEN, background=YELLOW,
                        font=(FONT_NAME, 40, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=512, height=512, bg=YELLOW, highlightthickness=0)
cat_img = PhotoImage(file=r'Depth_python\DAY28_Pomodoro_app\cat.png')
canvas.create_image(256, 256, image=cat_img)
timer_text = canvas.create_text(256, 256, text='00:00', fill='white',
                                font=(FONT_NAME, 50, 'bold'))
canvas.grid(column=1, row=1)
# count_down(5)  # because mainloop() so its looping

start_btn = ttk.Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = ttk.Button(text='Reset', command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = ttk.Label(foreground=GREEN, background=YELLOW)
check_mark.grid(column=1, row=3)


root.mainloop()
