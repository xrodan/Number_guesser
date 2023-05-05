from random import *
rm = randint(1, 100)
print('Добро пожаловать в числовую угадайку!')

def is_valid(number):
    return number.isdigit() and 1 <= int(number) <= 100

def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def proverka():
    count = 0
    while True:
        n = is_valid_num()
        if n < rm:
            print('Ваше число меньше загаданного, попробуйте еще разок!')
            count += 1
        elif n > rm:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
        else:
            print('Вы угадали, поздравляем!' + '    ' + 'Спасибо, что играли в числовую угадайку. Еще увидимся...')
            print(f'Количество затраченных попыток: {count}')
            break

proverka()
