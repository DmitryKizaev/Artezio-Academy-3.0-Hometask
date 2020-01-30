# 3. Написать функцию вычисления факториала числа

def factorial (x):
    if x.isdigit():
        x = int(x)
        fac = 1
        for i in range (2, x+1):
           fac = fac * i
        return fac
    else:
        return ('NaN')

print('Enter number:')
t = input ()
print (factorial (t))