"""Homework 5 Task 2"""

import time

MAX_TRIES_EXAM = 2  # допустимое число сдач экзамена
MAX_TRIES_LAB = 5  # допустимое число сдач каждой работы
CONF_BASIC = {
    "exam_max": 30.0,  # количество баллов, доступное за сдачу экзамена
    "lab_max": 7.0,  # количество баллов за выполнение 1 практической работы
    "lab_num": 10,  # количество практических работ в курсе
    "k": 0.61,  # доля баллов, которую необходимо набрать для сертификата
}


class Student:
    """Описывает поведение студента при прохождении курса"""

    def __init__(self, name, course=None):
        """Конструктор"""
        self.name = name  # Имя студента
        self.points = {}  # Словарь учета баллов за лабораторные
        self.points_exam = 0  # Балл за экзамен
        self.tries = {}  # Учет числа попыток сдачи лабораторных
        self.tries_exam = 0  # Учет числа попыток сдачи экзамена
        self.gooses = 0

        if course:  # Ручной ввод параметров курса
            self.course = course
            self.course_check()
        else:  # Если ручной не задан - подставим базовое значение
            self.course = CONF_BASIC

    def __str__(self):
        """Строковый вывод"""
        return str({"Username": self.name, "Lab results": self.points,
                    "Lab tries": self.tries, "Exam results": self.points_exam,
                    "Exam tries": self.tries_exam})

    def course_check(self):
        """При пользовательском вводе курса проверяет правильность"""
        if not self.course.get("exam_max"):
            print("Exam marks error!")
            return False
        if not self.course.get("lab_max"):
            print("Practice marks error!")
            return False
        lab_num_correct = self.course.get("lab_num")
        if not lab_num_correct:
            print("Number of tasks error!")
            return False
        if not isinstance(lab_num_correct, int) or lab_num_correct < 1:
            print("Number of tasks format error!")
            return False
        k_correct = self.course.get("k")
        if not k_correct:
            print("Percentage for diploma incorrect!")
            return False
        if not 0 < k_correct < 1:
            print("Percentage for diploma should be 0 <= k <= 1!")
            return False
        return True

    def points_earned(self):
        """Возвращает число играющих роль баллов, суммируя из словаря"""
        earned = self.points_exam
        for i in self.points:
            if 0 <= i < self.course["lab_num"]:  # В списке м.б. и доп. задания
                earned += self.points[i]  # их мы сохраняем, но не считаем
            else:
                print("<Lab {} is additional, {} points for it are not"
                      " counted>".format(i, self.points[i]))
        return earned

    def points_max(self):
        """Считает максимальное число баллов данного курса"""
        return (self.course["exam_max"] + self.course["lab_num"]
                * self.course["lab_max"])

    def points_needed(self):
        """Считает min достаточное число баллов для сдачи данного курса"""
        return self.points_max() * self.course["k"]

    def make_lab(self, m, n=None):
        """Считывает баллы за лабу, проверяет на сбои системы"""
        if n is None:
            for i in range(len(self.points)):
                if self.points.get(i, -1) == -1:
                    n = i  # Если не указан номер лабы берем первую несделанную
                    print("Warning: lab number is None,"
                          " working with first lab undone:", n)

        if not self.tries.get(n):
            self.tries[n] = 0
        elif self.tries[n] == MAX_TRIES_LAB:
            print("Unable to pass the lab one more time \n")
            return self  # Не получится сдать лабу если число попыток исчерпано

        if self.points.get(n):
            print("Lab {} overwritten successfully".format(n))

        self.points[n] = m

        # Проверки на сбои в системе баллов
        if self.points[n] > self.course["lab_max"]:

            print("Error fixed: <lab {}>: points {} out of {}"
                  " - converted to {} \n"
                  .format(n, self.points[n], self.course["lab_max"],
                          self.course["lab_max"]))

            self.points[n] = self.course["lab_max"]

        elif self.points[n] < 0:

            print("Error fixed: <lab {}>: points {} out of {}"
                  " - converted to 0 \n"
                  .format(n, self.points[n], self.course["lab_max"]))
            self.points[n] = 0

        self.tries[n] += 1
        return self

    def make_exam(self, m):
        """Считывает баллы за экзамен, проверяет на сбои системы"""
        if self.tries_exam == MAX_TRIES_EXAM:
            print("Unable to pass the exam one more time")
            return self

        if self.tries_exam:
            print("Exam will be overwritten")

        self.points_exam = m
        if self.points_exam < 0:

            print("Error fixed: <exam> points {} out of {}"
                  " - converted to 0 \n"
                  .format(self.points_exam, self.course["exam_max"]))

            self.points_exam = 0
        elif self.points_exam > self.course["exam_max"]:

            print("Error fixed: <exam> points {} out of {}"
                  " - converted to {} \n"
                  .format(self.points_exam, self.course["exam_max"],
                          self.course["exam_max"]))
            self.points_exam = self.course["exam_max"]

        self.tries_exam += 1
        return self

    def is_certified(self):
        """Проверяет достаточно ли баллов для диплома"""
        count_earned = self.points_earned()
        # чтобы выполнить функцию всего 1 раз
        tmp = (count_earned, count_earned >= self.points_needed())
        return tmp
        # почему return не работает если писать без tmp через tuple(...)?
        # выдает ошибку на логическом выражении "unexpected argument"


