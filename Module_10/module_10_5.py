# -*- coding: utf-8 -*-

# Домашнее задание по теме "Многопроцессное программирование"

import threading
import time
from multiprocessing import Pool
from datetime import timedelta


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        for line in f:
            all_data.append(line.strip())


# файлы распакованы в папку Files
filenames = [f'./Files/file {i}.txt' for i in range(1, 5)]

# Линейный вызов
time_start = time.time()

for filename in filenames:
    read_info(filename)

time_end = time.time()
print(f'Время при линейном вызове {timedelta(seconds=time_end - time_start)}')


# Многопроцессный вызов
if __name__ == '__main__':
    time_start = time.time()

    with Pool(len(filenames)) as p:
        p.map(read_info, filenames)

    time_end = time.time()
    print(f'Время при многопроцессном вызове {timedelta(seconds=time_end - time_start)}')
