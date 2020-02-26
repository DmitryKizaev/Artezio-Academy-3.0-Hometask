"""Homework 8 Task 3"""

# Напишите функцию, которая получает два аргумента
# 1)путь к файлу изображения jpeg на компьютере (строка);
# 2)имя целевого файла (строка)
# отправляет файл HTTP POST запросом на https://postman-echo.com/post
# В ответе будет получен файл изображения jpeg, в виде octet-stream, который нужно раскодировать и
# сохранить на компьютере под целевым именем, переданным в аргументе.
# Функция должна вернуть размер сохраненного файла.


import requests
URL = "https://postman-echo.com/post"
PATH = "F:\Github\Artezio-Academy-3.0-Hometask\Hometask8\send.jpg"
TARGET_NAME = "target.jpg"

# не понимаю почему картинка на выходе получается битая
# и как правильно декодировать файл
# пытался выдергивать куски из files - не помогает
# (посмотреть можно в task3_dump)


def send_jpeg(path, target_name):
    """Get image by POST"""
    name = path[path.rfind("\\")+1:]
    image = open(path, "rb")  # rb - чтение с начала в двоич. формате
    print("name:", name)
    files = {name: image}
    try:
        response = requests.post(URL, files=files)
        image.close()
        if not response or response.status_code != 200:
            print("No response!")

        got = open(target_name, 'wb')  # wb - запись с начала в двоич. формате
        got.write(response.content)
        return got.name
    except requests.ConnectionError as err:
        print(err)
        print("URL incorrect!")
        return None


print("got:", send_jpeg(PATH, TARGET_NAME))
