"""Замыкание функций"""

# def mult(x):
#     def power(y):
#         return x * y
#
#     return power
#
# print(mult(2)(5))

"""Lambda функция"""
# x = lambda a, b: a * b
# print(x(2, 3))

"""Генераторы"""
# def generator(n):
#     for i in range(n):
#         yield i  # ключевое слово для вывода генератора, вместо return
#
# element = generator(5)
# print(next(element))
# for i in generator(5):
#     print(i)

"""Декораторы - функция, которая позволяет расширить другую функцию каким-нибудь функционалом"""


# def decorator(func):
#     def wrapper():
#         print('start function')
#         func()
#         print('stop function')
#
#     return wrapper
#
#
# @decorator
# def test_func1():
#     print('Test text 1')
#
#
# test_func1()
#
#
# @decorator
# def test_func2():
#     print('Test text 2')
#
#
# test_func2()
# test_wrapped_1 = decorator(test_func1())
# test_wrapped_2 = decorator(test_func2())
# test_wrapped_1()
# test_wrapped_1()

"""Рекурсивная функция"""

# def factorial_number(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial_number(n - 1)
#
#
# print(factorial_number(4))

"""Функция enumerate"""
# list1 = [1, 2, 3, 4, 5]
# for i in enumerate(list1):
#     print(i)






















































