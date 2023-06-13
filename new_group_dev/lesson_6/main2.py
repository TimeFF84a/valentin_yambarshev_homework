#  1) Дан произвольный список. Представить его в обратном порядке
# print("# 1")
#
# listRandom = [i for i in range(10)]
# listRandom.reverse()
# print(listRandom)
import random

#  2) Дан список с числами и в нем есть цифра 20. Поменять 20 на 200.
# print("# 2")
#
# listRandom = [i for i in range(25)]
# xIndex = listRandom.index(20)
# listRandom[xIndex] = 200
# print(listRandom)

#  3) Список из 7 цифр. Если чётных цифр в нём больше,
#  то найти сумму всех цифр,
#  если нечётных больше, то найти произведение 1, 3 и 6 элемента.
print("# 3")

listRandom = [i for i in range(1, 8)]
chet = 0
nechet = 0
sum = 0
proizv = 0
for i in listRandom:
    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1
print(f"Количество четных элементов: {chet}")
print(f"Количество нечетных элементов: {nechet}")
if chet > nechet:
    for i in listRandom:
        sum += i
    print(f"Сумма четных элементов: {sum}")
else:
    proizv = listRandom[0] * listRandom[2] * listRandom[5]
print(f"Произведение нечетных элементов: {proizv}")






