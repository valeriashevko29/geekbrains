# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().
user_list = list(input('Enter numbers with a space:').split())
for el in range(1, len(user_list), 2):
    user_list[el - 1], user_list[el] = user_list[el], user_list[el - 1]
print(user_list)

