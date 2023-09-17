""" Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res. """

n = int(input('Entere 3-digits number \n'))

res = n // 100  + n % 100 // 10 + n % 10

print(f'sum is {res}')