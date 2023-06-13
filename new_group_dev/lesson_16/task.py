# 1) Написать функцию, которая определяет количество разрядов введенного целого числа.
#
#
#
# def func(n):
#     i = 0
#     while n > 0:
#         n = n // 10
#         i += 1
#     return i
#
#
# num1 = int(input('Введите любое целое число: '))
# print(f'Количество разрядов: {func(num1)}')
import math

# 2) В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.
# print('# 2')
#
#
# def function(figure):
#     if figure == 'круг':
#         def area_of_circle(r):
#             s = math.pi * (r ** 2)
#             return s
#
#         radius = int(input('Введите радиус: '))
#         print(area_of_circle(radius))
#     elif figure == 'прямоугольник':
#         def area_of_rectangle(side_a, side_b):
#             s = side_a * side_b
#             return s
#
#         a = int(input('Введите первую сторону прямоугольника: '))
#         b = int(input('Введите вторую сторону прямоугольника: '))
#         print(area_of_rectangle(a, b))
#     elif figure == 'треугольник':
#         def area_of_triangle(side_x, height):
#             s = side_x * height * 0.5
#             return s
#
#         x = int(input('Введите сторону треугольника: '))
#         h = int(input('Введите высоту треугольника: '))
#         print(area_of_triangle(x, h))
#
#
# figure = input('Введите "круг", "прямоугольник" или "треугольник": ')
# function(figure)

# 3) Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами в диапазоне,
# указанном пользователем с клавиатуры.
# Функция должна принимать два аргумента – начало диапазона и его конец, при этом ничего не возвращать.
# print('# 3')
# def func_range(start, end):
#     list1 = [i for i in range(start, end)]
#     print(list1)
# start = int(input('Введите начало диапозона: '))
# end = int(input('Введите конец диапозона: '))
# func_range(start, end)

# 4) Написать функцию и сделать так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
# print('# 4')
# def time(sec):
#     day = sec // 86400
#     clock = sec // 3600
#     min = sec // 60
#     second = sec % 60
#     print(f'{day}:{clock}:{min}:{second}')
#
# sec = int(input('Введите секунды: '))
# time(sec)

# 5) Написать функцию, которая считает сколько гласных и согласных в строке. Строку вводить с клавиатуры.
# 6) Функцию которая при заданном целом числе n посчитает n + nn + nnn.
