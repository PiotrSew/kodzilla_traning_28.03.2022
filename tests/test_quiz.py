from unittest.mock import MagicMock
from project.quiz import UsersController, QuizController


class RequestMock:
    def __init__(self, text):
        self.text = text


quiz_controller = QuizController()
quiz_controller._get_quiz = MagicMock(
    return_value=RequestMock(
        text='{"response_code":0, "results":[{"category":"Science: Computers","type":"multiple","difficulty":"easy","question":"How many kilobytes in one gigabyte (in decimal)?","correct_answer":"1000000","incorrect_answers":["1024","1000","1048576"]}]}'))


def test_mock():
    assert quiz_controller._get_quiz().text == '{"response_code":0, "results":[{"category":"Science: Computers","type":"multiple","difficulty":"easy","question":"How many kilobytes in one gigabyte (in decimal)?","correct_answer":"1000000","incorrect_answers":["1024","1000","1048576"]}]}'


def test_take_quiz_wrong_answer():
    quiz_controller.take_quiz('mail', ['1024'])
    assert quiz_controller.result == [{'email': 'mail', 'points': 0}]


def test_take_quiz():
    quiz_controller.take_quiz('mail', ['1000000'])
    assert quiz_controller.result == [{'email': 'mail', 'points': 0}, {'email': 'mail', 'points': 1}]


def test_ranking():
    assert quiz_controller.ranking() == [{'email': 'mail', 'points': 1}, {'email': 'mail', 'points': 0}]
