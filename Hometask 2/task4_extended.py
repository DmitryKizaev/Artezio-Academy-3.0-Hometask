# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def myrange(*args):
    if len(args) == 1:
        return myrange_defaults(*args)
    elif len(args) == 2:
        return myrange_defaults(args[1], args[0])
    else:
        return myrange_defaults(args[1], args[0], args[2])


def myrange_defaults(stop, start=0, step=1):
    if step == 0:
        return 'Value Error'
    l = []
    i = start
    if stop > start:
        while i < stop:
            l.append(i)
            i += step
    else:
        while i > stop:
            l.append(i)
            i -= step
    return l


print("Example")
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
