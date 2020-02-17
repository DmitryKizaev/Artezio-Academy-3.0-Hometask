"""Homework 6 Part 2 Generators Task 4"""

# Написать функцию-генератор cycle которая бы возвращала циклический итератор.

from time import sleep


def cycle(it):
    # первый проход
    values = []
    for i in it:
        values.append(i)  # добавим в список
        yield i  # поставим значение
    # последующие проходы: крутим список
    count = 0
    while True:
        yield values[count]  # поставляем эл-т
        count += 1  # увеличим счетчик
        if count == len(values):  # если перебор (в списке у нас от 0 до len-1):
            count = 0  # зациклим


i = iter(["oh", "###", "here", "we", "go", "again", "------"])
c = cycle(i)
while True:
    print(next(c))
    sleep(0.5)
