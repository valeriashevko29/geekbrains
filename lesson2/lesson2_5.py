# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
# не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
# существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
# должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.

my_list = [7, 5, 3, 3, 2]
user_num = ''

while user_num != 'q':
    user_num = input('Введите число.\nЧтобы выйти из программы, введите "q".')
    i = 0
    if user_num.isdigit():
        for n in my_list:
            if int(user_num) <= n:
                i = i + 1
            else:
                break
        my_list.insert(i, user_num)
    print(my_list)



