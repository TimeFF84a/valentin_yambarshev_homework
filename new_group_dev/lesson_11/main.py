file = open("text.txt", "r")

"""1 способ взаимодействия с файлом"""
# print(file)
# print(*file)  # позволяет вывести содержимое файла
# file.close()  # закрытие файла, чтобы не грузить систему

"""2 способ взаимодействия с файлом"""  # в данном способе не надо закрывать файл, все происходит автоматически
# with open("text.txt", "r") as file:  # если не использовать режим, то автоматом будет режим чтение "r"
#     # print(file.read())  # указывает какое количество символов вывести, если пустые скобки, то выведет все
#     # print(file.readline())
#     lines = file.readlines()  # выводит строчку полностью
#     print(lines[1])  # выводит переменную и мы можем указать в индексе, какую строчку вывести

"""Запись в файл"""
# with open("text.txt", "a") as file:  # дозаписывает, "w" перезаписывает
#     file.write("World Hello")  # перезаписывает содержимое файла
#
# with open(r"D:\python\project\new_group_dev\lesson_2\data1.txt") as file:
#     print(file.read())

# with open('text.txt', 'r') as file:
#     text = file.readlines()
# wer = 0
# for i in text:
#     wer += len(i.split())
#     print(i)
# print(wer)
