"""Homework 1 Task 9"""

# 9. Write a Python program to remove duplicates from a list.


def remove_dup(_list):
    """Removes duplicates from a list keeping order of elements"""
    elems = set(_list)
    newlist = []
    for i in _list:
        if i in elems:
            newlist.append(i)
            elems.remove(i)
    return newlist


print("Enter number of elements in list")
n = int(input())

elements = []
for i in range(1, n+1):
    print("Enter value", i)
    elements.append(input())
print(elements)

print("Removing duplicates...")
print(remove_dup(elements))
print(type(elements))
