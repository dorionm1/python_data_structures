def partition(lst, fn):
    lst1 = []
    lst2 = []

    for x in lst:
        if fn == 'is_even':
            if x % 2 == 0:
                lst1.append(x)
            else:
                lst2.append(x)
        elif fn == 'is_string':
            if isinstance(x, str):
                lst1.append(x)
            else:
                lst2.append(x)

    return lst1, lst2
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

print(partition([1, 2, 3, 4], 'is_even'))
print(partition(["hi", None, 6, "bye"], 'is_string'))