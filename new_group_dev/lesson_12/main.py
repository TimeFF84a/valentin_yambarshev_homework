"""Исключения (exceptions) - ещё один тип данных в python.
Исключения необходимы для того, чтобы сообщать программисту об ошибках."""

# try:  # блок try обрабатывает выражение, где мы ожидаем увидеть ошибку
#     formula = 1 / 0
# except Exception:  # указываем исключение (Exception), которое необходимо обработать
#     formula = 0
#     print(formula)

# mydict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = mydict['d']
# except Exception:
#     print('Такого ключа нет')


"""Может быть несколько исключений, но отработает тот который (которая указана в try)"""
# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[6]
# except Exception:
#     print('Элемента с данным индексом нет')
# except KeyError:
#     print('Такого ключа нет')

# mydict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = mydict['d']
# except (IndexError, KeyError):
#     print('Произошла ошибка IndexError или KeyError')

# mydict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = mydict['d']
# except KeyError:
#     print('Вызвано исключение KeyError')
# finally:  # оператор finally всегда выполниться
#     print('finally')

# mydict = {"a": 1, "b": 2, "c": 3}
# try:
#     value = mydict['a']
# except KeyError:
#     print('Вызвано исключение KeyError')
# else:
#     print('Ошибки нет')
# finally:
#     print('Программа завершена')
