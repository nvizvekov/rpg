import weakref


class Unit(object):

    instances = []

    def __init__(self, **props):
        self._name = props['name']
        self._attack = props['attack'] if 'attack' in props.keys() else 0
        self._hp = props['hp'] if 'hp' in props.keys() else 0
        self.__class__.instances.append(weakref.proxy(self))

    name = property()
    attack = property()
    hp = property()

    @hp.getter
    def hp(self):
        print("Hp: {}".format(self._hp))

    @hp.setter
    def hp(self,value):
        pass

    @hp.deleter
    def hp(self):
        print("Am i zombie?")

    @attack.getter
    def attack(self):
        print("I have random attack")
        return self._attack

    @attack.setter
    def attack(self, value):
        print("I need go to gym to be stringer")

    @attack.deleter
    def attack(self):
        pass

    @name.getter
    def name(self):
        print("My name {}".format(self._name))
        return self._name

    @name.setter
    def name(self,value):
        print("No! My name is {}".format(self._name))

    @name.deleter
    def name(self):
        print("You can`t drop my name!")


class Orc(Unit):

    def __init__(self, name):
        super().__init__(**{'name': name,'hp': 100, 'attack': 10})

class Elf(Unit):

    def __init__(self, name):
        super().__init__(**{'name': name,'hp': 70, 'attack': 5})

orc1 = Orc('Myke')
orc2 = Orc('Ivan')
elf1 = Elf('Rick')

for instance in Unit.instances:
    instance.name
    instance.hp
    instance.attack