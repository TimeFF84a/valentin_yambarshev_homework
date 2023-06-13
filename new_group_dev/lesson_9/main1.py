"""Словари как тип данных"""
"""Ключи могут быть только неизменяемые типы объектов, а значения - любые"""

"""СОЗДАНИЕ СЛОВАРЯ"""
# dict1 = {}  # ключи ("dict") должны быть уникальны, значения (:1) нет
# dict3 = dict(hello="world", short="dictionary")
# dict4 = dict([(1, 1), (2, 4)])
# dict5 = dict.fromkeys(["a", "b"], 100)  # одно значение ко всем - 100
# dict6 = dict.fromkeys(["a", "b"])  # будет значение - NONE
numbers_1 = dict(zip((1, 2, 3), ["1", "2", "3"]))  #  создает новый словарь, (1, 2, 3) - ключи, ["1", "2", "3"] - значения
print(numbers_1)
# print(dict1)
# print(dict3)
# print(dict4)
# print(dict5)
#
dict7 = {i: i**3 for i in range(10)}  # будет 10 пар (ключ:значение). i:-это ключ, i**3-это значение(в этом случае ключ возведенный в куб)
print(dict7)

"""ОБЪЕДИНЕНИЕ СЛОВАРЕЙ"""

print(f"\nСпособ № 1 через метод UPDATE")
dictionary_1 = {"a": 300, "b": 400}
dictionary_2 = {"c": 500, "d": 400}
dictionary_1.update(dictionary_2)
print(dictionary_1)

print(f"\nСпособ № 2 через оператор '**' ")
merged_dict1 = {**dictionary_1, **dictionary_1}
print(merged_dict1)

print(f"\nСпособ № 3 через оператор '|' ")
merged_dict2 = dictionary_1 | dictionary_1
print(merged_dict2)

"""ЗАМЕНА ЗНАЧЕНИЯ КЛЮЧА"""
dict8 = {1: 2, 2: 4, 3: 9}
# dict8[2] = 5  # меняем значение ключа
# print(dict8)

"""МЕТОДЫ СЛОВАРЯ"""
# dict9 = dict8.copy()  # копируем
# dict8.clear()  # очищаем полностью, остается пустой словарь
# print(dict8.keys())  # выводит ключи, но не как список (хотя и выглядит как список)
# print(dict8.values())  # выводит значения, но не как список (хотя и выглядит как список)
# print(dict8.items())  # возвращает пары "ключ: значение"
# print(dict8.get(0, "такого ключа нет"))  # позволяет вывести значение по ключу, если нет значения в ключе, то выведет что мы укажем или None
# print(dict8.pop(3))  # pop удаляет по ключу, но значение выведет, если мы захотим (но удаляет пару "ключ: значение")
dict8.update({"a": 2, "b": 3})  # обновляем словарь, другим словарем
print(dict8)
# del dict8["a"]  # оператор del также удаляет по ключу
# print(dict8)



