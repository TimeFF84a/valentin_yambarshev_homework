import random

# def first_function():  # вызов функции без параметров
#     print('Hello world')
#
#
# first_function()
#
#
# def second_function():
#     pass  # пустая функция

'''Создайте функцию sum_of_list и посчитайте сумму элементов самопроизвольного списка'''


# def sum_of_list():
#     list1 = [random.randint(1, 100) for i in range(10)]
#     sum1 = 0
#     for i in list1:
#         sum1 += i
#     print(f'Сумма чисел списка {list1}:\n{sum1}')
#
#
# sum_of_list()


"""Передача аргументов в функцию"""

# def func(num1, num2):
#     return num1 + num2  # оператор, который показывает что вернет функция в итоге
#
#
# x = int(input('Введите первое число'))
# y = int(input('Введите первое число'))
# print(func(x, y))


"""Явное наименование аргументов"""

# def func(num1, num2):  # num1 и num2 - параметры функции
#     return num1 + num2
#
#
# x = int(input('Введите первое число'))
# y = int(input('Введите второе число'))
# # print(func(num1=5, num2=10))
# result_of_func = func(x, y)  # x и y аргументы функции
# print(result_of_func)

"""Ключевые аргументы"""

# def func_1(x, y=3, c=5):
#     return x + y + c
#
#
# print(func_1(5))


"""args, kwargs"""
# def new_func(*args, **kwargs):  # kwargs - ключевые аргументы
#     print(args)
#     print(kwargs)
#
#
# new_func(1, 2, 3, 4, 5, 6, name='petya', second_name='petrov')
# (1, 2, 3, 4, 5, 6) - в виде кортежа выводит args
# {'name': 'petya', 'second_name': 'petrov'} - в виде словаря выводит kwargs

"""Области видимости"""

x = 4
def func1():
    global x  # делает x внутри функции глобальной и после переопределения x внутри функции на выходе становиться 2
    print(f'x равен {x}')
    x = 2
    print(f'Замена переменной глобальной X на {x}')


func1()
print(f'Глобальный {x}')

# def func2():
#     c = 3
#     return x + c

























































