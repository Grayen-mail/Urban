# -*- coding: utf-8 -*-

""" Дополнительное практическое задание по модулю 6 """


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled: bool = False):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        elif len(sides) == 1 and isinstance(sides[0], int):
            self.__sides = list(sides) * self.sides_count
        else:
            self.__sides = [1 for _ in range(self.sides_count)]
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(*color):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in color)

    def set_color(self, *color):
        self.__color = list(color) if self.__is_valid_color(*color) else self.__color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and \
                len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        self.__sides = list(new_sides) if self.__is_valid_sides(*new_sides) \
                        else self.__sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        # sides = sides if len(sides) == 1 and sides[0] > 0 else [1]
        super().__init__(color, *sides, filled=True)
        self.__radius = sides[0] / 2 / 3.14

    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled=True)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        sides = [sides[0] for _ in sides]
        super().__init__(color, *sides, filled=True)

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
print(f'Цвет круга circle1 до изменения: {circle1.get_color()}')
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'Цвет круга circle1 после изменения: {circle1.get_color()} - изменилось\n')

print(f'Цвет куба cube1 до изменения: {cube1.get_color()}')
cube1.set_color(300, 70, 15)  # Не изменится
print(f'Цвет куба cube1 после изменения: {cube1.get_color()} - не изменилось\n')

# Проверка на изменение сторон:
print(f'Стороны куба cube1 до изменения: {cube1.get_sides()}')
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(f'Стороны куба cube1 после изменения: {cube1.get_sides()} - не изменилось\n')

print(f'Окружность circle1 до изменения: {circle1.get_sides()}')
circle1.set_sides(15)  # Изменится
print(f'Окружность circle1 после изменения: {circle1.get_sides()} - изменилось')

# Проверка периметра (круга), это и есть длина:
print(f'Периметр круга circle1: {len(circle1)}\n')

# Проверка объёма (куба):
print(f'Объём куба cube1: {cube1.get_volume()}\n')

triangle1 = Triangle((200, 200, 100), 3, 4, 5)
print(f'Площадь треугольника triangle1: {triangle1.get_square()}')
print(f'Цвет треугольника triangle1: {triangle1.get_color()}')
print(f'Стороны треугольника triangle1: {triangle1.get_sides()}\n')

cube2 = Cube((30, 30, 30), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print(f'Стороны куба cube2: {cube2.get_sides()}')
