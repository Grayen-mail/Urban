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

    def eat(self, food: Plant):
        edible: bool = food.__getattribute__(food.name, )
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
    # def __repr__(self):
    #     return f'{self.name}'


class Predator(Animal):
    pass
    # def __repr__(self):
    #     return f'{self.name}'

    # def eat(self, food: Object):
    #     if isinstance(food, Animal):
    #         self.fed = True
    #         print(f'{self.name} съел {food}')
    #     else:
    #         print(f'{self.name} не стал есть {food}')


class Flower(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.edible = True


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
