# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

print('Введите начальное количество пробегаемых километров: ')
a = int(input())
print('Введите желаемое количество пробегаемых километров: ')
b = int(input())
i = 1
while a < b:
    a = a * 1.1
    i = i + 1

print('Необходимое количество дней для достижения цели: ', i)
