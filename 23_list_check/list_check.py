def list_check(lst):
    return all(isinstance(i, type(lst[0])) for i in lst[1:])
        
"""Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
print(list_check([[1], [2, 3]]))
print(list_check([[1], "nope"]))