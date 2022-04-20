import pytest
from quizzes.forms import quiz_form_factory
from quizzes.models import QuizQuestion, QuizTaken
from wtforms.fields.core import UnboundField
from wtforms import RadioField


@pytest.fixture
def new_quiz_question():
    quiz_question = QuizQuestion(question='text', correct_answer='correct',
                                 incorrect_answers=["incorrect_1", "incorrect_2", "incorrect_3"])
    return quiz_question


@pytest.fixture
def new_quiz_taken(new_quiz_question):
    quiz_taken = QuizTaken(uuid='1234', difficulty='easy',
                           questions=[new_quiz_question, new_quiz_question, new_quiz_question])
    return quiz_taken


def test_quiz_form_factory(new_quiz_taken):
    field = UnboundField(RadioField, ('text'), choices=['incorrect_1', 'incorrect_2', 'incorrect_3', 'correct'])
    assert quiz_form_factory(new_quiz_taken).question_1.field_class == field.field_class
    assert quiz_form_factory(new_quiz_taken).question_1.args == field.args
    assert quiz_form_factory(new_quiz_taken).question_1.name == field.name
    assert quiz_form_factory(new_quiz_taken).question_1.kwargs == field.kwargs
