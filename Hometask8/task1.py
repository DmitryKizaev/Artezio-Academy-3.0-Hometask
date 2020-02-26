"""Homework 8 Task 1"""

# Напишите функцию, которая возвращает
# размер HTML документа по адресу https://google.com.
# Т.е. нужно получить страницу и вернуть ее размер (количество символов).

import requests  # единственный действительно необходимый импорт

# остальные импорты - для импровизации и самодеятельности:
import os  # запишем результат в файл и сможем пощупать его ручками
from re import search  # используем вторую часть урока (regexp)
import datetime  # и системное время для автогенерации имен файлов

from time import sleep
N_REQUESTS = 4  # размер документа нестабилен - возьмем N_REQUESTS запросов
REQUESTS_TIMEOUT = 2  # с интервалом REQUESTS_TIMEOUT секунд
URL_TO_GET = "https://google.com"  # по адресу URL_TO_GET


def url_to_filename(url):
    """Берет начало от URL и заменяет в нем некорректные символы"""
    url_name = url[:30]
    forbidden = r"([\W]+)"  # оставим в имени файла буквы, цифры и _

    try:
        found = search(forbidden, url_name).group()
        while found:
            url_name = url_name.replace(found, "_")
            found = search(forbidden, url_name).group()
    except AttributeError:
        pass
    now = datetime.datetime.now()
    return url_name+"_"+now.strftime("%d%m_%H_%M_%S")+".txt"


def get_html_size(url):
    """Basic task, impossible to check result"""
    try:
        obj = requests.get(url)
        if not (obj and obj.status_code == 200):
            print("URL unreachable!")
            return None
        return len(obj.text)

    except requests.ConnectionError:
        print("URL incorrect!")
        return None


def get_html_advanced(url, filename=None):
    """More opportunities and friendly interface of get_html_size"""
    try:
        obj = requests.get(url)
        if not (obj and obj.status_code == 200):
            print("URL unreachable!")
            return None
        if not filename:
            filename = url_to_filename(url)
        html_file = open(filename, "w")
        html_file.write(obj.text)

        html_file = open(filename, "r")
        symbols = 0
        lines = 0

        for line in html_file:
            lines += 1
            symbols += len(line)
        symbols = symbols - lines + 1
        # удаляем все символы конца строки кроме последнего - eof

        html_file.close()
        return [filename, symbols]

    except requests.ConnectionError:
        print("URL incorrect!")
        return None


# БАЗОВАЯ ЧАСТЬ
print("URL = ", URL_TO_GET, "\n")
print("Function get_html_size:")
print(get_html_size(URL_TO_GET), "\n")

# РАСШИРЕННАЯ ЧАСТЬ
print("Function get_html_advanced: {} requests with {}sec timeout"
      .format(N_REQUESTS, REQUESTS_TIMEOUT))
files_created = {}

for i in range(N_REQUESTS):
    got = get_html_advanced(URL_TO_GET)
    if got[0] in files_created.keys():
        print("HTML document", got[0], " updated")
    else:
        print("HTML document", got[0], " received")
    files_created[got[0]] = got[1]
    sleep(REQUESTS_TIMEOUT)

print()

for file_name in files_created:
    print("Filename: <{}> | symbols: {} | size: {} bytes"
          .format(file_name, files_created[file_name],
                  os.stat(file_name).st_size))

print("\nYou can now check number of symbols in received files manually")
print("Files can be found in project folder")

answer = None
while answer not in ("yes", "no"):
    print("Would you like to delete them now?")
    answer = input()
    if answer == "yes":
        for file_name in files_created:
            try:
                os.remove(file_name)
                print("File: <{}> deleted".format(file_name))
            except FileNotFoundError:
                print("Error: file {} is already deleted".format(file_name))
    else:
        print("Files will be kept in project folder")
