def last_element(lst):
    if len(lst) == 0:
        return 'none'
    return lst[-1]


print(last_element([1, 2, 3]))
print(last_element([1, 2, 3, 4, 8, 10, 50]))
print(last_element([]))
