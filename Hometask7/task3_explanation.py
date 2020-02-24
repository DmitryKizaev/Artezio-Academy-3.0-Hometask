"""Homework 7 Task 3: HOW DOES IT WORK"""

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
        # выясняем сколько (NUM) переданной функции нужно
        # получить аргументов для успешного выполнения

    print("Вызван carry для", function.__name__)
    print("Необходимо аргументов: arg_num", arg_num)

    def func_call(*first_bracket):
        """Возвращает либо функцию, либо carry, если не хватает аргументов"""
        # подбираем первую скобку аргументов в вызове: в ней X аргументов
        print("Пытаемся вызвать функцию", function.__name__)
        print("first_bracket: аргументов", len(first_bracket), first_bracket)
        if len(first_bracket) == arg_num:
            # если X = NUM то мы собрали аргументы в нужном количестве:
            print("Собрали достаточно аргументов:", len(first_bracket))
            print("Вернем результат:", function.__name__, first_bracket)
            return function(*first_bracket)
            # возвращаем функцию

        def bracket_merge(*tail_args):
            """Сливает вместе 2 самые последние скобки аргументов"""
            print("Сливаем списки аргументов:")
            print("first_bracket: аргументов", len(first_bracket), first_bracket)
            print("tail_args: аргументов", len(tail_args), tail_args)
            args_together = first_bracket + tail_args
            print("args_together", args_together)
            # сливаем вместе в одну скобку аргументы полученные здесь и в one
            print("Вернем результат:", function.__name__, args_together)
            return function(*args_together)

        # если нам не хватает аргументов для выполнения: сольем вместе 2 последние скобки
        # и каррируем результат еще раз, к успеху придем когда получим оставшиеся NUM - X аргументов
        print("Мало аргументов для {}, пробуем еще раз carry для 'хвоста'\n"
              .format(function.__name__))
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


print("\n-------------Тест 1-------------\n")
my_func(11, 22, 33)
print("\n-------------Тест 2-------------\n")
my_func(44, 55)(66)
print("\n-------------Тест 3-------------\n")
my_func(77)(88)(99)
print("\n-------------Тест 4-------------\n")
print(foo_1(1)(5)(4)(10))
print("\n-------------Тест 5-------------\n")
print(foo_2(1)(5))
