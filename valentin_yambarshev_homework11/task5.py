#  3. В текстовом файле посчитать количество строк,
#  а также для каждой отдельной строки определить количество в ней символов.

with open("task2.txt", "r") as file:
    text = file.readlines()  # выводится в списке
    print(text)
kol_str = 0
dict1 = {}
# Перебираем каждый элемент (файла) в цикле
for i in text:
    # i = i[:-1]  # избавляемся от последнего элемента \n- переноса строки. Тут переприсваивать нет смысла
    kol_str += 1
    dict1 = {i[:-1]: len(i[:-1]) for i in text}  # генератор словаря
print(f"Количество строк в файле 'task2.txt': {kol_str}")
print(f"Длина каждого элемента:\n{dict1}")

# Вопрос еще один, почему если в 11 строке мы перепресваиваем i, то это i не работает в словаре?
# Единственное что меня не устраивает, что в словаре цифры в ключе становятся строками! Это критично Артем?
# Просто я тогда не представляю как вообще это сделать)))) Ну представляю, сортировать в список, переводить в число,
# потом как-то добавить в общий список, а как потом внести это все в словарь....ума не приложу))