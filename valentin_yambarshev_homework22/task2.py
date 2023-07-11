# 2. Создайте класс Робот
# создайте 2 типа оружия: меч, автомат
# Создайте 2 типа амуниции: броня, шлем
# Добавьте оружию и амуниции свои характеристики(например урон, прочность)
# Создайте своего робота с каким либо оружием
# (может быть несколько и брони может быть несколько. Так же может быть ничего)
# Выведите весь арсенал робота на экран

class Robot:

    def __init__(self, name, weapon, ammunition):
        self.name = name
        self.weapon = dict(weapon)
        self.ammunition = dict(ammunition)

    def arsenal(self):
        for key in self.weapon.keys():
            return key

    def damage(self):
        for values in self.weapon.values():
            return values

    def armor(self):
        for key in self.ammunition.keys():
            return key

    def strength(self):
        for values in self.ammunition.values():
            return values

    def __str__(self):
        pass


class Terminator(Robot):

    def __str__(self):
        return f'Terminator - {self.name}, оружие - {Robot.arsenal(self)}, урон - {Robot.damage(self)}, ' \
               f'амуниция - {Robot.armor(self)}, прочность - {Robot.strength(self)}'

class Robokop(Robot):

    def __str__(self):
        return f'Robocop - {self.name}, оружие - {Robot.arsenal(self)}, урон - {Robot.damage(self)}, ' \
               f'амуниция - {Robot.armor(self)}, прочность - {Robot.strength(self)}'


terminatorT1000 = Terminator('T-1000', {'автомат': 12}, {'шлем': 14})
terminatorT800 = Terminator('T-800', {'меч': 23}, {'нагрудник': 18})
robocop = Robokop('Алекс Мерфи', {'пистолет': 34}, {'перчатки': 7})
print(terminatorT1000)
print(terminatorT800)
print(robocop)