# дальше пойдет немного необязательной отсебятины
# было интересно разобраться с поддержкой нескольких студентов

num_users = 1  # число хранимых системой студентов в данный момент
# 1 - потому что добавил admin чтобы не регаться каждый раз заново при тестах

users = [Student("admin")]
# список экземпляров класса Student (для динамического создания)

user_names = {"admin": 0}
# словарь сопоставления имени студента с номером его экземпляра класса в списке

current_user = None  # идентификатор пользователя для интерфейса (по имени)


def user_sign_in():
    """Войти как существующий студент"""
    global num_users
    global user_names

    print('\n----- SIGN IN FORM -----')
    print("Enter student's name:")
    username = input()
    exists = user_names.get(username)
    if exists is None:  # имени нет в базе
        print("User not found. Start registration process? (yes/no)")
        create = 0
        while create not in ("yes", "no"):
            create = input()
        if create == "yes":
            user_register()
        else:
            print("Process aborted\n")
            raise UserWarning
    else:  # имя существует
        return username


def user_register():
    """Задать параметры для включения студента в базу"""
    global num_users
    global user_names

    print('\n----- USER REGISTRATION -----')
    conf_course = 0
    while conf_course not in ("basic", "custom"):
        print('Enter course: "basic" or "custom"')
        conf_course = input()

    if conf_course == "basic":
        course = CONF_BASIC
    else:
        print("Enter: exam_max ⮠  lab_max ⮠  lab_num ⮠  k ⮠ ")
        course = {"exam_max": float(input()), "lab_max": float(input()),
                  "lab_num": int(input()), "k": float(input())}

    print("Enter student's name:")
    username = input()
    exists = user_names.get(username)
    if not exists:  # имени нет в базе
        user_names[username] = num_users
        num_users += 1
        users.append(Student(username, course))
    else:  # имя существует
        print("User {} already exists, overwrite? (yes/no)")
        overwrite = 0
        while overwrite not in ("yes", "no"):
            overwrite = input()

        if overwrite == "yes":
            user_names[username] = exists
            users[exists] = Student(username, course)
        else:
            print("Process aborted")


