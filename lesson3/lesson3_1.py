# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_f (a, b):
    # a = int(input('Enter first number: '))
    # b = int(input('Enter second number: '))
    try:
        a = int(a)
    except ValueError as error2:
        print(error2)
    try:
        b = int(b)
    except ValueError as error3:
        print(error3)
    try:
        return a // b
    except (ZeroDivisionError, TypeError) as error1:
        print(error1)

print(my_f(input('Enter first number: '), input('Enter second number: ')))