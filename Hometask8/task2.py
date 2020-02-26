"""Homework 8 Task 2"""

# Напишите функцию, которая принимает три аргумента:
# 1) число, количество денег в исходной валюте, float;
# 2) исходная валюта, трехсимвольная строка, str;
# 3) целевая валюта, трехсимвольная строка, str;
# и возвращает количество денег в целевой валюте (тип float).
# Для получения курса валют воспользуйтесь https://api.exchangerate-api.com

import requests


def update_course(curr):
    """Course updater auxiliary function"""
    # можно было не прописывать отдельно, но на мой взгляд действие полезное
    # и по смыслу его лучше выделить - может пригодиться при развитии "проекта"
    try:
        url = "https://api.exchangerate-api.com/v4/latest/" + curr
        courses = requests.get(url)
        if not (courses and courses.status_code == 200):
            print("URL {} unreachable!".format(url))
            print("Probably you should check supported currencies:")
            print("https://www.exchangerate-api.com/"
                  "docs/supported-currencies\n")
            return None
        courses = eval(courses.text)
        return courses
    except requests.ConnectionError:
        print("URL incorrect!")
        return None


def sberkot(cash, name_from, name_into):
    """Financial converter"""
    if not (cash.isdigit()
            and isinstance(name_from, str) and len(name_from) == 3
            and isinstance(name_into, str) and len(name_into) == 3):
        print("Incorrect input data\n")
        return None
    cash = float(cash)

    print("Converting", cash, name_from, "into", name_into)
    courses = update_course(name_from)
    try:
        course = float(courses["rates"][name_into])
        print("Course from {}".format(courses["date"]))
        print("1 {} is {} {}\n".format(name_from, course, name_into))
        return cash * course
    except KeyError as wrong_curr:
        print(wrong_curr, "is not a supported target currency.")
        print("Check supported currencies:")
        print("https://www.exchangerate-api.com/docs/supported-currencies\n")
        return None
    except TypeError:
        print("Courses for \"{}\" unavailable\n".format(name_from))
        return None


print("Enter your currency")
exchange_from = input()
print("Enter target currency")
exchange_to = input()
print("Enter sum to exchange")
exchange_sum = input()

print("\nSberkot({}, {}, {}):"
      .format(exchange_sum, exchange_from, exchange_to))

print(sberkot(exchange_sum, exchange_from, exchange_to))
