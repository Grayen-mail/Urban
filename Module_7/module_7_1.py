# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Режимы открытия файлов" """

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ''

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        existing_products = [product.split(', ')[0] for product in existing_products if product]

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_products:
                    try:
                        file.write(str(product) + '\n')
                    except IOError:
                        print(f'Ошибка записи в файл')
                    else:
                        # existing_products.append(product.name)  # если нужно убрать дубликаты в списке
                        pass
                else:
                    print(f'Продукт {product.name} уже есть в магазине')


# Пример работы программы
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
