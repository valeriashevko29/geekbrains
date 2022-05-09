# 6. Реализовать функцию int_func(), принимающую слова из
# маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
# пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
# исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
# написанную ранее функцию int_func().

def int_func(*args):
    args = input('Введите строку в нижнем регистре, латиница: ').split()
    for word in args:
        char = 0
        for letter in word:
            if 97 <= ord(letter) <= 122:
                char += 1
        # здесь в принт выводится цифра, если она есть в тексте
        # print(word.capitalize(), end= ' ') if len(word) == char else print(word, end=' ')
        # здесь, как по заданию
        print(word.capitalize(), end= ' ') if len(word) == char else print('\nSmall English letters only!')


int_func()



# Решение с ascii (сохранила для себя)

# int_func = lambda word: word.title() if word.islower() and ascii(word)[1:-1].isalpha() else ''
# print(' _ '.join(map(int_func, input('Enter a phrase: '). split())))