"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

def without_er(n):
    primes = []
    for i in range(2, n+1):
        for k in range(2, i):
            if i % k == 0:
                break
        else:
            primes.append(i)
    return primes


def with_er(n):
    a = list(range(n + 1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1

# Но как по мне алгоритмы мало отличаются, с решетом Эратосфена, 2 функция, взял из стаьи хабра, а 1 сам писал
n = int(input("Введите количество: "))
print(without_er(n))
print(with_er(n))
