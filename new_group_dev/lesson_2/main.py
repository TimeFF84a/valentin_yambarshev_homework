# num1 = 5
# str_num1 = str(num1)
# print(str_num1)
# print(type(str_num1))  # type- проверка, какой тип данный
import random

# Базовые операции со строками

# str1 = '4'
# str2 = '5'
# print(str1 + str2)
# str3 = 'Hello'
# print(str3 * 7)  # Увеличивает количество слов Hello
# str5 = ' '
# print(len(str5))  # Узнаем количество символов, длину строки

'''Срезы'''

# string = 'Hello world'
# print(string[0])
# print(string[-1])
# print(string[6], string[6])
#
# print(string[0:4])  # 0- с какого символа, 4- до какого, не включая 4 символ
# print(string[:4])  # Можно и так, начинается с первого символа
# print(string[1:])  # Можно и так, заканчивается последним символом
#
# print(string[::2])  # Третий шаг указывает ШАГ
# print(string[::-1])  # Перевернутая строка просто

# string = 'Hello my name is'

# print(string[6:13])
# print(string[::-1])
# print(string[2:4])
# print(string[0:5], string[-2:])

# Разделение строки

string = 'hello my name is'
# Разделяет строку на список (делает список из строки)
string_split = string.split(' ')  # разделяет строку по символу, который присутствует в строке(тут пробел)
# string_split = string.split()  # если пустой, то тоже делит по пробелу
print(type(string_split))
#
# Объединение строки из списка в строку (делает строку из списка)
string_join = ','.join(string_split)  # через запятую определяем
print(string_join)
#
# Замена элементов строки
#
# new_string = string.replace('hello', 'hi')  # Заменяет старый символ на новый
# print(new_string)
# a = 'hello'
# print(a.isalpha()) # это буквы?
#
# Количество определенного элемента строки count
#
# print(new_string.count('m'))  # если дано число, то надо переводить в строку и там искать
# print(new_string.upper())  # перевод в верхний регистр
# print(new_string.lower())  # перевод в нижний регистр
# print(new_string.swapcase())  # буквы верхнего регистра в нижний и наоборот
# print(new_string.title())  # каждая первая буква каждого слова ставиться в верхнем регистре
# print(new_string.capitalize())  # преобразует первую букву в верхний регистр

"""Работа в конце урока"""

# user_name = input('Введите Ваше имя: ')
# print('Привет,', user_name)
# print(user_name * 3)

# num_random = random.randint(0, 999)
# str_num_random = str(num_random)
# print('Случайное трехзначное число: ', str(num_random))
# x = str_num_random[0]
# y = str_num_random[1]
# z = str_num_random[2]
# sum = int(x) + int(y) + int(z)
# print('Сумма случайного числа:', sum)


# s = input('Введите строку: ')
# print(s[::3])
# print(s[0] + s[-1])
# print(s.upper())
# print(s[::-1])
# print(s.isdigit())
#
# s1 = 'My name'
# s1_split = s1.split()
# print(s1_split)
# s1_join = ' '.join(s1_split[::-1])
# print(s1_join)