# Программа принимает действительное положительное число x и целое
# отрицательное число y. Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    try:
        x = int(x)
    except ValueError:
        print("The first value is not a number")
        return
    try:
        y = int(y)
    except ValueError:
        print("The second value is not a number")
        return
    if y > 0:
        y = -y
    return print(round((x ** y), 3))

my_func(input(), input())




