from uuid import uuid4
import pytest
from quizzes.models import calculate_points, QuizQuestion, QuizTaken, QuizResult, User


@pytest.fixture
def new_user():
    user = User(id=1, active=True, username="username_test", password="password_test", first_name='first_name_test',
                last_name='last_name_test')
    return user


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


@pytest.fixture
def new_quiz_result():
    quiz_result = QuizResult(user_id=1, quiz_uuid='4321', points=1)
    return quiz_result


def test_calculate_points_dummy():
    quiz_taken = QuizTaken(uuid=uuid4().hex, difficulty='easy', questions=[])
    assert 0 == calculate_points(quiz_taken=quiz_taken, answers={})


def test_new_user(new_user):
    assert new_user.id == 1
    assert new_user.active is True
    assert new_user.username == 'username_test'
    assert new_user.password == 'password_test'
    assert new_user.first_name == 'first_name_test'
    assert new_user.last_name == 'last_name_test'


def test_quiz_question(new_quiz_question):
    assert new_quiz_question.question == 'text'
    assert new_quiz_question.correct_answer == 'correct'
    assert new_quiz_question.incorrect_answers == ["incorrect_1", "incorrect_2", "incorrect_3"]


def test_quiz_taken(new_quiz_taken, new_quiz_question):
    assert new_quiz_taken.uuid == '1234'
    assert new_quiz_taken.difficulty == 'easy'
    assert new_quiz_taken.questions == [new_quiz_question, new_quiz_question, new_quiz_question]


def test_quiz_result(new_quiz_result):
    assert new_quiz_result.user_id == 1
    assert new_quiz_result.quiz_uuid == '4321'
    assert new_quiz_result.points == 1


def test_calculate_points(new_quiz_taken):
    answers = {1: 'correct',
               2: 'incorrect',
               3: 'correct'}
    assert calculate_points(new_quiz_taken, answers) == 2
