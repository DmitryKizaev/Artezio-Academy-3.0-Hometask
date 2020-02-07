"""Hometask 4"""

# 5. Внутри модуля check_response напишите функцию, которая на вход принимает
# URL как строку (например, 'http://google.ru/') и использует функцию из
# предыдущего файла, чтобы сделать запрос. Если status_code равен 200, функция
# возвращает True, иначе False.

import website_alive.make_request


def check_url(string):
    """Prepares a string to call make_request.get_status"""
    if string[:7] != "http://" and string[:8] != "https://":
        print("Wrong URL. Maybe you meant ""http://{}?".format(string))
        string = "http://" + string
        print("Checking {}...".format(string))
    result = website_alive.make_request.get_status(string)
    if result and result.status_code == 200:
        return True
    return False
