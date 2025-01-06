# -*- coding: utf-8 -*-

# Домашнее задание по теме "Создание потоков"

from threading import Thread
import time
from datetime import timedelta


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i+1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
print(f'Работа функций {timedelta(seconds=time_end - time_start)}')

time_start = time.time()
treads = [
    Thread(target=write_words, args=(10, 'example5.txt')),
    Thread(target=write_words, args=(30, 'example6.txt')),
    Thread(target=write_words, args=(200, 'example7.txt')),
    Thread(target=write_words, args=(100, 'example8.txt'))
]

for tread in treads:
    tread.start()

for tread in treads:
    tread.join()

time_end = time.time()
print(f'Работа потоков {timedelta(seconds=time_end - time_start)}')
