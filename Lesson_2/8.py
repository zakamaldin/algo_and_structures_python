"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
num = input('Введите последовательность чисел через пробел:')
k = input('Введите цифру котрое будем искать:')
count = 0
for i in num:
    if i == k:
        count += 1
print('В данной последовательности таких цифр: ', count)
