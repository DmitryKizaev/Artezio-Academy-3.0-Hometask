"""Homework 1 Task 4"""

# 4. Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


def str_in_list(_list):
    """Сounts the number of strings with definite parameters from a list"""
    count = 0
    for word in _list:
        if len(word) >= 2 and word[0] == word[len(word)-1]:
            count += 1
    return count


print("Enter number of elements in list")
n = int(input())  # насколько важно писать здесь n как константу в UPPER_CASE, как просит pylint?

strings = []
for i in range(n):
    print("Enter string", i+1)
    t = input()
    strings.append(t)

print(str_in_list(strings))
