#Questions.py
import json
import os
from Quiz import Interface
from random import shuffle



# Question(text, options, answer)
class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer
    
# fetch from json file
def load_question(filepath):
    with open(filepath , 'r', encoding='utf-8') as f:
        data = json.load(f)
        questions = [Question(q['question'], q['options'], q['answer']) for q in data]
        shuffle(questions)
        return questions
    
# check if subject is available and return a list of Question objects
def the_questions():
    subjects = [f.replace('_questions.json', '') for f in os.listdir('Data') if f.endswith('.json')]
    if not subjects:
        exit(Interface.display_no_Quizes())
    subject=''
    while True:
        subject = input(Interface.choose_subject()).title()
        if subject in subjects:
            return load_question(f'Data/{subject}_questions.json')


        
