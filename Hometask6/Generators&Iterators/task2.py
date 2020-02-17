"""Homework 6 Part 2 Generators Task 2"""

# Написать генератор списка для получения списка
# всех публичных атрибутов объекта


def get_public(obj):
    """Получить публичные атрибуты объекта"""
    return [i for i in dir(obj) if not i.startswith('_')]


# В Python для обозначения protected атрибутов
# используют "_", для private — "__", так что
# вернем атрибуты через dir если они подходят

C = complex()
print(get_public(C))
