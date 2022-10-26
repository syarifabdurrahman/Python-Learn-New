class QuizBrain:
    def __init__(self,questions_list) -> None:
        self.question_number = 0
        self.score = 0
        self.question_list = questions_list
        self.current_question = None
        self.answer = None

    def still_has_question(self):
       return self.question_number < len(self.question_list) # if question number < returning True, then if > returning false 
           

    def checking_answer(self):
        if self.answer == self.current_question.answer:
            self.question_number += 1
            self.score += 1

            print('You got it right!')
            print(f'The correct answer was: {self.current_question.answer}')
            print(f'Your current score is: {self.score}/{self.question_number} \n')
        else:
            self.question_number += 1
            print('Oops, You got it wrong!')
            print(f'The correct answer was: {self.current_question.answer}')
            print(f'Your current score is: {self.score}/{self.question_number} \n')
            

    def next_question(self):
       self.current_question = self.question_list[self.question_number]
       self.answer = input(f"Q.{self.question_number + 1}: {self.current_question.text} (True/False): ").title()
       self.checking_answer()

