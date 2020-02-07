"""Hometask 4"""

# 6. В корневой директории ("Lesson 4") создайте файл main.py,
# который при запуске спрашивает у пользователя адрес сайта, который
# необходимо проверить. Дальше делает проверку, используя пакет website_alive,
# и пишет, доступен ли сайт.

from website_alive import check_response

import website_alive
print("Enter URL to check:")
string = input()
if website_alive.check_response.check_url(string):
    print("Success! Website available.")
else:
    print("Error! Website unreachable.")
