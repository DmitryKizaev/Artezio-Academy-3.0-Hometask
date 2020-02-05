"""Homework 1 Task 6"""

# 6. Write a Python script to generate and print a dictionary that contains
# a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


def square_dic(_n):
    """Creates a dictionary in the form (x, x*x)"""
    dic = {}
    if _n <= 0:
        return "n must be >= 1"
    for i in range(1, _n + 1):
        dic[i] = i * i
    return dic


print("Enter n")
print(square_dic(int(input())))
