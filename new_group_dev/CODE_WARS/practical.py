# № 1. Преобразовать число в перевернутый массив цифр
# num1 = 35231
# list1 = list(str(num1)[::-1])
# list2 = []
# for letter in list1:
#     if type(letter) is str:
#         list2.append(int(letter))
# print(list2)
# a = [int(letter) for letter in str(num1)[::-1]] #  это решение лучше
# print(a)

# № 2. Дан массив целых чисел.
# Возвращает массив, где первый элемент — это количество положительных чисел,
# а второй элемент — сумма отрицательных чисел. 0 не является ни положительным,
# ни отрицательным.
# Если вход представляет собой пустой массив или имеет значение null,
# верните пустой массив.

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# number_of_positive_digits = 0
# sum_of_negative_numbers = 0
# if list1:
#     for number in list1:
#         if number > 0:
#             number_of_positive_digits += 1
#         elif number <= 0:
#             sum_of_negative_numbers += number
#     print([number_of_positive_digits, sum_of_negative_numbers])
# else:
#     print([])

# № 3. Напишите функцию bmi, которая вычисляет индекс массы тела (bmi = вес / рост ** 2 ).
# если bmi <= 18,5, вернуть "Недостаточный вес"
# если bmi <= 25,0, вернуть «Нормальный»
# если bmi <= 30,0 вернуть "Избыточный вес"
# если bmi > 30, верните ("Ожирение").

# def bmi(weight, height):
#     if weight / height ** 2 <= 18.5:
#         return "Недостаточный вес"
#
#     elif 18.5 <= weight / height ** 2 <= 25.0:
#         return "Нормальный"
#
#     elif 25.0 <= weight / height ** 2 <= 30.0:
#         return "Избыточный вес"
#
#     elif weight / height ** 2 > 30.0:
#         return "Ожирение"
#
#
# print(bmi(50, 1.80))
#
#
# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
#
#
# print(bmi(50, 1.80))

# № 4. Вам будет предоставлен массив A и значение X. Все, что вам нужно сделать, это проверить,
# содержит ли предоставленный массив значение.
# Массив может содержать числа или строки. Х может быть любым.
# Возврат, true если массив содержит значение, false если нет.

# def check(seq, elem):
#     while True:
#         if elem in seq:
#             return True
#         else:
#             return False
#     pass
#
#
# print(check([66, 101], 66))


# № 5. Завершите решение так, чтобы оно перевернуло переданную в него строку.
# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

# def solution(string):
#     return string[::-1]
#     pass
# print(solution('world'))

# № 6. Нам нужна функция, которая может преобразовать число (целое число) в строку.
# Какие способы достижения этого вы знаете?
# Примеры (ввод --> вывод): 123  --> "123"

# def number_to_string(num):
#     return str(num)

# № 7. Рассмотрим массив/список овец, где некоторые овцы могут отсутствовать на своем месте.
# Нам нужна функция, которая подсчитывает количество овец, присутствующих в массиве (true означает наличие).

# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count
#     pass
# #   return sheep.count(True)
#
# print(count_sheeps(
#     [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True,
#      True, True, False, False, True, True]))

# № 8. Напишите функцию RemoveExclamationMarks, которая удаляет все восклицательные знаки из заданной строки.
# def remove_exclamation_marks(s):
#     s1 = s.replace('!', '')
#     print(s1)

# № 9. Напишите функцию для преобразования имени в инициалы.
# Это ката строго состоит из двух слов с одним пробелом между ними.
# На выходе должны быть две заглавные буквы с точкой, разделяющей их.
# Это должно выглядеть так: patrick feeney => P.F или Sam Harris => S.H

# def abbrevName(name):
#     first, last = name.upper().split(' ')
#     return first[0] + '.' + last[0]
# print(abbrevName("patrick feeney"))