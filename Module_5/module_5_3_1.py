from typing import Union


class House:
    def __init__(self, name: str, floors: int = 1) -> None:
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor: int) -> None:
        if 0 < new_floor <= self.number_of_floors:
            print(*[i for i in range(1, new_floor+1)], sep='\n')
        else:
            print('Такого этажа не существует')

    def __len__(self) -> int:
        return self.number_of_floors

    def __str__(self) -> str:
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __add__(self, other: Union['House', int]) -> 'House':
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return NotImplemented

    def __radd__(self, other: 'House') -> 'House':
        return self.__add__(other)

    def __iadd__(self, other: int) -> 'House':
        return self.__add__(other)

    def __eq__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return NotImplemented

    def __lt__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    def __gt__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented

    def __ge__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented

    def __le__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented

    def __ne__(self, other: 'House') -> bool:
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return NotImplemented


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

h1 = h1 + h2  # __add__
print(h1)

h1 = h2 + h1  # __add__
print(h1)

h1 += h2  # __iadd__
print(h1)
