"""Homework 1 Task 7"""

# 7. Write a Python script to merge two Python dictionaries


def merge_dict(_d1, _d2):
    """My implementation of dict.update"""
    _d3 = _d1
    for i in _d2:
        _d3[i] = _d2[i]
    return _d3


def input_dict(_dic):
    """Allows to enter a dictionary and prints the result"""
    print("Enter number of elements in dictionary")
    n = int(input())
    for i in range(1, n+1):
        print("Enter key", i)
        k = input()
        print("Enter value", i)
        v = input()
        _dic[k] = v
    print(_dic)


d1 = {}  # а здесь, тоже нужен UPPER_CASE naming style?
d2 = {}
input_dict(d1)
print()
input_dict(d2)
print()
print(d1, d2)

print("Merged:")
print(merge_dict(d1, d2))
