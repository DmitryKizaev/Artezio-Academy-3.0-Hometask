"""Homework 6 Part 2 Generators Task 1"""

# Напишите итератор EvenIterator, который позволяет
# получить из списка все элементы, стоящие на чётных индексах.


class EvenIterator:
    """Четный итератор"""
    def __init__(self, values, start=0):
        self.values = values
        self.limit = len(values) - 1
        self.current = start - 2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration("Iteration stopped: next index is [{}],"
                                " last index in list is [{}]"
                                .format(self.current, self.limit))
        return self.values[self.current]


def list_inp(n):
    """Allows to enter a list and prints the result"""
    lin = list()
    for i in range(0, n):
        print("Enter element", i)
        lin.append(input())
    return lin


print("Enter length of list:")
N = int(input())
list_1 = list_inp(N)

print("Result for EvenIterator:")
for i in EvenIterator(list_1):
    print(i, end=' ')

print()

print("Check for EvenIterator:")
for i in range(0, N, 2):
    print(list_1[i], end=' ')

print("\n")

print("Let's try next(<iterator>):")
list_2 = ["i", "want", "to", "know", "python",
          "and", "get", "a", "job", "in", "Artezio"]
print(list_2)
ei = EvenIterator(list_2)
try:
    print(next(ei))
    print(next(ei))
    print(next(ei))
    print(next(ei))
    print(next(ei))
    print(next(ei))
except StopIteration as excep:
    print(excep)
