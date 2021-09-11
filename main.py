from data import question_data
from random import sample

def str_to_bool(s):
    s = s.replace(" ", "").lower()
    
    if s in ['true', 't']:
        return True
    elif s in ['false', 'f']:
        return False
    else:
        raise Exception()
        
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            
            try:                
                user_answer = str_to_bool(user_answer)
            except Exception as e:
                print("Input is invalid. Please enter True/False or T/F (not case-sensitive)")
            else:
                break
        
        self.check_answer(user_answer, current_question.answer)
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
            
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}", end='\n')
        
        
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = bool(question["answer"].capitalize())
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
question_bank = sample(question_bank, 5)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")