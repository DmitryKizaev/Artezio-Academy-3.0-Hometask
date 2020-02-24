"""Homework 7 Task 3"""

# Преобразовать вызов функции с конечным количеством позиционных аргументов
# f(a, b, c, d) в вызов вида f(a)(b)(c)(d), используя декоратор.
# Пример:
# @carry
# def foo(a, b):
#     return a + b


def carry(function, arg_num=None):
    """Декоратор для каррирования"""
    if arg_num is None:
        arg_num = function.__code__.co_argcount

    def func_call(*first_bracket):
        """Возвращает либо функцию, либо carry, если не хватает аргументов"""
        if len(first_bracket) == arg_num:
            return function(*first_bracket)

        def bracket_merge(*tail_args):
            """Сливает вместе 2 самые последние скобки аргументов"""
            args_together = first_bracket + tail_args
            return function(*args_together)

        return carry(bracket_merge, arg_num - len(first_bracket))
    return func_call


@carry
def my_func(a, b, c):
    """Пример 1"""
    print('%d-%d-%d' % (a, b, c))


@carry
def foo_1(a, b, c, d):
    """Пример 2"""
    return a + b + c + d


@carry
def foo_2(a, b):
    """Пример 3"""
    return a + b


my_func(11, 22, 33)
my_func(44, 55)(66)
my_func(77)(88)(99)
print(foo_1(1)(5)(4)(10))
print(foo_2(1)(5))
