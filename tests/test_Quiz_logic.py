#test_Quiz_logic.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import patch, MagicMock
from Quiz.Quiz_logic import Quiz

# Mock question object
class MockQuestion:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

# Sample questions for tests
mock_questions = [
    MockQuestion("What is 2 + 2?", ["A. 3", "B. 4", "C. 5", "D. 6"], "B"),
    MockQuestion("Capital of France?", ["A. London", "B. Berlin", "C. Paris", "D. Rome"], "C"),
]

def test_is_correct_valid_input():
    quiz = Quiz(mock_questions)
    assert quiz.is_correct("B", "B") is True
    assert quiz.is_correct("C", "B") is False

@patch("builtins.input", return_value="2")
@patch("Quiz.Quiz_logic.Interface.number_of_questions", return_value="How many questions?")
def test_value_error_handler_valid(mock_interface_msg, mock_input):
    quiz = Quiz(mock_questions)
    assert quiz.value_error_handler() == 2

@patch("builtins.input", side_effect=["abc", "25", "2"]) 
@patch("Quiz.Quiz_logic.Interface.number_of_questions", return_value="How many questions?")
@patch("Quiz.Quiz_logic.Interface.value_error", return_value="Invalid input")
@patch("Quiz.Quiz_logic.Interface.enter_in_range", return_value="Enter 1-2: ")
def test_value_error_handler_invalid_then_valid(mock_range_prompt, mock_val_err, 
                                             mock_interface_msg, mock_input):
    quiz = Quiz(mock_questions)    
    assert quiz.value_error_handler() ==2
    

@patch("builtins.input", side_effect=["25", "2"])
@patch("Quiz.Quiz_logic.Interface.enter_in_range", return_value="Enter a number between 1 and 20:")
@patch("Quiz.Quiz_logic.Interface.number_of_questions", return_value="How many questions?")
def test_range_handler_out_of_range_then_valid(mock_interface_msg, mock_range_msg, mock_input):
    quiz = Quiz(mock_questions)
    assert quiz.value_error_handler() == 2

@patch("builtins.input", side_effect=["B", "C"])
@patch("Quiz.Quiz_logic.Interface.display_question", side_effect=["", ""])
@patch("Quiz.Quiz_logic.Interface.display_correct")
@patch("Quiz.Quiz_logic.Interface.display_incorrect")
@patch("Quiz.Quiz_logic.Interface.display_score", return_value="Final Score: 2/2")
@patch("Quiz.Quiz_logic.Interface.number_of_questions", return_value="How many questions?")
def test_quiz_start(mock_num_q, mock_score, mock_incorrect, mock_correct, mock_display_q, mock_input):
    quiz = Quiz(mock_questions)
    with patch.object(quiz, 'value_error_handler', return_value=2):
        quiz.start()
        assert quiz.score == 2
