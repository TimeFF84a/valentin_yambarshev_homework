import fileinput
import os

# os.rename('text.txt', 'new_text.txt')  # переименование файла

# print(f'Текущая директория {os.getcwd()}')

# os.mkdir('folder')  # создание папки
# file = open('folder/data.txt', 'w')  # в папке folder создаем файл
# file.close()
# os.chdir('folder')  # переместиться в определенную папку
#
# print(f"Текущая директория {os.getcwd()}")  # переместились в папку folder
# file = open('data2.txt', 'w')  # создали файл в этой папке
# file.close()  # закрыли файл
#
# os.chdir('..')  # вышли из папки folder
# print(f"Текущая директория {os.getcwd()}")

"""Удаление файлов - remove"""
# os.remove('folder/data2.txt')
"""Удаление папки - для начала необходимо удалить все файлы"""
# os.rmdir('folder')
"""Создание папок в папке"""
# os.makedirs('folder1/folder2')
"""удаление вложенных папок"""
os.removedirs('folder1/folder2')

