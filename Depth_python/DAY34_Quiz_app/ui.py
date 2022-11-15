from tkinter import *
from quiz_brain import QuizBrain
from time import sleep

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.root = Tk()
        self.root.title('Quizz App')
        self.root.geometry('350x500')
        self.root.resizable(False, False)
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text='Score: 0', font=(
            'Arial'), highlightthickness=0, bg=THEME_COLOR, foreground='white')
        self.score_label.grid(column=1, row=0)

        # Creating Canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.center_text = self.canvas.create_text(150, 125, width=280, text='Lorem ipsum dolor sit amet',
                                                   font=('Arial', 15, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Buttons

        self.true_img = PhotoImage(
            file=r'Depth_python\DAY34_Quiz_app\images\true.png')
        self.true_btn = Button(image=self.true_img, command=self.true_handler)
        self.true_btn.grid(column=0, row=2)

        self.false_img = PhotoImage(
            file=r'Depth_python\DAY34_Quiz_app\images\false.png')
        self.false_btn = Button(image=self.false_img,
                                command=self.false_handler)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.root.mainloop()

    def true_handler(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_handler(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            # self.canvas.itemconfig(self.center_text, fill='white')
            self.canvas.config(bg='green')
        else:
            # self.canvas.itemconfig(self.center_text, fill='white')
            self.canvas.config(bg='red')

        self.canvas.update()

        sleep(.5)

        self.canvas.itemconfig(self.center_text, fill='black')
        self.canvas.config(bg='white')
        self.canvas.update()

        self.root.after(1000, self.get_next_question())

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(
                text=f'Score: {self.quiz.score}/{self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.center_text, text=q_text)
        else:
            self.canvas.config(bg='white')

            self.canvas.itemconfig(
                self.center_text, text='Thats for all of quiz :D')

            self.true_btn['state'] = 'disabled'
            self.false_btn['state'] = 'disabled'


if __name__ == '__main__':
    quiz = QuizInterface()
