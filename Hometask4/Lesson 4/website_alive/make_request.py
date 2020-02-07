"""Hometask 4"""

# 4. Внутри модуля make_request напишите функцию, которая делает запрос
# на сайт с использованием библиотеки requests, и возвращает объект
# (найдите документацию по библиотеке, вам будет достаточно раздела QuickStart)


import requests

from urllib3.exceptions import MaxRetryError, NewConnectionError
from _socket import gaierror


def get_status(url):
    """Tries to get an object from address s using requests"""
    try:
        obj = requests.get(url)
    except requests.ConnectionError:
        print("URL incorrect!")
        obj = None
    return obj
