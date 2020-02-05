"""Homework 1 Task 2"""

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


def symbol_count(_s):
    """Makes a dictionary with character frequency in a string"""
    _d = {}
    for letter in _s:
        if _d.get(letter, 0):
            _d[letter] += 1
        else:
            _d[letter] = 1
    _d = dict_value_sort(_d)
    return _d


def dict_value_sort(_d):
    """Sorts a dictionary by value from biggest values to smallest"""
    _d_list_sorted = sorted(_d, key=_d.__getitem__, reverse=True)
    _d_sorted = {}
    for i in _d_list_sorted:
        _d_sorted[i] = _d[i]
    return _d_sorted


print("Enter string")
print(symbol_count(input()))
