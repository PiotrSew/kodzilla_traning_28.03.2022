def is_palindrome(data):
    check_data(data)
    palindrome = data[::-1]
    return data == palindrome


def check_data(var):
    if type(var) is not str or var == '' or var.count(' '):
        raise TypeError('Incorrect type')


palindromes = ['kajak', 'sedes', 'oko']
for word in palindromes:
    assert is_palindrome(word)

not_palindromes = ['palindrom', 'kapelusz']
for word in not_palindromes:
    assert not is_palindrome(word)

incorrect_data = ['', ' ', 123, ['abc'], (1, 2)]
for word in incorrect_data:
    try:
        is_palindrome(word)
    except TypeError as err:
        pass
