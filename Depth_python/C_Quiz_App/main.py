from question_model import Question
from question_data import question_data
from quiz_brain import QuizBrain


question_bank= []
for i in range (len(question_data)):
    new_question = Question(question_data[i]['text'],question_data[i]['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
        