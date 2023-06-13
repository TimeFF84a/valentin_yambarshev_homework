"""МНОЖЕСТВА"""
# Множества - содержит только уникальные значения, неиндексируемые, выводиться в хаотичном порядке, поддерживает только
# неизменяемые типы данных

# set1 = {1, 2, 1, 2}  # создаются через {}
# print(set1)
# set12 = set()  # создание пустого множества
# numbers = {}  # создание пустого словаря

# words = {"cat", "dog", "numbers"}
# print(words)  # множества не сохраняет последовательность

"""МЕТОДЫ"""
"""Добавление элементов во множество"""
# numbers = {"dog", "cat", "lion", 1, 2, 3, 4, 5}
# numbers.add('6')  # не можем добавить списки и словари
# print(numbers)

"""Удаление по имени элементов: remove, discard"""
# numbers.remove(2)  # будет ошибка если элемента не существует
# numbers.discard(3) # не будет ошибки если элемента не существует

"""Удаление без параметра"""
# numbers.pop()  # в основном удаляет первый элемент
# print(numbers)

"""clear, copy"""
# x = numbers.copy()  # копирует
# numbers.clear()  # очищает
# print(numbers)

"""Объединение множеств: union, | - создает новое множество"""
# x = {1, 2, 3}
# y = {"1", "2", "3"}
# x1 = {7, 8, 9}
# c = x.union(y, x1)
# print(c)


"""Пересечение множеств: intersection. Выведет элементы, которые есть и в первом множестве и втором множестве"""
x = {"dog", "cat", "bird"}
y = {"dog", "cat", "lion"}
print(x.intersection(y))

"""Разница множеств: difference - оставляет уникальные значения в множестве, за исключением второго"""
set1 = {1, 2}
set2 = {2, 3}
print(set1.difference(set2))

"""Объединение множеств: update - расширяет"""
# set1.update("hello")
# print(set1)

"""issubset-Проверка, является ли множество подмножеством другого"""
num1 = {1, 2}
num2 = {2, 3}
print(num2.issubset(num1))  # выведит булевое значение

"""isdisjoint-Проверка есть ли пересечение между множествами
если пересечение есть: False, нет пересечения: True"""
print(num1.isdisjoint(num2))  # выведит булевое значение