#  1. Создать произвольный словарь.
#  a) Добавить новый элемент с ключом типа str и значением типа int;
#  b) Добавить новый элемент с ключом типа кортеж(tuple) и значением типа список(list);
#  c) Получить элемент по ключу;
#  d) Удалить элемент по ключу;
#  i) Получить список ключей словаря;

dict1 = {"cat": "Myrka", "dog": "Jack", 1: 45, "bird": 56, "London": "capital"}
dict1["str"] = 123
print(f"Добавили новый элемент с ключом типа str и значением типа int: \n{dict1}")
dict1[("q", "w", "e")] = [1, 2]
print(f"Добавили новый элемент с ключом типа кортеж(tuple) и значением типа список(list): \n{dict1}")
print(f"Получить элемент по ключу: \n{dict1['cat']}")
print(f"Удалили элемент по ключу: \n{dict1.pop('dog')}")
print(f"Получили список ключей словаря: \n{dict1.keys()}")

