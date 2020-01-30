# Написать свою имплементацию функции range() из Python 2.x
# (аналогично Python 3, только возвращает список).


def myrange(start, stop, step):
    if step == 0:
        return 'ValueError'
    l = []
    i = start
    while i < stop:
        l.append(i)
        i += step
    return l


print("Example")
print("Enter a,b,c to emulate range (a, b, c)")
print("Enter a")
a = int(input())
print("Enter b")
b = int(input())
print("Enter c")
c = int(input())
print(myrange(a, b, c))
