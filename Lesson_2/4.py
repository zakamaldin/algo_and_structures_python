"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def count(base, num):
    if num == 0:
        return base
    else:
        print(base)
        return base + count(base / (-2), num - 1)


num = int(input('Введите натуральное число:'))
print(count(1, num))
