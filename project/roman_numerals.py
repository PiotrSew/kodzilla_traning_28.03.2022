from re import search

num = [1, 4, 5, 9, 10, 40, 50, 90,
       100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL",
       "L", "XC", "C", "CD", "D", "CM", "M"]
roman_translator = dict(zip(sym, num))
incorrect_symbols = ["IIII", "IIX"]


def from_roman_to_int(roman):
    check_if_roman_correct(roman)
    i = 0
    number = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_translator:
            number += roman_translator[roman[i:i + 2]]
            i += 2
        else:
            number += roman_translator[roman[i]]
            i += 1
    return number


def from_int_to_roman(integer):
    i = 12
    roman = ""
    while integer:
        div = integer // num[i]
        integer %= num[i]

        while div:
            roman += sym[i]
            div -= 1
        i -= 1
    return roman


def check_if_roman_correct(roman):
    roman_signs_regex = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    if not bool(search(roman_signs_regex, roman)):
        raise ValueError('Incorrect roman format')
