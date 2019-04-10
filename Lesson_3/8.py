"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
import pprint
K = 5
pp = pprint.PrettyPrinter(indent=K)
a = []
for i in range(K):
    b = []
    for j in range(K):
        if j != K-1:
            b.append(int(input('Введите значение:')))
        else:
            b.append(sum(b))
    a.append(b)
pp.pprint(a)