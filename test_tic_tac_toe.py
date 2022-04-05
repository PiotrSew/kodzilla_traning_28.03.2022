import unittest

from tic_tac_toe import tic_tac_toe_winner


class TestFinishedGame(unittest.TestCase):  #➜ 1

    def test_3x_in_a_row(self):  #➜ 2
        self.assertEqual(tic_tac_toe_winner('XXX O O  '), 'X')  #➜ 3

    # kolejne testy dla planszy opisujących zakończone gry


class TestUnfinishedGame(unittest.TestCase):

    def test_empty_board(self):
        self.assertIsNone(tic_tac_toe_winner(' '*9))  #➜ 4

    # kolejne testy dla niezakończonych gier


class TestInvalidBoard(unittest.TestCase):

    def test_illegal_symbols(self):
        with self.assertRaises(ValueError):  #➜ 5
            tic_tac_toe_winner('    E    ')

    # kolejne testy nieprawidłowego wejścia
