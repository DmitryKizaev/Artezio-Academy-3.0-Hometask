"""Homework 7 Task 2"""

# Напишите параметризованный декоратор для классов, который
# будет считать и выводить время работы методов класса, имена
# которых переданы в параметрах декоратора.

from time import time, sleep


def for_some_methods(decorator, *names):
    """Декорирует выбранным декоратором названные методы класса"""
    def class_decorator(my_class):
        for name in names:
            if name in my_class.__dict__:
                if callable(getattr(my_class, name)) and not name.startswith('_'):
                    setattr(my_class, name, decorator(getattr(my_class, name)))
            return my_class
    return class_decorator


def func_time(func):
    """Декорирует выбранным декоратором функцию"""
    def wrapper(*args, **kwargs):
        time_start = time()
        tmp = func(*args, **kwargs)
        time_stop = time()
        print("Функция: {}".format(func.__name__))
        print("Время работы: {} мс.".format(round(time_stop-time_start)*1000))
        return tmp
    return wrapper


def check_time(*names):
    """Не будем каждый раз писать имя декоратора"""
    return for_some_methods(func_time, *names)


@check_time("inspect")
class Spam:
    """Тестовый класс"""
    def __init__(self, s):
        """Конструктор"""
        self.s = s

    def inspect(self):
        """Функция 1"""
        sleep(self.s)

    def show(self):
        """Функция 2"""
        return self.s


A = Spam(2)
A.inspect()  # должно вывести сообщение о времени работы
A.show()  # ничего не выводить
