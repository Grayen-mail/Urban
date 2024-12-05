# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Зачем нужно наследование" """


class Plant:
    def __init__(self, name: str):
        self.name: str = name
        self.edible: bool = False

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Animal:
    def __init__(self, name: str):
        self.name: str = name
        self.alive: bool = True  # Живой
        self.fed: bool = False   # Голодный (True - сытый)

    def eat(self, food: object):
        edible: bool = food.__getattribute__('edible')
        if edible:
            self.fed = True
            print(f'{self.name} съел {food}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food}')

    def __repr__(self) -> object:
        return f'{self.name}'


class Mammal(Animal):
    pass


class Predator(Animal):
    def eat(self, food: object):
        if isinstance(food, Animal):
            self.fed = True
            print(f'{self.name} съел {food}')
        else:
            self.alive = False
            print(f'{self.name} не стал есть {food}')


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.edible = True


if __name__ == '__main__':
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')

    print(a1.name)
    print(p1.name)

    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)

    # added
    a3 = Predator('Гиена')
    print(f'\nНовый хищник: {a3}')
    a3.eat(a2)
    print(a3.alive)
    print(a3.fed)
    print(f'Хищник {a3} съел {a2} и насытился')
