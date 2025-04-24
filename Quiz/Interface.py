#Interface.py
import colorama

colorama.init(autoreset=True)


def choose_subject():
    return 'Choose: Math , English , History: \n'

def number_of_questions():
    return 'How many questions would you like? (1->20)\n'

def value_error():
    return 'Invalid input! Please enter a number.\n'

def enter_in_range(num):
    return f'Please enter a number between 1 and {num}.\n'

def display_question(question, options):
    return f"\n{question}\n" + "\n".join(options)+'\n'

def display_no_Quizes():
    return 'No quizes available right now. Please come back later'
    
def display_correct():
    return f"{colorama.Fore.GREEN}Correct!\n"
    
def display_incorrect(answer):
    return f"{colorama.Fore.RED}Incorrect! The correct answer was {answer}\n"

    
def display_score(score, total):
    if score > total/2 :
        return f'{colorama.Fore.GREEN}Your total score is {score}/{total} '
    else:
        return f'{colorama.Fore.RED}Your total score is {score}/{total} '