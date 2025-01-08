# -*- coding: utf-8 -*-

# Домашнее задание по теме "Потоки на классах"

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self._enemy = 100
        self._delay = 1

    def run(self):
        enemy = self._enemy
        print(f'{self.name}, на нас напали!')
        days = 0
        while enemy:
            days += 1
            enemy -= self.power if enemy > self.power else enemy
            print(f'{self.name}, сражается {days} день(дня)... Осталось {enemy} воинов.')
            time.sleep(self._delay)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
