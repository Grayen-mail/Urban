# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Файлы в операционной системе" """

import os
import time

work_dir = os.path.abspath('.')
for dirpath, dirnames, filenames in os.walk(work_dir):
    # print(f'Directory: {dirpath}')
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        # print(f'File: {filepath}')
        filetime = os.path.getmtime(os.path.join(dirpath, file))
        # print(f'File time: {filetime}')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # print(f'Formatted time: {formatted_time}')
        filesize = os.path.getsize(filepath)
        # print(f'File size: {filesize}')
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,',
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
