#test_Question.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pytest
from unittest.mock import patch, mock_open
from Quiz.Questions import the_questions, load_question

mock_questions = [{"question": "Test", "options": ["A. 1"], "answer": "A"}]

@patch("Quiz.Questions.os.listdir", return_value=["Math_questions.json"])
@patch("Quiz.Questions.load_question", return_value=mock_questions)
def test_the_questions_valid_input(mock_load, mock_listdir):
    with patch("builtins.input", return_value="math"):
        result = the_questions()
        mock_load.assert_called_once_with("Data/Math_questions.json")
        assert result == mock_questions

@patch("Quiz.Questions.os.listdir", return_value=["History_questions.json"])
@patch("Quiz.Questions.load_question", return_value=mock_questions)
def test_the_questions_invalid_then_valid(mock_load, mock_listdir):
    with patch("builtins.input", side_effect=["INVALID", "history"]):
        result = the_questions()
        mock_load.assert_called_once_with("Data/History_questions.json")
        assert result == mock_questions

@patch("Quiz.Questions.os.listdir", return_value=[])
@patch("builtins.input")  # Add this line
def test_the_questions_no_files(mock_input, mock_listdir, capsys):
    with pytest.raises(SystemExit) as exc_info:
        the_questions()
    assert exc_info.value.code == "No quizes available right now. Please come back later"

    
@patch("Quiz.Questions.os.listdir", return_value=["English_questions.json"])
@patch("Quiz.Questions.load_question", return_value=mock_questions)
def test_the_questions_case_insensitive(mock_load, mock_listdir):
    with patch("builtins.input", return_value="ENGLISH"):
        result = the_questions()
        mock_load.assert_called_once_with("Data/English_questions.json")
        assert result == mock_questions

# Test for load_question function
@patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{
    "question": "Test Q",
    "options": ["A. 1"],
    "answer": "A"
}]))
def test_load_question(mock_file):
    questions = load_question("dummy_path.json")
    assert len(questions) == 1
    assert questions[0].answer == "A"
    mock_file.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")