# -*- coding: utf-8 -*-

# Домашнее задание по теме "Создание функций на лету"

from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        try:
            # text version
            # with open(file_name, 'w', encoding='utf-8') as file:
            #     for data in data_set:
            #         file.write(str(data)+'\n')

            # binary version
            with open(file_name, 'wb') as file:
                for data in data_set:
                    file.write(str(data).encode('utf-8')+b'\n')
        except IOError as err:
            print(f'Ошибка записи: {err}')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка',
      ['А', 'это', 'уже', 'число', 5, 'в', 'списке'],
      10,
      {1, 2, 3, 4, 5},
      {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
      (1, 2, 3, 4, 5))


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return self.words[choice(range(len(self.words)))]


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
