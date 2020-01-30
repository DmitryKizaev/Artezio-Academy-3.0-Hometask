# 2. Написать функцию, которая принимает 3 числа (a,b,c)
# и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’

# "между" в моем решении подразумевается не включая границы a и b

def divisibility(a, b, c):
    if c == 0:
        return 'division by 0'
    else:
        num = 0
        for i in range(a, b):
            if i % c == 0:
                num += 1
               # print ('Number found:', i, 'total:', num)
        return num

print('Enter a:')
a = int (input())
print('Enter b:')
b = int (input())
print('Enter c:')
c = int (input())
print (divisibility(a, b, c))



