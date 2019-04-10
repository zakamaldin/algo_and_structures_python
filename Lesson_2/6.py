"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

import random

answer = random.randint(0, 100)
print(answer)


def game(attempt):
    if attempt == 0:
        print('Не угадал!!! Ответ:', answer)
        exit('GAME OVER')
    choise = int(input('Введите вашу догадку: '))
    print(choise)
    if choise == answer:
        exit('Угадал!')
    elif choise < answer:
        print('Больше!')
    elif choise > answer:
        print('Меньше!')
    game(attempt-1)

game(9)
