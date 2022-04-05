import math


def prime_factors(number):
    check_input_argument(number)
    result = []
    while number % 2 == 0:
        result.append(2)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):

        while number % i == 0:
            result.append(i)
            number = number / i
    if number > 2:
        result.append(number)
    return result


def check_input_argument(number):
    if type(number) != int:
        raise ValueError('Incorrect type')
