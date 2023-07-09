def is_palindrome(phrase):
    rev_phr = phrase[::-1]

    if phrase.lower().replace(" ", "") == rev_phr.lower().replace(" ", ""):
        return True
    return False

print(is_palindrome('tacocat'))
print(is_palindrome('noon'))
print(is_palindrome('robert'))

print(is_palindrome('Noon'))
print(is_palindrome('taco cat'))

"""Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