def goose():
    """Запускает гуся"""
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░ЗАПУСКАЕМ░В░ARTEZIO░░░░░░░░")
    print("░░░░░░░░░▄▀▀▀▄░░░░░░░░░░░░░░░░░░░")
    print("░░░▄███▀░◐░░░▌░░░░ГУСЯ░░░░░░░░░░")
    print("░░░░░░░▌░░░░░▐░░░░CТАЖЁРА░░░░░░░░")
    print("░░░░░░░▐░░░░░▐░░░░░░░░░░░░░░░░░░░")
    print("░░░░░░░▌░░░░░▐▄▄░░░░░░░░░░░░░░░░░")
    print("░░░░░░░▌░░░░▄▀▒▒▀▀▀▀▄░░░░░░░░░░░░")
    print("░░░░░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄░░░░░░░░░")
    print("░░░░░░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄░░░░░░")
    print("░░░░░░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄░░░░")
    print("░░░░░░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄░░")
    print("░░░ПО░░░░░░░░░░░▌▌░▌▌░░░░░░░░░░░░")
    print("░░░░░░░PYTHON░░░▌▌░▌▌░░░3.8░░░░░░")
    print("░░░░░░░░░░░░░░▄▄▌▌▄▌▌░░░░░░░░░░░░")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n")
    if current_user is not None:
        users[user_names[current_user]].gooses += 1


def user_interface():
    """Обеспечивает работу с функционалом через консоль"""
    global current_user

    while not current_user:
        while not num_users:
            print("No accounts available. Register please! \n")
            user_register()
            return False

        print("[{}] users available:".format(num_users))
        for i in user_names:
            print(i)

        print("1 -> I have an account")
        print("2 -> Create new account")

        todo = 0
        while todo not in ('1', '2'):
            todo = input()
        if todo == '1':
            try:
                current_user = user_sign_in()
                print("\nWelcome [{}]".format(current_user))
            except UserWarning:
                return False
        else:
            user_register()

    print("1 -> Hand in a lab <make_lab method>")
    print("2 -> Pass the exam <make_exam method>")
    print("3 -> Get a certificate <is_certified method>")
    print("4 -> User statistics")
    print("5 -> Current course info")
    print("6 -> Switch user")
    print("7 -> LAUNCH A GOOSE")
    print("8 -> Quit")

    todo = 0

    while todo not in range(1, 9):
        todo = int(input())
    if todo == 1:
        print("Enter m (lab_max is {})"
              .format(users[user_names[current_user]].course["lab_max"]))
        try:
            m = float(input())
            print("Enter n (lab_num is {})"
                  .format(users[user_names[current_user]].course["lab_num"]))
        except ValueError:
            print("Invalid m\n")
            return False
        try:
            n = int(input())
            users[user_names[current_user]].make_lab(m, n)
        except ValueError:
            print("Invalid n\n")
            return False
        return False

    if todo == 2:
        print("Enter m (exam_max is {})"
              .format(users[user_names[current_user]].course["exam_max"]))
        try:
            m = float(input())
            users[user_names[current_user]].make_exam(m)
        except ValueError:
            print("Invalid m\n")
        return False

    if todo == 3:
        print(users[user_names[current_user]].is_certified(), "\n")
        return False

    if todo == 4:
        print("Account:")
        print(users[user_names[current_user]])
        print("Points earned:")
        print(users[user_names[current_user]].points_earned())
        print("Gooses launched:")
        print(users[user_names[current_user]].gooses, "\n")
        return False

    if todo == 5:
        print(users[user_names[current_user]].course)
        print("To pass: {} points out of {}\n"
              .format(users[user_names[current_user]].points_needed(),
                      users[user_names[current_user]].points_max()))
        return False

    if todo == 6:
        current_user = None
        return False

    if todo == 7:
        goose()
        if users[user_names[current_user]].gooses == 5:
            print("OH NO! YOU HAVE JUST STARTED A GOOSE ATTACK")
            for i in reversed(range(1, 6)):
                print(i, "seconds to hide")
                time.sleep(2)
            while True:
                goose()
        return False

    if todo == 8:
        return True


print("loading... [████████████] 99 % \n")
while not user_interface():
    pass
