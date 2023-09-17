def make_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(4))  # 8
print(triple(4))  # 12


def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5, 6]
#squares = map(square, numbers)
squares = map(lambda x: int(x)*x, numbers)
print(list(squares))  # [1, 4, 9, 16, 25, 36]


def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # [2, 4, 6]

""" Задача 47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
Пример ввода и вывода:
Ввод: values = [1, 23, 42, 'asdfg'] 
transformed_values = list(map(trasformation, values)) 
if values == transformed_values:    
    print('ok') else:    
    print('fail') 
Вывод: ok"""

values = [1, 23, 42, 'asdfg']
transformation = lambda x:x
transormed_values = list(map(transformation, values))
if values == transormed_values:    
    print('ok') 
else:    
    print('fail')

""" Задача №49. Решение в группах Планеты вращаются вокруг звезд по эллиптическим орбитам. 
Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь. 
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, 
по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, 
зато искусственные спутники были запущены на круговые орбиты. Результатом функции должен быть кортеж, 
содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса. 
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения. 
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую  площадь. 
Гарантируется, что самая далекая планета ровно одна
Пример ввода:
Ввод: orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)] 
print(*find_farthest_orbit(orbits))
Вывод: 2.5 10 """

from math import pi
def find_farthest_orbit(list_of_orbits):
    filter_orbit = list(filter(lambda x: x[0]!=x[1], list_of_orbits))
    square_orbit = list(map(lambda x: pi*x[0]*x[1], filter_orbit))
    orbit_dict = dict(zip(square_orbit,filter_orbit))
    max_orbit = max(orbit_dict.keys())
    return orbit_dict.get(max_orbit)

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
print(max(orbits, key= lambda x: x[0]*x[1]*(x[0]!=x[1])))

""" Задача №51. Решение в группах Напишите функцию same_by(characteristic, objects), которая проверяет, 
все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, 
функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику. 
Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values): 
    print('same') 
else: 
    print('different')
          
Вывод: same   """

""" def same_by(x,list):
    return

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values): 
    print('same') 
else: 
    print('different') """

""" Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа. 
Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
 пример - 8 11 0 -23 140 1 вывод - 11 -23"""

lst = list(map(int,input("Введите список целых чисел в одну строчку через пробел: ").split()))
print(lst)
filtered_lst = list(filter(lambda x: 9<abs(x)<100 and x>0, lst))
print(filtered_lst, end=" ")
#len(str(abs(int(x))))==2

