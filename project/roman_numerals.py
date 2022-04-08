num = [1, 4, 5, 9, 10, 40, 50, 90,
       100, 400, 500, 900, 1000]
sym = ["I", "IV", "V", "IX", "X", "XL",
       "L", "XC", "C", "CD", "D", "CM", "M"]
roman_translator = dict(zip(sym, num))


def from_roman_to_int(roman):
    i = 0
    number = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_translator:
            number += roman_translator[roman[i:i + 2]]
            i += 2
        else:
            # print(i)
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
