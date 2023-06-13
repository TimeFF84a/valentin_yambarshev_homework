# print(5 == 5)
# print(5 > 5)
# print(5 >= 5)
# print(5 < 5)
# print(5 <= 5)
# print(5 != 5)  # не равно

# Условный оператор

"""
if условие:
    код(действие)
elif условие:
    код(действие)
else:
    код(действие)"""

# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# if x > y:
#     print(f'число {x} больше чем {y}')
# elif x < y:
#     print(f'число {x} меньше чем {y}')
# else:
#     print(f'число {x} равно {y}')
#
# x = int(input('Введите x: '))
# y = int(input('Введите y: '))

# Операторы and, or, not

# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# if x > y and x > 5:
#     print('and')
# elif x > y or x > 5:
#     print('or')
# else:
#     print('Hello')

# num1 = int(input('Введите первое целое число: '))
# num2 = int(input('Введите второе целое число: '))
# num3 = int(input('Введите третье целое число: '))
#
# if num1 > num2 and num1 > num3:
#     print(f"{num1} наибольшее число")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} наибольшее число")
# elif num2 > num3:
#     print(f"{num3} наибольшее число")
# else:
#     print('Непонятно что да как)))')

# num1 = int(input('Введите число: '))
# if num1 > 100 or num1 < -100:
#     print("-")
# else:
#     print("+")

# num1 = int(input('Введите первое число: '))
# operation = input('Введите операцию: ')
# num2 = int(input('Введите второе число: '))
# if operation == "+":
#     print(num1 + num2)
# elif operation == "-":
#     print(num1 - num2)
# elif operation == "*":
#     print(num1 * num2)
# elif operation == "/":
#     print(num1 / num2)
# else:
#     print('Операция не соответствует заявленной')

# string = 'Кошка сказала "мяу"'
# print(f"{string}")

# num1 = int(input('Введите первое целое число: '))
# num2 = int(input('Введите второе целое число: '))
# if num1 % 10 == 0 or num2 % 10 == 0:
#     print('Какое - то из чисел заканчивается на 0')
# else:
#     print('Никакое из чисел не заканчивается на 0')

# num1 = int(input('Введите первое целое число: '))
# num2 = int(input('Введите второе целое число: '))
# result = num1 > num2
#
# if result:
#     print(f"{num1} больше чем {num2}")
# else:
#     print('Неравенство не верно')

# print('abc' * 2, 'abc' * 2.0, 'abc' * -2)
# print(1_000_000)  # можно так писать большие числа

# str1 = 'a'
# str2 = 'A'
# print(str1 >= str2)
# print(ord('a'))
# print(ord('A'))