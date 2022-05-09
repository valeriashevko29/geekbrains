# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
#
def my_func(a, b, c):
    list1 = [a, b, c]
    list1.remove(min(list1))
    return print(f'The summary of the two biggest numbers is: {sum(list1)}')

my_func(int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: ')))




