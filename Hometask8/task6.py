"""Homework 8 Task 6"""

# Напишите шаблон регулярного выражения, который соответствует вопросительным
# предложениям, в которых одно слово (более 2 символов) повторяется 4 или более раз.

import re


def test_exp(regexp, string):
    """Prints result of <regular expression> test on <string>"""
    try:
        print(re.search(regexp, string).group())
    except AttributeError:
        print("Correct expression not found")


MY_TEXT_TRUE_1 = 'И кто же это был, тот, кто за, или те, кто против, кто?'
MY_TEXT_TRUE_2 = 'Булка, большая булка, средняя булка или не булка?'

MY_TEXT_FALSE_1 = 'Ку ку ку ку?'  # регистр
MY_TEXT_FALSE_2 = 'Если булка - большая булка, назовем её булка-пребулка?'
MY_TEXT_FALSE_3 = 'был был был был был'  # нет вопросительного знака
MY_TEXT_FALSE_4 = 'а а а а а а?'  # короткие слова
MY_TEXT_FALSE_5 = 'тридцать три коровы коровы коровы?'  # нет повторов

MY_REGEX = r"((\b([a-яА-Я]{2,})\b){4,}).*\?$"

test_exp(MY_REGEX, MY_TEXT_TRUE_1)
test_exp(MY_REGEX, MY_TEXT_TRUE_2)
print()
test_exp(MY_REGEX, MY_TEXT_FALSE_1)
test_exp(MY_REGEX, MY_TEXT_FALSE_2)
test_exp(MY_REGEX, MY_TEXT_FALSE_3)
test_exp(MY_REGEX, MY_TEXT_FALSE_4)
test_exp(MY_REGEX, MY_TEXT_FALSE_5)
