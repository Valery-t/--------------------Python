""" Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res. """

n = int(input('Entere 3-digits number \n'))

res = n // 100  + n % 100 // 10 + n % 10

print(f'sum is {res}\n')

""" Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.

Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей. """

n = 6
Petya, Katya, Sergey = (n // 6, (n // 6 + n // 6) * 2, n // 6)
print(f"{Petya} {Katya} {Sergey}\n")

""" Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no. """

n = 385916
x1 = n // 100000
x2 = n % 100000 // 10000
x3 = n % 10000 // 1000
x4 = n % 1000 // 100
x5 = n % 100 // 10
x6 = n % 10
if x1 + x2 + x3 == x4 + x5 + x6:
    print("yes")
else:
    print("no")

""" Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно. """

a,b,c = 3, 2, 4

if c < a * b and (c % a == 0 or c % b == 0):
    print("yes")
else:
    print("no")