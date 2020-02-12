"""Homework 5 Task 1"""


def digital(inp):
    """Checks if <input> is int or float"""
    if isinstance(inp, (int, float)):
        return True
    if isinstance(inp, str):
        if inp.isdigit():
            return True
        try:
            float(inp)
            return True
        except ValueError:
            return False
    return False


def complex_input():
    """Scans a complex number from string: <real><space><imaginary>"""
    print("Enter complex number: <real> <imaginary>")
    string = input()
    comp = MyComplex(int(string[:string.find(" ")]), int(string[string.find(" ") + 1:]))
    return comp


class MyComplex:
    """Custom realization of complex numbers"""
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], MyComplex):  # конструктор копирования
            self.real = args[0].real
            self.imaginary = args[0].imaginary
        elif len(args) == 1 and digital(args[0]):  # конструктор преобразования типа
            self.real = args[0]
            self.imaginary = 0
        elif len(args) == 2 and digital(args[0]) and digital(args[1]):  # конструктор инициализации
            self.real = args[0]
            self.imaginary = args[1]
        else:  # конструктор по умолчанию
            self.real = 0
            self.imaginary = 0

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return self.real != other.real or self.imaginary != other.imaginary

    def __round__(self, digits):
        self.real = self.real.round(digits)
        self.imaginary = self.imaginary.round(digits)

    def __str__(self):
        if self.imaginary >= 0.00:
            return "{0:.2f}+{1:.2f}i".format(self.real, self.imaginary)
        return "{0:.2f}{1:.2f}i".format(self.real, self.imaginary)

    def __add__(self, other):
        tmp = MyComplex(other)
        tmp.real += self.real
        tmp.imaginary += self.imaginary
        return tmp

    def __sub__(self, other):
        tmp = MyComplex(self)
        tmp.real -= other.real
        tmp.imaginary -= other.imaginary
        return tmp

    def __mul__(self, other):
        coef_real = self.real * other.real - self.imaginary * other.imaginary
        coef_img = self.real * other.imaginary + self.imaginary * other.real
        return MyComplex(coef_real, coef_img)

    def __truediv__(self, other):
        coef_real = ((self.real * other.real + self.imaginary * other.imaginary)
                     / (other.real ** 2 + other.imaginary ** 2))
        coef_img = ((self.imaginary * other.real - self.real * other.imaginary)
                    / (other.real ** 2 + other.imaginary ** 2))
        return MyComplex(coef_real, coef_img)

    def __pow__(self, power):
        try:
            if isinstance(power, int) and power > 1:
                tmp = MyComplex(self)
                for i in range(1, power+1):
                    tmp = tmp * self
                    return tmp
            elif power == 0:
                return 1
            else:
                return "Power is not integer"
        except ValueError:
            return "Wrong power value"

    def __iadd__(self, other):
        self.__add__(other)

    def __isub__(self, other):
        self.__sub__(other)

    def __imul__(self, other):
        self.__mul__(other)

    def __itruediv__(self, other):
        self.__truediv__(other)

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5


A = complex_input()
B = complex_input()
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(MyComplex(abs(A)))
print(MyComplex(abs(B)))
