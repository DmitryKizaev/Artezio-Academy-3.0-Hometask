"""Homework 6 Part 1 Exceptions Task 1"""

# You are given a string S.
# Your task is to find out whether S is a valid regex or not.
# The first line contains integer T, the number of test cases.
# The next T lines contain the string S.
# Print "True" or "False" for each test case without quotes.

import re


def re_check(string):
    """Проверка строки на соответствие регулярному выражению"""
    try:
        re.compile(string)
        return True
    except re.error:
        return False


STRINGS = []
T = int(input())

for i in range(T):
    STRINGS.append(input())

for i in STRINGS:
    print(re_check(i))
