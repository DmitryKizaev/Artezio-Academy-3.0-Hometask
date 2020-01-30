# Написать функцию, которая печатает
# квадраты всех нечетных чисел
# в произвольном интервале [0, Х],
# а так же количество таких чисел.

def squareprint(x):
    if x.isdigit():
        x = int (x)
        num = 0
        for i in range(1, x+1, 2):
            print("({})^2 = {}".format(i, i*i))
        print('total number: ', (x+1) // 2)
    else:
        print (x, ' is not a number!')
    return

print('Enter number:')
x = input()
squareprint (x)

