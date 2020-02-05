"""Homework 3 Task 1"""


# 1. Написать несколько функций, которые в качестве единственного аргумента
#  принимают список (или кортеж) целых чисел.
#      - первая функция должна вернуть квадраты элементов коллекции;
#      - вторая функция должна вернуть только элементы на четных позициях;
#      - третья функция возвращает кубы четных элементов на нечетных позициях.


def squares(_list):
    """Возвращает квадраты элементов коллекции"""
    squares_list = []
    for i in _list:
        squares_list.append(i * i)
    return squares_list


def chet_human(_list):
    """Возвращает элементы на "человеческих" четных позициях"""
    # позиция элементов считается на "человеческий" глаз
    # в списке [1, 2, 3, 4, 5] 2 - второй элемент, 4 - четвертый и т.д.
    chet_list = []
    for i in range(1, len(_list), 2):
        chet_list.append(_list[i])
    return chet_list


def chet_machine(_list):
    """Возвращает элементы на четных позициях по фактическому номеру"""
    # позиция элементов считается по номеру в списке, т.е. с 0
    # в списке [1, 2, 3, 4, 5] 1 - нулевой элемент, 3 - второй и т.д.
    chet_list = []
    for i in range(0, len(_list), 2):
        chet_list.append(_list[i])
    return chet_list


def cube_human(_list):
    """Возвращает кубы чет. элементов на "человеческих" нечетных позициях"""
    # позиция элементов считается на "человеческий" глаз
    # в списке [1, 2, 3, 4, 5] 1 - первый элемент, 3 - третий и т.д.
    cube_list = []
    #
    for i in range(0, len(_list), 2):
        if not _list[i] % 2:
            cube_list.append(_list[i] ** 3)
    return cube_list


def cube_machine(_list):
    """Возвращает кубы чет. элементов на нечет. позициях по фактич. номеру"""
    # позиция элементов считается по номеру в списке, т.е. с 0
    # в списке [1, 2, 3, 4, 5] 2 - первый элемент, 4 - третий и т.д.
    cube_list = []
    for i in range(1, len(_list), 2):
        if not _list[i] % 2:
            cube_list.append(_list[i] ** 3)
    return cube_list


lin = []
print("Enter number of elements in list")
n = int(input())
for i in range(1, n + 1):
    print("Enter element", i)
    lin.append(int(input()))
print("Исходный список:", lin)
print()
print("f1:", squares(lin))
print("f2 по-человечески:", chet_human(lin))
print("f2 по-машинному:", chet_machine(lin))
print("f3 по-человечески:", cube_human(lin))
print("f3 по-машинному:", cube_machine(lin))
