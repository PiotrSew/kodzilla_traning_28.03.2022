import pytest
from quiz.quizzes.forms import quiz_form_factory
from quiz.quizzes.models import QuizQuestion, QuizTaken


@pytest.fixture
def new_quiz_question():
    quiz_question = QuizQuestion(question='text', correct_answer='correct', incorrect_answers="incorrect")
    return quiz_question


@pytest.fixture
def new_quiz_taken(new_quiz_question):
    quiz_taken = QuizTaken(uuid='1234', difficulty='easy',
                           questions=[new_quiz_question, new_quiz_question, new_quiz_question])
    return quiz_taken


def test_quiz_form_factory(new_quiz_taken):
    quiz_form_factory(new_quiz_taken)
