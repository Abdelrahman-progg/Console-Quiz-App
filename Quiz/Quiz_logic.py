#Quiz_logic.py
from Quiz import Interface

class Quiz :
    def __init__(self, questions):
        self.questions = questions
        self.score=0
        
    def start(self):
         
        num = self.value_error_handler()

        for i in range (num):
            print('Enter the letter of the answer:')
            answer = input(Interface.display_question(self.questions[i].text, self.questions[i].options )).upper()
            if self.is_correct(self.questions[i].answer, answer):
                self.score +=1
                print(Interface.display_correct())
            else:
                print(Interface.display_incorrect(self.questions[i].answer))
        print(Interface.display_score(self.score, num))
        
        
        
    def is_correct(self, real_answer, user_answer):
        options = ['A','B','C','D']

        while True:           
            if user_answer in options:
                break
            else:
                user_answer=input('Enter a letter in range (A-D)\n').upper()
        if real_answer == user_answer:
            return True 
        else :
            return False
    
    def value_error_handler(self) :   
        while True:
            try:
                num = int(input(Interface.number_of_questions()))
                num = self.range_handler(num)
                return num
            except  ValueError:
                print(Interface.value_error()) 
        
    def range_handler(self, num):
        max = len(self.questions)
        while True:
            if 1<= num <= max :
                return num
            else:
                num = int(input(Interface.enter_in_range(max)))