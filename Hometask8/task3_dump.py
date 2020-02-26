"""Homework 8 Task 3"""
# свалка для кода, призванного что-то исправить

import requests

URL = "https://postman-echo.com/post"
PATH = "F:\Github\Artezio-Academy-3.0-Hometask\Hometask8\send.jpg"
TARGET_NAME = "target.jpg"


def send_jpeg(path, target_name):
    """Get image by POST"""
    name = path[path.rfind("\\") + 1:]
    print(name)
    image = open(path, "rb")
    files = {"image": image}  # rb - чтение с начала в двоич. формате
    try:
        response = requests.post(URL, files=files)
        if not (response and response.status_code == 200):
            print("URL unreachable!")
            return None
        resp_text = response.text
        while True:
            try:
                resp_dict = eval(resp_text)
                break
            except NameError as errcode:
                # убираем все null, которые не дают создать словарь, в кавычки
                errcode = str(errcode)
                bad_start = errcode.find("\'") + 1
                bad_end = errcode.find("\'", bad_start)
                bad_word = errcode[bad_start:bad_end]
                resp_text = resp_text.replace(bad_word, "\"" + bad_word + "\"")

        print(resp_text)

        octet = resp_dict["files"][name]
        octet = octet[octet.find("base64") + 7:len(octet)]

        print(octet)

        with open("dump_"+target_name+".txt", 'wb') as text_file:
            # wb - запись с начала в двоич. формате
            text_file.write(bytes(octet, "UTF-8"))
        with open("dump_"+target_name, 'wb') as output_file:
            # wb - запись с начала в двоич. формате
            output_file.write(bytes(octet, "UTF-8"))
        return output_file.name
    except requests.ConnectionError:
        print("URL incorrect!")
        return None


print(send_jpeg(PATH, TARGET_NAME))
