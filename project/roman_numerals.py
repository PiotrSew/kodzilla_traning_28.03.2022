def from_roman_to_int(roman):
    roman_translator = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    i = 0
    num = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman[i:i + 2] in roman_translator:
            num += roman_translator[roman[i:i + 2]]
            i += 2
        else:
            # print(i)
            num += roman_translator[roman[i]]
            i += 1
    return num


def from_int_to_roman(integer):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
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
