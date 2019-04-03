"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random
K = 10
a = []
for i in range(K):
    a.append(random.randrange(K))

def find_min(array):
    min = K
    min_i = 0
    for i, val in enumerate(array):
        if val < min:
            min = val
            min_i = i
    return min_i
print(a)
first = a.pop(find_min(a))
print(a)
second = a.pop(find_min(a))
print(a)
print(first, second)


