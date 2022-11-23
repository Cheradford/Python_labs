import random

count = 0


def word_generate():
    global count
    strin = ''
    for i in range(count):
        strin += chr(random.randint(ord('А'), ord('Я')))
    return strin


def isPolindrom(str):
    length = len(str)
    for i in range(int(length / 2)):
        if str[i] != str[length - i - 1]:
            return False

    return True


def main_loop():
    global count
    count = int(input('Введите количество букв в слове>'))
    strings = []
    print('Созданный текст:')
    for i in range(0, 100):
        str = word_generate()
        strings.append(str)
        print(str, end=',')
        if i%10 == 0: print()
    print('\nПолиндромы')
    for i in strings:
        if (isPolindrom(i)): print(i, end=',')


main_loop()
