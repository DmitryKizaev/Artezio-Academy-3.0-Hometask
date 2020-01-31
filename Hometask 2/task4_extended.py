# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def myrange(*args):
    if len(args) == 1:
        return myrange_defaults(*args)
    elif len(args) == 2:
        return myrange_defaults(args[1], args[0])
    elif len(args) == 3:
        return myrange_defaults(args[1], args[0], args[2])
    else:
        return "Wrong number of arguments"


def myrange_defaults(stop, start=0, step=1):
    l = []
    i = start
    if stop > start and step > 0:
        while i < stop:
            l.append(i)
            i += step
    elif stop < start and step < 0:
        while i > stop:
            l.append(i)
            i += step
    return l


print("Example")
print("myrange gives", myrange(7))
print("range gives   [0, 1, 2, 3, 4, 5, 6] \n")
print("myrange gives", myrange(1, 8))
print("range gives   [1, 2, 3, 4, 5, 6, 7] \n")
print("myrange gives", myrange(0, 20, 5))
print("range gives   [0, 5, 10, 15] \n")
print("myrange gives", myrange(0, -7, -1))
print("range gives   [0, -1, -2, -3, -4, -5, -6] \n")
print("myrange gives", myrange(1, 0))
print("range gives   [] \n")

print("Сustom Example")
print("Enter a,b,c to emulate range (a, b, c)")
print("Enter a")
a = int(input())
print("Enter b")
b = int(input())
print("Enter c")
c = int(input())

print("range (a, b, c)")
print(myrange(a, b, c))
print("range (a, b)")
print(myrange(a, b))
print("range (b)")
print(myrange(b))
