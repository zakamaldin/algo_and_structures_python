#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random
K = 10
a = []
for i in range(K):
    a.append(random.randrange(K))

max_i = 0
min_i = 0
max = 0
min = K

for i, val in enumerate(a):
    if val > max:
        max_i = i
        max = val
    if val < min:
        min_i = i
        min = val
print(a)
a[min_i], a[max_i] = a[max_i], a[min_i]
print(a)
