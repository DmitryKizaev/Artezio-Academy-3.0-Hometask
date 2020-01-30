# Написать функцию, которая печатает
# квадраты всех нечетных чисел
# в произвольном интервале [0, Х],
# а так же количество таких чисел.


def squareprint(t):
    if t.isdigit():
        t = int(t)
        for i in range(1, t+1, 2):
            print("({})^2 = {}".format(i, i*i))
        print('total number: ', (t+1) // 2)
    else:
        print(t, ' is not a number!')
    return


print(Enter number:)
x = input()
squareprint(x)
