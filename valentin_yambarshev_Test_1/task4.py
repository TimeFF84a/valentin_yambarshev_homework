#  4. Даны два целых числа m и n (m≤n).
#  Напишите программу, которая выводит все числа от m до n включительно.

m = int(input("Введите первое целое число: "))
n = int(input("Введите второе целое число, которое больше числа 'm': "))
for digit in range(m, n + 1):
    if n >= m:
        print(digit)
