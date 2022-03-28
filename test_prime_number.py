from prime_factors import prime_factors


def test_import_prime_factors():
    try:
        assert callable(prime_factors), "tic_tac_toe not callable"
    except ImportError as error:
        assert False, error


def test_correct_number():
    winner = prime_factors(3958159172)
    assert winner == [2, 2, 11, 2347, 38329], f"expected [2, 2, 11, 2347, 38329], got {winner}"


def test_illegal_input_format():
    try:
        prime_factors('Ala ma kota')
        assert False, "ValueError expected"
    except ValueError:
        pass


if __name__ == '__main__':
    for test in (
            test_import_prime_factors,
            test_correct_number,
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)
