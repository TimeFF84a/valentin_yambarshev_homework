#  6*. Заполнить список степенями числа 2 (от 2^1 до 2^n) (не самим создать такой список,
#  а сделать так, чтобы ваша программа сгенерировала сама такой список.
#  Посказка: прочитать про генератор списков)

num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
num3 = int(input("Введите число, которое является основанием степени: "))
list1 = [i for i in range(num1, num2)]
newList = [num3 ** i for i in list1]
print(f"Список чисел, которые являются степенями числа {num3}:")
print(list1)
print(f"Список чисел, которые получились:")
print(newList)