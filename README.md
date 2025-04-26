# Consol Quiz Application 

A command-line quiz game that tests your knowledge in various subjects. Built with Python.


# Features 
- **Multiple Subjects**: Choose between Math, English, and History or more if you added more files
- **Dynamic Question Loading**: Questions loaded from JSON files
- **Score Tracking**: Get a colored score summary (green/red) at the end
- **Input Validation**: Robust handling of invalid inputs
- **Randomized Questions**: Questions shuffled for each session


## Installation
1. Clone repository:
```bash
git clone https://github.com/Abdelrahman-progg/Console-Quiz-App.git
cd Console-Quiz-App
Install dependencies:

bash
pip install -r requirements.txt
Usage
Run the application:

bash
python project.py
Sample workflow:

Choose from available subjects

Select number of questions (1-20)

Answer questions using A-D input

Get final score with color-coded results

Project Structure
Console-Quiz-App/
├── Data/                   # Pre-made question banks
│   ├── English_questions.json
│   ├── History_questions.json
│   └── Math_questions.json
├── Quiz/                  # Core application logic
│   ├── Interface.py       # UI components and color handling
│   ├── Questions.py       # Question loading and processing
│   └── Quiz_logic.py      # Quiz flow and scoring system
├── tests/                 # Test suite
│   ├── test_Question.py
│   └── test_Quiz_logic.py
├── project.py             # Main entry point
├── requirements.txt
└── README.md
Testing
Run the test suite with:

bash
pytest tests/
Customization
To add more questions:

Edit existing JSON files in Data/ or create new ones following the format:

json
[
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Berlin", "D. Madrid"],
        "answer": "B"
    }
]
Maintain the naming convention: <Subject>_questions.json


## Code Structure Deep Dive 

### Core Modules:
| File               | Purpose                                  |
|--------------------|------------------------------------------|
| `Interface.py`     | Manages colored terminal UI components   |
| `Questions.py`     | Loads/shuffles questions from JSON files |
| `Quiz_logic.py`    | Contains quiz flow and scoring logic     |

### Key Functions `Interface.py`:

choose_subject():
    give the user the freedom to pick which ever subject the user wish.

number_of_questions():
    give the user the freedom to pick the number of questions te user wish to solve (in the range of existing questions).

value_error():
    return an understandable ValueError massage to the user.

enter_in_range(num):
    inform the used of the availabe range  .

display_question(question, options):
    return the question with the options of choice.

display_no_Quizes():
    return a statement indicates the unavailability of quizes at the time.

display_correct():
    return the correct answer message (green).

display_incorrect(answer):
    return the incorrect answer message with the correct answer (red).

display_score(score, total):
    return the final score (red for the failure) (green for succes).



### Key Functions `Questions.py`:

class Question:
    A class to identify Question objects in the wanted form.

__init__(self, text, options, answer):
    initiating method for the class to design the objects' structure and declare objects.

load_question(filepath):
    a methos that fitches from json file to declare "Question" objects and returns the objects in random order.

the_questions():
    identifies the json files and let the user choose between subjects.load the questions from the json file and return them.


### Key Functions `Quiz_logic.py`:

class Quiz:
    A class to identify Quiz objects in the wanted form.    

__init__(self, questions):
    initiating method for the class to design the objects' structure and declare objects.

start(self):
    takes the answer from the user. In conclution it prints the score.

is_correct(self, real_answer, user_answer):
    check the correctness of the answer(if the answer is incorrect in print the right answer).

value_error_handler(self):
    insures that the user must enter an integer.

range_handler(self, num)
    insures that the user must enter a number in the range of the questions.

```
bash
### Opportunity for growth
-** Add levels for each subject to test the examinee level in certain subject.**
-** Add subsubjects to acknowledge the Quiz taker's weaknesses.**
-** Store the past quiz data for each user.**
