# Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_f (a, b):
    try:
        a = int(a)
    except ValueError:
        print("The first value is not a number")
    try:
        b = int(b)
    except ValueError:
        print("The second value is not a number")
    try:
        return a // b
    except (TypeError, ZeroDivisionError) as err:
        print("Operation is impossible")
        print(err)

print(my_f(input('Enter first number: '), input('Enter second number: ')))