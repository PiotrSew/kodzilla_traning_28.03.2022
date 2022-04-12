from typing import Dict, List

import requests
import json


class UsersController:
    data = {
    }

    def register(self, email: str, password: str):
        self.data[email] = password

    def login(self, email: str, password: str):
        if email in self.data and self.data[email] == password:
            # login successful
            pass
        else:
            # login unsuccessful
            pass


class QuizController:
    result = []

    def take_quiz(self, email: str, answers: List[str]):
        points = 0
        # mock this!
        quiz_request = self._get_quiz()
        quiz_data = json.loads(quiz_request.text)
        for question, answer in zip(quiz_data['results'], answers):
            if question['correct_answer'] == answer:
                points += 1
        self.result.append(
            {
                'email': email,
                'points': points
            }
        )

    @staticmethod
    def _get_quiz():
        return requests.get(' https://opentdb.com/api.php?amount=10')

    def ranking(self) -> List[Dict]:
        return sorted(self.result, key=lambda a: a['points'], reverse=True)
