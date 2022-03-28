def tic_tac_toe_winner(board):
    check_arguments(board)
    return dummy_tic_tac_toe_algorithm(board)


def dummy_tic_tac_toe_algorithm(board):
    x_count = board.count('X')
    o_count = board.count('O')
    space_flag = True if board.count(' ') > 0 else False
    winner = None
    if space_flag:
        if x_count > o_count:
            winner = 'X'
        elif o_count > x_count:
            winner = 'O'
    return winner


def check_arguments(board):
    if len(board) != 9:
        raise ValueError('Incorrect board')
    elif abs(board.count('X') - board.count('O')) > 1:
        raise ValueError('Incorrect number of marks')


# TESTS
test_boards = [('XOX  O XO', None),
               ('XO X OX  ', 'X'),
               ('XO OX   X', 'X'),
               ('XOXOXOXOX', None)]
for board in test_boards:
    assert tic_tac_toe_winner(board[0]) == board[1]

incorrect_test_boards = [('', 'Incorrect board'),
                         ('XXXXXXXXX', 'Incorrect number of marks'),
                         ('XOXOXOXOXOXOXOXOX', 'Incorrect board')]

for board in incorrect_test_boards:
    try:
        tic_tac_toe_winner(board[0])
    except ValueError as err:
        assert str(err) == board[1]
