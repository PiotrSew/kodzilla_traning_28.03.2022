from prime_factors import prime_factors


def test_import_prime_factors():
    try:
        assert callable(prime_factors), "tic_tac_toe not callable"
    except ImportError as error:
        assert False, error


if __name__ == '__main__':
    for test in (
            test_import_prime_factors,
    ):
        print(f'{test.__name__}: ', end='')
        try:
            test()
            print('OK')
        except AssertionError as error:
            print(error)
