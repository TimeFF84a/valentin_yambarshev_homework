#  1) Даны два кортежа. Требуется объединить их между собой.
import random

# print("Задача № 1")
# tuple1 = (1, 2, 3, 4)
# tuple2 = (5, 6, 7, 8)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# 2) В кортеже целых чисел найдите максимальный и минимальный элементы,
# а также осуществите их обмен.

# print("Задача № 2")
# tuple1 = (1, 2, 3, 4)
# tuple2 = (5, 6, 7, 8)
# maxTuple1 = max(tuple1)
# minTuple2 = min(tuple2)
# print(maxTuple1)
# print(minTuple2)
# maxTuple1, minTuple2 = minTuple2, maxTuple1
# print(maxTuple1)
# print(minTuple2)

# 3) В список, сгенерированный случайным образом, добавить введенный пользователем элемент.

# print("Задача № 3")
# list1 = [random.randint(1, 100) for i in range(10)]
# print(list1)
# num1 = int(input("Введите целое число: "))
# list1.append(num1)
# print(list1)

# 4) В список, сгенерированный случайным образом, добавить введенный пользователем элемент на указанную позицию.

# print("Задача № 4")
#
# list1 = [random.randint(1, 100) for i in range(10)]
# print(list1)
# num1 = int(input("Введите целое число: "))
# list1.insert(0, num1)
# print(list1)

# 5) Имеются два списка, сгенерированные случайным образом.
# Добавьте в конец первого списка все элементы второго списка.

# print("Задача № 5")

# list1 = [random.randint(1, 100) for i in range(10)]
# list2 = [random.randint(1, 100) for i in range(10)]
# print(list1)
# print(list2)
# list1.extend(list2)
# print(list1)

# 6) Из заранее сформированного списка следует удалить элемент, введенный пользователем.

# print("Задача № 6")
# list1 = [random.randint(1, 100) for i in range(10)]
# list2 = [random.randint(1, 100) for i in range(10)]
# list1.extend(list2)
# print(list1)
# num1 = int(input("Введите целое число, которое необходимо удалить: "))
# list1.remove(num1)
# print(list1)

# 7) Из исходного списка следует удалить элемент, позицию которого указал пользователь.

# print("Задача № 7")
# list1 = [random.randint(1, 100) for i in range(10)]
# print(list1)
# num1 = int(input("Введите номер позиции, для удаления необходимого элемента: "))
# list1.pop(num1)
# print(list1)

# 8) В кортеже целых чисел вычислите произведение отрицательных элементов, имеющих нечетные индексы.

# print("Задача № 8")
# prod_of_num = 1
# tuple1 = tuple([random.randint(-10, 10) for i in range(10)])
# print(tuple1)
# for i in tuple1:
#     if i < 0 and tuple1.index(i) % 2 != 0:
#         prod_of_num *= i
# print(prod_of_num)

# 9) Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно.
# Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж.
# С помощью метода кортежа count() определите в нем количество нулей.
# Выведите на экран третий кортеж и количество нулей в нем.

# print("Задача № 9")
#
# tuple1 = tuple([random.randint(0, 5) for i in range(10)])
# tuple2 = tuple([random.randint(-5, 0) for i in range(10)])
# print(f"Первый кортеж:\n{tuple1}")
# print(f"Второй кортеж:\n{tuple2}")
# tuple3 = tuple1 + tuple2
# print(f"Получившийся кортеж при сложении двух:\n{tuple3}")
# count_zero = tuple3.count(0)
# print(f"Количество нулей в третьем кортеже:\n{count_zero}")

# 10) Вывести данные кортежа без скобок, через запятую. Обязательно: элементы кортежа – строки.

# print("Задача № 10")
#
# tuple1 = ("cat", "dog", "bird", "hand")
# print(tuple1)
# str_tuple1 = str(tuple1)
# print(str_tuple1.replace("(","").replace(")","")) # альтернативный вариант
# print(",".join(tuple1)) # этот вариант лучше

# 11) Сгенерируйте 2 кортежа случайными числами в диапазоне от 10-90.
# Количество элементов в кортеже 10.
# Определить: 1) Сумма элементов какого из кортежей больше и вывести соответствующее сообщение на экран
# (Сумма больше в кортеже - ..) 2) Вывести на экран порядковые номера минимальных элементов этих кортежей

# print("Задача № 11")
#
# tuple1 = tuple([random.randint(10, 90) for i in range(10)])
# tuple2 = tuple([random.randint(10, 90) for i in range(10)])
# print(f"Первый кортеж:\n{tuple1}")
# print(f"Второй кортеж:\n{tuple2}")
# sum_tuple1 = sum(tuple1)
# sum_tuple2 = sum(tuple2)
# if sum_tuple1 > sum_tuple2:
#     print(f"Сумма больше в кортеже:\n{tuple1}")
# elif sum_tuple1 < sum_tuple2:
#     print(f"Сумма больше в кортеже:\n{tuple2}")
# else:
#     print("Кортежи равны")
# min_elem_tuple1 = min(tuple1)
# min_elem_tuple2 = min(tuple2)
# print("Порядковый номер минимального элемента:", tuple1.index(min_elem_tuple1))
# print("Порядковый номер минимального элемента:", tuple2.index(min_elem_tuple2))
