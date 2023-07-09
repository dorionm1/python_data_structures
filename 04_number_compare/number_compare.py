def number_compare(a, b):
    if a == b:
        return 'Numbers are equal'
    if a < b:
        return 'Second is Greater'
    if a > b:
        return 'First is greater'
    
print(number_compare(1, 1))
print(number_compare(-1, 1))
print(number_compare(1, -2))
