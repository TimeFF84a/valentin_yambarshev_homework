#  Цикл While

# i = 0
# while i < 10:
#     # print(i)  # выведит числа от 0 до 9
#     # i += 1
#     i += 1
#     print(i)  # выведит числа от 1 до 10

"""Задачи"""

# 1 Вывести сумму чисел от 1 до 50

# i = 1
# result = 0
# while i <= 50:
#     result += i
#     i += 1
# print(result)

# 2 Вводим число с клавиатуры и если число 20, то мы что - нибудь с ним делаем

# num1 = 20
# while True:
#     num2 = int(input("Введите любое целое число: "))
#     if num1 == num2:
#         print("Вы угадали число")
#         break
#     elif num1 < num2:
#         print(f"Введенное число {num2} больше {num1}")
#     else:
#         print(f"Введенное число {num2} меньше {num1}")

# 3 Вывести на экран квадраты всех чисел от 1 до 10

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# 4 Перемножить все четные значения в диапозоне от 0 до 125

# i = 0
# res = 1
# while i <= 125:
#     i += 1
#     if i % 2 == 0:
#         res *= i
# print(res)

# 5 Вывести числа от 1 до 15 в порядке убывания

# num1 = 15
# while num1 > 0:
#     print(num1)
#     num1 -= 1

# 6 Пользователь вводит два числа с клавиатуры, необходимо вывести на экран все отрицательные числа, лежащие в этом
# диапозоне. Например пользователь ввел -5 и 3, на экране вывелось -4, -3, -2, -1

# num1 = int(input("Введите первое любое отрицательное число: "))
# num2 = int(input("Введите второе любое число, которое больше первого: "))
# while num1 < num2:
#     num1 += 1
#     if num1 == 0:
#         break
#     print(num1)

# 7 Необходимо чтобы программа выводила на экран вот такую последовательность (не использовать готовый список):
# 7 14 21 28 35 42 49 56 63 70 77 84 91 98. Добавить в список и найти его длину

# i = 7
# list1 = []
# while i < 105:
#     list1.append(i)
#     i += 7
# print(f"Необходимый список:\n{list1}")
# print(f"Длина списка:\n{len(list1)}")

# 8 Простейший калькулятор с введенными двумя числами вещественного типа.
# Ввод с клавиатуры следующих операций: "-", "+", "*", "/". И двух чисел
# Обработать ошибку: "Деление на ноль". Ноль использовать в качестве завершения программы, сделать как отдельную операцию

while True:
    num1 = float(input("Введите первое любое вещественное число: "))
    num2 = float(input("Введите второе любое вещественное число: "))
    operation = input("Введите операцию -, +, *, /: ")
    if operation == "/" and num2 == 0:
        print("Деление на ноль")
        break
    elif operation == "-":
        print(f"{num1 - num2}")
    elif operation == "+":
        print(f"{num1 + num2}")
    elif operation == "*":
        print(f"{num1 * num2}")
    elif operation == "/":
        print(f"{num1 / num2}")
    else:
        print("Такой операции не существует")


