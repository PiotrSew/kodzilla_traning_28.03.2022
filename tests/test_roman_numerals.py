from project.roman_numerals import from_roman_to_int, from_int_to_roman
import pytest

correct_answers = {
    'I': 1,
    'VI': 6,
    'IX': 9,
    'XX': 20,
    'XL': 40,
    'CC': 200,
    'MMMCMXCIX': 3999,
}

incorrect_answers = ['IIII', 'IIIIIIII', 'XIIII', 'IIIX']


def test_correct_answers_in_from_roman_to_int():
    for roman in correct_answers:
        assert from_roman_to_int(roman) == correct_answers[roman]


def test_correct_answers_in_from_int_to_roman():
    for roman in correct_answers:
        assert from_int_to_roman(correct_answers[roman]) == roman


def test_incorrect_answers_in_from_roman_to_int():
    for roman in incorrect_answers:
        with pytest.raises(ValueError):
            from_roman_to_int(roman)
