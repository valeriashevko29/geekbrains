from functools import reduce
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

list1 = [i for i in range(100, 1001) if i % 2 == 0]
res = reduce(lambda x, y: x * y, list1)
print(res)

# после разбора д/з...

list2 = [a for a in range(100, 1001, 2)]
res1 = reduce(lambda x, y: x * y, list1)
print(res1)





