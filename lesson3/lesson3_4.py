# Программа принимает действительное положительное число x и целое
# отрицательное число y. Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

# def my_func(x, y):
#     try:
#         x = int(x)
#     except ValueError:
#         print("The first value is not a number")
#         return
#     try:
#         y = int(y)
#     except ValueError:
#         print("The second value is not a number")
#         return
#     if y > 0:
#         y = -y
#     return print(round((x ** y), 3))
#
# my_func(input(), input())


#//////////// 2 вариант (здесь не предусмотрены обязательные условия задачи) ////////////

# def my_func(x, y):
#     res = 1
#     for i in range(abs(y)):
#         if y > 0:
#             res = res * x
#         elif y < 0:
#             res = round((res / x), 6)
#         else:
#             res = x
#     return res
#
# print(my_func(3, -8))


#             //////////// 3 вариант - после просмотра разбора д/з////////////

def my_func(x, y):
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return print('Вы ввели НЕ число')
    if x <= 0 or y >= 0:
        return print('Ошибка.\nЗначение х должно быть больше нуля.\nЗначение y должно быть меньше нуля.')
    else:
        res = 1
        for i in range(abs(y)):
            res = res / x
    return print(f'Результат возведения числа {x} в степень {y}: {round((res), 7)}')

num1 = input('Введите целое положительное число х: ')
num2 = input('Введите целое отрицательное число y: ')
my_func(num1, num2)

