"""Homework 1 Task 10"""

# 10. Write a Python program to get the difference between the two lists


def list_diff(_list1, _list2):
    """Excludes all elements of list2 from list1"""
    list3 = []
    for i in _list1:
        if i not in _list2:
            list3.append(i)
    return list3


def list_inp():
    """Allows to enter a list and prints the result"""
    lin = list()
    print("Enter number of elements in list")
    n = int(input())
    for i in range(1, n+1):
        print("Enter element", i)
        lin.append(input())
    print(lin)
    return lin


print("Enter list 1")
list1 = list_inp()
print("Enter list 2")
list2 = list_inp()
print("l1-l2:")
print(list_diff(list1, list2))
print("l2-l1:")
print(list_diff(list2, list1))
