"""Homework 1 Task 8"""

# 8. Write a Python program to find the highest 3 values in a dictionary


def dict_check_digit(_dic):
    """True if every value in a dictionary is a number"""
    for i in _dic:
        if isinstance(_dic[i], int):
            if not _dic[i].isdigit():
                return False
    return True


def pop_max(_dic):
    """Pops a biggest value from a dictionary"""
    dic_temp = _dic
    imax = list(dic_temp.keys())[0]

    for i in dic_temp:
        if dic_temp[i] > dic_temp[imax]:
            imax = i
    return dic_temp.pop(imax)


def input_dict():
    """Allows to enter a dictionary and prints the result"""
    _dic = {}
    print("Enter number of elements in dictionary")
    n = int(input())
    for i in range(1, n+1):
        print("Enter key", i)
        k = input()
        print("Enter value", i)
        v = str(input())
        _dic[k] = v
    print(_dic)
    return _dic


d = input_dict()
if dict_check_digit(d):
    for i in d:
        d[i] = int(d[i])

if len(d) >= 3:
    for i in range(3):
        print(i+1, "max element is", pop_max(d))
else:
    print("dictionary is too short")
