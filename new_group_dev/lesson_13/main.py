import csv

"""CSV (comma-separated value) - это формат представления табличных данных
(например, это могут быть данные из таблицы или данные из БД).
В этом формате каждая строка файла - это строка таблицы."""
# with open('data.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')  #
#     writer.writerow(['user_name', 'user_password'])

data = [
    ['user_name', 'user_address'],
    ['user1', 'address1'],
    ['user2', 'address2'],
    ['user3', 'address3'],
]

"""Разница между writerow и writerows"""
"""writerow - надо проходиться циклом, чтобы записалось в строчки и столбики"""
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=';')
#     for user in data:
#         writer.writerow(user)

"""writerows - цикл не нужен"""
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)
