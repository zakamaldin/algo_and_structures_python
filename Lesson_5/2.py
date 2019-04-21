"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
import collections
numbers = collections.defaultdict(list)
ten_to_hex = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

for i in range(2):
    numbers[i] = list(input('Введите число в шестнадцатеричном формате: ').upper())

first = numbers[0]
second = numbers[1]

hex_sum = []
hex_mult = []
if len(first) > len(second):
    first, second = second, first
first.reverse()
second.reverse()
k = 0
for i in range(len(first)):
    current = ten_to_hex.index(first[i]) + ten_to_hex.index(second[i]) + k
    hex_sum.append(ten_to_hex[current % 16])
    if ten_to_hex.index(first[i]) + ten_to_hex.index(second[i]) >= 15:
        k = 1
    else:
        k = 0
if len(first) != len(second):
    current = ten_to_hex.index(second[-1]) + k
    hex_sum.append(ten_to_hex[current % 16])
hex_sum.reverse()
print('Сумма:', hex_sum)

