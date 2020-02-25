"""Homework 8 Task 5"""

# Напишите шаблон регулярного выражения, который соответствовал бы паролю,
# состоящему из 8-12 символов, среди которых могут быть строчные и заглавные буквы латинского
# алфавита, цифры, нижнее подчеркивание, звездочка, процент и амперсанд.
# Пароль обязательно должен включать в себя одну строчную букву, одну заглавную букву и одну цифру.

import re


def test_exp(regexp, string):
    """Prints result of <regular expression> test on <string>"""
    try:
        print(re.search(regexp, string).group())
    except AttributeError:
        print("Correct expression not found")


MY_TEXT_TRUE_1 = "Qwerty123"
MY_TEXT_TRUE_2 = "b_Ab*a%Ab&8"

MY_TEXT_FALSE_1 = "Wh0Let@@out"  # запрещенный спецсимвол @
MY_TEXT_FALSE_2 = "qwerty123"  # нет заглавных
MY_TEXT_FALSE_3 = "QWERTY123"  # нет маленьких
MY_TEXT_FALSE_4 = "Qwerty123Qwerty123Qwerty123"  # не проходит по длине

MY_REGEX = r"(?=^.{8,12}$)(?=.*\d)(?=.*[A-Z])(?=.*[a-z])((?!.*[\W])|(?=.*[*%&])).*$"

# (?=^.{8,12}$)
# вид строки: начало ^, потом есть .{8,12} от 8 до 12 любых символов, потом конец $

# (?=.*\d)(?=.*[A-Z])(?=.*[a-z])
# проверим найдутся ли после любых символов .* строки числа \d
# проверим найдутся ли после любых символов .* строки буквы [A-Z]
# проверим найдутся ли после любых символов .* строки буквы [a-z]

# ((?!.*[\W])|(?=.*[*%&])) - и в строке при этом
# ЛИБО не найдено ничего кроме чисел, букв и подчеркивания [\W]
# ЛИБО найдены спецсимволы разрешенные: *%&

# если все проверки прошли вернуть .*$ все символы до конца строки

test_exp(MY_REGEX, MY_TEXT_TRUE_1)
test_exp(MY_REGEX, MY_TEXT_TRUE_2)
test_exp(MY_REGEX, MY_TEXT_FALSE_1)
test_exp(MY_REGEX, MY_TEXT_FALSE_2)
test_exp(MY_REGEX, MY_TEXT_FALSE_3)
test_exp(MY_REGEX, MY_TEXT_FALSE_4)