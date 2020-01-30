# Написать программу, которая принимает от пользователя имя и пароль.
# Сравнивает пароль с заданным в коде.
# В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
# Если пароль не совпадает, то печатает в консоль
# "Password for user: <Имя пользователя> is incorrect"
# "Please try again..."
# И снова запрашивает пароль (не завершается).

passw = "QWERTY123"
inp_p = 0
print("Enter username")
inp_u = input()

while True:
    print("Enter password")
    inp_p = input()
    if inp_p == passw:
        break
    else:
        print("Password for user: {} is incorrect".format(inp_u))
        print("Please try again...\n")

print("Password for user: {} is correct".format(inp_u))
