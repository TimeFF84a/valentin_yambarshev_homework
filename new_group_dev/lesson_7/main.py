# Кортеж - неизменяемый тип данных
# Создание кортежа
tuple1 = (1, 2, 3, 4, 5)
# У кортежа только два метода
# tuple.index()
# tuple.count()
list1 = [1, 2, 3, 4, 5]
print(tuple1.__sizeof__())
print(list1.__sizeof__())

print(tuple1[:4])
print(tuple1[1])
new_tuple = tuple(list1)  # перевод списка в кортеж

# numbers = (1, 2, 3, 4, [6, 7, 8, 9]) # можно изменять внутри кортежа список
# list2 = numbers[-1]
# list2[0] = 4
# print(numbers)

numbers = (1, 2, 3, 4, 6, 7, 8, 9)
print(max(numbers))
print(min(numbers))