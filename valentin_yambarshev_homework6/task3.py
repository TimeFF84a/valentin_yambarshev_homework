#  3. Даны несколько списков: [-8, 1, 2, -2, 0], [1, -1, 0, -9, 4, -5], [1, 4, 0, 23, 6, 34]. 1- '-2', 2- '-5', 3- '1'
#  Для каждого из списков найти второе наименьшее значение в нем (правильные ответы выделены жирным шрифтом).

list1 = [-8, 1, 2, -2, 0]
list2 = [1, -1, 0, -9, 4, -5]
list3 = [1, 4, 0, 23, 6, 34]
list1.sort()
print(f"Bторое наименьшее значение первого списка: {list1[1]}")
list2.sort()
print(f"Bторое наименьшее значение второго списка: {list2[1]}")
list3.sort()
print(f"Bторое наименьшее значение третьего списка: {list3[1]}")