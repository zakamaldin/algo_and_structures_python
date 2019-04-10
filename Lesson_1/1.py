# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = input('Введите трехзначное число: ')
if len(num) is not 3:
    print('Ошибка! Колчичество знаков отличается от необходимого')
    exit()
num = int(num)
hundreds = num // 100
tens = num // 10 % 10
units = num % 10
print('Сотни:', hundreds)
print('Десятки:', tens)
print('Единицы:', units)
print('Сумма цифр:', hundreds + tens + units)
print('Произведение цифр:', hundreds * tens * units)

