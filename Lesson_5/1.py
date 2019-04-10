"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections
import random

corps = collections.defaultdict(dict)
averages = []
# блок добавления тестовых данных
##################################
names = ['Yandex', 'Google', 'Rambler', 'Mail']
for name in names:
    temp = 0
    for quarter in range(1, 5):
        corps[name][quarter] = random.randint(0, 100)
        temp += corps[name][quarter]
    averages.append(temp/len(corps[name]))
##################################
# окончание блока доавбления тестовых данных

while True:
    name = input('Введите название компании(exit-для выхода): ')
    if name == 'exit':
        break
    temp = 0
    for quarter in range(1, 5):
        money = int(input(f'Введите прибыль за {quarter} квартал: '))
        corps[name][quarter] = money
        temp += money
    averages.append(temp)

average = sum(averages)/len(averages)
print('Средний доход')

for name, money in corps.items():
    print('\nКомпания:', name)
    for key in money:
        print(key, ':', money[key])
    avr = sum(money.values())/len(money)
    print('В сумме:', sum(money.values()))
    print('В среднем:', avr)
    if avr >= average:
        print('Доход выше среднего')
    else:
        print('Доход ниже среднего')
# print()
