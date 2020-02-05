"""Homework 1 Task 3"""

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def str_cut(_s):
    """Makes a string of the first 2 and the last 2 chars of given, or "EMPTY STRING"""
    if len(_s) < 2:
        s_new = "Empty String"
    else:
        s_new = _s[:2] + _s[-2:]
    return s_new


print("Enter string")
print(str_cut(input()))
