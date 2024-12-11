# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Позиционирование в файле" """


def custom_write(file_name, text):
    with open(file_name, 'w', encoding='utf-8') as file:
        res = {}
        i = 1
        try:
            for line in text:
                res[i, file.tell()] = line
                file.write(line + '\n')
                i += 1
        finally:
            file.close()
    return res


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
