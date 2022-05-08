# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
#
def my_func(a, b, c):
    list1 = [a, b, c]
    list1.remove(min(list1))
    list1 = sum(list1)
    return print(list1)

my_func(int(input()), int(input()), int(input()))




