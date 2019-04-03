# 4.	Определить, какое число в массиве встречается чаще всего.
import random
K = 10
a = []
b = []
for i in range(K):
    a.append(random.randrange(K))
    b.append([0])


for i in a:
    b[i][0] += 1
max = 0
max_i = 0
print(a)
print(b)
for i, val in enumerate(b):
    if val[0] > max:
        max = val[0]
        max_i = i
print(f' Число {max_i} встречается {max} раз')
