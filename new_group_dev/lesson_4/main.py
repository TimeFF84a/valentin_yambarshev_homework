# list1 = []  # первый способ создания списка
# list2 = list()  # второй способ создания списка
# print(list2)  # покажет пустой список(квадратные скобки)
#
list3 = ['cat', 'dog', 'bird']
# print(list3)
# print(list3[1])
print(list3[-1])
# print(list3[0])
#
# list4 = list('cat')  # только один итерируемый объект
# print(list4)  # result ['c', 'a', 't']

# Добавления элемента в список append
list_words = ['cat', 'dog', 'bird']
# list_words.append('panda')  # в конец списка только один элемент
# print(list_words)

# Удаление элемента из списка remove
# list_words.remove('bird')
# print(list_words)

# Определить сколько раз встречается определенный элемент count
list_nums = [1, 2, 3, 4, 5, 6, 4, 6, 3, 3, 3, 7]
# count_num = list_nums.count(3)
# print(count_num)

# Определение индекса списка - index
index_cat = list_words.index('cat')
print(index_cat)

'''Только методы count, index, pop позволяют со списком
производить какие-то действия'''

# удаление элемента по индексу, а также возвращает удаленный элемент - pop
pop_num = list_nums.pop(4)
print(pop_num)
print(list_nums)





