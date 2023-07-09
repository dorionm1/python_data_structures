def remove_every_other(lst):
    new_lst = []

    for el in lst:
        if lst.index(el) % 2 == 0:
            new_lst.append(el)
    return new_lst

    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """


lst = [1, 2, 3, 4, 5]

print(remove_every_other(lst))

print(lst)