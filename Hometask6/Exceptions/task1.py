"""Homework 6 Part 1 Exceptions Task 1"""

# You are given two values a and b.
# Perform integer division and print a/b.
# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b
# 0 < T < 10
# Output Format: Print the value of a/b.
# In the case of ZeroDivisionError or ValueError, print the error code.

STRINGS = []
T = int(input())

for i in range(T):
    STRINGS.append(input())

for i in STRINGS:
    try:
        space = (i.index(" "))
        a = int(i[:space])
        b = int(i[space+1:])
        print(a // b)
    except ValueError as err_code:
        print("Error Code:", err_code)
    except ZeroDivisionError as err_code:
        print("Error Code:", err_code)
