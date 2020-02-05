"""Homework 1 Task 5"""

# 5. You are given with 3 sets, find if 3rd set is a subset of 1st and 2nd sets
# Input: set([1,2]), set([2,3]), set([2])
# Expected result: True
# Input: set([1,2]), set([3,4]), set([5])
# Expected result: False


def find_subset(_s1, _s2, _s3):
    """Returns True if 3rd set is a subset of 1st and 2nd sets"""
    if _s3.issubset(_s1) and _s3.issubset(_s2):
        return True
    return False


def inp_set():
    """Allows to enter a set and prints the result"""
    s_inp = set()
    print("Enter number of elements in set")
    n = int(input())
    for i in range(1, n+1):
        print("Enter element", i)
        s_inp.add(input())
    print(s_inp)
    return s_inp


s1 = inp_set()
s2 = inp_set()
s3 = inp_set()
print()
print(find_subset(s1, s2, s3))
