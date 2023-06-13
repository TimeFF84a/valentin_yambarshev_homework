import random
# sum_of_num = 0
# for i in "12345":
#     if int(i) % 2 != 0:
#         sum_of_num += int(i)
# print(sum_of_num)

# Коллекционные типы данных (коллекции) - упорядоченный изменяемый порядок различных элементов, разных типов
#  list-список, tupl-кортеж, set/frozenset-множество/неизменяемое множество, dict-словарь
#  str-строка

# Создание списка
# split - из строки через split
# list1 = []
# list2 = list() функция преобразования
# list3 = [i for i in range(10)] генератор списков

# list1 = [1, 2, 3]
# print(list1[-1])
# list_of_rnd_nums = [random.randint(1, 100) for i in range(10)]
# print(list_of_rnd_nums)

 # вот это то же самое что и это

# list2 = []
# for i in range(10):
#      list2.append(random.randint(1, 100))
# print(list2)

# Добавление элемента в конец списка "append"
list1 = [1, 2, 3, 'cat']
list1.append(5)
# print(list1)

# Добавление элемента на указанную позицию "insert"
list1.insert(2, 6)  # на 2-ую позицию, цифру 6
print(list1)

# Изменение элемента списка

list1[-2] = 7   # на индекс -2 мы присваиваем цифру 7
# print(list1)

# Удаление элемента из списка
# по его названию "remove"
# list1.remove(1)
# print(list1)
# метод "pop" удаляет и возвращает элемент удаленный по индексу
# x = list1.pop(0)
# print(x)
# print(list1)
# по индексу
# del list1[1]
# print(list1)

"""Расширение списка "extend" не создает новое, а просто расширяет, кроме того если добавлять слово,
то слово разобьет на символы"""
list2 = [1, 2, 3]
list3 = list1 + list2  # операция "+" создает новый объект
print(list3)

# list1.extend(list2)
# print(list1)

# Копирование списка "copy"
# copy_list = list1.copy()
# print(copy_list)

# Очистить список "clear" убираются все элементы
# copy_list.clear()
# print(copy_list)

# Определение количества элемента списка "count"
# print(list1.count(5))

# Определение индекса определенного элемента "index"
# print(list1.index[7])  # до первого вхождения

# Изменение порядка элементов в списке на противоположный "reverse"
# list1.reverse()
# print(list1)

# count, index, pop - возвращают элемент

# Сортировка элементов в списке
# list1.sort()  # сортировка в порядке возрастание
# print(list1)

# list1.sort(reverse=True)  # сортировка в порядке убывания
# print(list1)

# Вложенные списки
# list6 = [1, 2, 3]
# list7 = [4, 5, 6]
# list6.append(list7)
# print(list6)
# print(list6[-1][1])

# Можем использовать срезы в списках

# print(list6[1:3:2])