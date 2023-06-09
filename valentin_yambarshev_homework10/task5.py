# 5. Создайте 2 множества:
# - Если они одинаковы: вывести что они равны;
# - Если 1 множество полностью состоит из второго: вывести сообщение множество 1
# состоит из множества 2;
# - Если 2 множество полностью состоит из 1: вывести сообщение множество 2
# состоит из множества 1;
# - Если они пересекаются: вывести элементы в которых они пересекаются;
# - Если не пересекаются: вывести сообщение об этом.
set1 = {9}
set2 = {1, 2, 3, 4, 5, 6, 7, 9}
if set1 == set2:
    print(f"Множество 'set1': {set1} \n равно \nМножеству 'set2': {set2}")
elif set1.issubset(set2):
    print(f"Множество 'set1': {set1} \nсостоит из \nМножество 'set2': {set2}")
    print(f"Множества пересекаются в следующих элементах: \n{set1.intersection(set2)}")
elif set2.issubset(set1):
    print(f"Множество 'set2': {set2} \nсостоит из \nМножество 'set1': {set1}")
    print(f"Множества пересекаются в следующих элементах: \n{set2.intersection(set1)}")
elif set1.intersection(set2) is not True:
    print("Множества не пересекаются")
