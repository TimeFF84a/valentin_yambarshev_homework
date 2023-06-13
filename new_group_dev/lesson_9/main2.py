# numbers = {i: i**2 for i in range(10)}
# print(numbers)
# print(f"\nКлючи")
# for key in numbers.keys():
#     print(key)
#
# print(f"\nЗначения")
# for value in numbers.values():
#     print(value)
#
# print(f"\nКлюч:Значения")
# for key, value in numbers.items():
#     print(f"{key}: {value}")
#
# print(f"\nКлюч:Значения. Другим способом")
# for key in numbers:
#     print(f"{key}: {numbers[key]}")
#


# 1) Создайте словарь person, в котором будут присутствовать ключи name, age, city.
# Выведите значение возраста из словаря person.

# person = {"name": "Valentin", "age": 20, "city": "Minsk"}
# print(person["age"])

# 2) Создайте словарь с ключами BMW, AUDI и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

car = {"BMW": ["M3", "M5", "M6"], "AUDI": ["A100", "A80", "A50"]}
for key in car:
    print(f"Первая модель {key}: {car[key][0]}. Последняя модель {key}: {car[key][-1]}")







