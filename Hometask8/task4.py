"""Homework 8 Task 4"""

# Напишите шаблон регулярного выражения, который соответствовал бы следующему формату
# времени: YYYY-MM-DDThh:mm:ss±hh:mm (ISO формат).

import re


def test_exp(regexp, string):
    """Prints result of <regular expression> test on <string>"""
    try:
        print(re.search(regexp, string).group())
    except AttributeError:
        print("Correct expression not found")


MY_TEXT_TRUE_1 = '2005-08-09T18:31:42+03:30'  # UTC +
MY_TEXT_TRUE_2 = '1765-11-07T18:31:42-03:30'  # UTC -

MY_TEXT_FALSE_1 = '2O05-08-09T18:31:42+03:30'  # O вместо нуля
MY_TEXT_FALSE_2 = '1765-13-18T18:31:42-03:30'  # 13 месяц
MY_TEXT_FALSE_3 = '1765-11-18T25:31:42-03:30'  # 25 час

#            YYYY -    MM     -      DD       T
MY_REGEX = r"\d{4}-(0\d|1[12])-([0-2]\d|3[01])T([01]" \
              r"[\d]|2[0-3]):([0-5]\d):([0-5]\d)[+-]([0-5]\d):([0-5]\d)"
#                   hh      :    mm   :    ss    +-     hh   :   mm

test_exp(MY_REGEX, MY_TEXT_TRUE_1)
test_exp(MY_REGEX, MY_TEXT_TRUE_2)
test_exp(MY_REGEX, MY_TEXT_FALSE_1)
test_exp(MY_REGEX, MY_TEXT_FALSE_2)
test_exp(MY_REGEX, MY_TEXT_FALSE_3)
