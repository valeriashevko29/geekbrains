# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. ####
# # Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

import itertools

user_num = int(input('Введите число. Верну последовательность до 10: '))
s = itertools.count(user_num)
for el in s:
    print(el)
    user_num += 1
    if user_num > 10:
        break
    exit = input('Для продолжения - Enter. Для выхода - q')
    if exit == 'q':
        break


list1 = input('Введите список, разделитель - запятая: ').split(', ')
cycler = itertools.cycle(list1)
counter = 0
for i in cycler:
    print(i)
    counter += 1
    if counter == len(list1):
        break
    exit = input('Для продолжения - Enter. Для выхода - q')
    if exit == 'q':
        break

# после разбора д/з - оптимизация:

my_count = itertools.count(int(input('Enter a number and I will return a sequence: ')))
my_cycle = itertools.cycle(input('Enter a list, separated by comma:').split(', '))

for f in range(10):
    print(f'(my_count, my_cycle - {next(my_count)}, {next(my_cycle)}')

# range и next автоматически делают break. Next вытягиваеет по одному элементу и не позволит циклу стать бесконечным, т.к. range



