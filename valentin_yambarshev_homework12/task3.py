# 3. Дан список целых чисел. Создать новый список, каждый элемент которого
# равен исходному элементу умноженному на -2.
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    i *= -2
    list2.append(i)
print(list2)
