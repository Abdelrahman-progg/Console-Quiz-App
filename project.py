#project.py
from Quiz.Quiz_logic import Quiz
from Quiz import Questions 
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print( os.path.join(current_dir, "Quiz", "Questions.py"))
def main():

    questions = Questions.the_questions()
    quiz = Quiz(questions)
    quiz.start()
    
if __name__ == '__main__':
    main()