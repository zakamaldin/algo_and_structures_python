#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random
K = 100
a = []
for i in range(K):
    a.append(random.randint(-K, K))
min = K
min_i = 0
for i, val in enumerate(a):
    if val < min:
        min = val
        min_i = i
print(min_i, min)