#  Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
#  Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
#  Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
#  В случае неудачи вывести на экран правильную комбинацию.

import random

randomNum = str(random.randint(1, 10))  # рандомное целое число, которое переводится в строчку
color = random.randint(1, 2)  # рандомное целое число для цвета
attempt = 1  # попытка

if color == 1:  # если 1-то присваивается красный цвет, если 2-черный
    color = "красный"
else:
    color = "черный"

randomNumColor = f"{randomNum} {color}"  # переменная которая будет сравниваться с вводимыми данными
# print(randomNumColor)  # для проверки комбинации
while attempt <= 5:
    num1 = input("Введите любое целое число от 1 до 10: ")
    str1 = input("Введите 'красный' или 'черный': ")
    numStr = f"{num1} {str1}"  # присваиваем введенные данные для проверки в дальнейшем
    print(f"Вы ввели: {numStr}")  # строчка не обязательна, но мне так нравится))
    attempt += 1  # увеличивается попытка на единицу

    if numStr == randomNumColor:  # условие, если мы угадали, то выходим из цикла
        print("Вы угадали правильную комбинацию")
        break
    elif attempt > 5:  # если попыток > 5, то выводим выигрышную комбинацию
        print(f"Вы израсходовали все попытки.\nВот правильная комбинация: {randomNumColor}")
    else:
        print(f"Вы не угадали.\nСейчас будет {attempt} попытка из 5")





