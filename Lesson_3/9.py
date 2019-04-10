# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
import pprint
K = 5
pp = pprint.PrettyPrinter(indent=K)
a = []
for i in range(K):
    b = []
    for j in range(K):
        b.append(random.randrange(K))
    a.append(b)

pp.pprint(a)
max = 0
for i in range(K):
    min = K
    for j in range(K):
        if a[j][i] < min:
            min = a[j][i]
    if min > max:
        max = min
print(max)