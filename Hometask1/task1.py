"""Homework 1 Task 1"""

# 1. Ensure that the first and last names of people begin with a capital letter
# Given a full name, your task is to capitalize the name appropriately.
# 0 < len(S) < 1000
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized.
# Output Format:Print the capitalized string, S.


def capital(username):
    """Capitalizes each word in a string formatted as <name_surname>"""
    split = username.find(" ", 0, len(username))
    if username:
        name = (username[0:split])
        surname = username[split+1:len(username)]
        username = name.capitalize() + ' ' + surname.capitalize()
    else:
        return "Error: empty username"
    return username


print("Enter username")
print(capital(input()))
