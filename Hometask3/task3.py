"""Homework 3 Task 3"""

# Написать функцию, которая будет принимать только
# 4 позиционных аргументы (все аргументы числовые).
# Функция должна вернуть среднее арифметическое аргументов
# и самый большой аргумент за все время вызовов этой функции.
# Пример: foo(1,2,3,4) -> 2.5, 4
#         foo(-3, -2, 10, 1) -> 1.5, 10
#         foo(7,8,8,1) -> 6, 10

history_max = None


def four_args(*args):
    """Найти среднее арифм. 4 чисел, запомнить max аргумент за все время"""
    if len(args) != 4:
        return "Incorrect number of arguments"

    global history_max
    result = 0
    for i in args:
        result += i
    local_max = sorted(args)[3]
    if history_max is None or local_max > history_max:
        history_max = local_max
    return [result/4, history_max]


print(four_args(1, 2, 3, 4))
print(four_args(-3, -2, 10, 1))
print(four_args(7, 8, 8, 1))
