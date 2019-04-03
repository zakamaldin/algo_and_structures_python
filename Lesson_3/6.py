"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
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
   if val >= max:
       max_i = i
       max = val
   if val <= min:
       min_i = i
       min = val
sum = 0
if min_i is not max_i:
    if min_i < max_i:
        for i in range(min_i+1, max_i):
            sum += a[i]
    elif min_i > max_i:
        for i in range(max_i+1, min_i):
            sum += a[i]


print(a)
print(min_i, max_i)
print(sum)