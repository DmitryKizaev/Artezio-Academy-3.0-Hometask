"""Homework 7 Task 1"""

# Напишите параметризованный декоратор, который считает
# и выводит при каждом вызове среднее время работы функции
# за n последних вызовов. Время выводить в миллисекундах.
# @average_time(n=2) для foo(a): sleep(a) return a
# foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
# foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
# foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."

from time import time, sleep


def average_time(n):
    """Среднее время работы функции за n последних вызовов"""
    a = []

    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            t1 = time()
            result = func(*args, **kwargs)
            t2 = time()
            a.append(t2 - t1)
            if len(a) > n:
                a.pop(0)
            print("Среднее время работы: {} мс.".format(round(sum(a) / len(a))*1000))
            return result
        return wrapper
    return inner_decorator


@average_time(n=2)
def foo(a):
    sleep(a)
    return a


print(foo(3))
print(foo(7))
print(foo(1))
print(foo(4))
print(foo(0))
print(foo(0))
print(foo(1))
