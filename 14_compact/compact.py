def compact(lst):
    return list(filter(bool,lst))
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
