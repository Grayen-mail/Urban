# -*- coding: utf-8 -*-

# Домашнее задание по теме "Генераторные сборки"


first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(i[0])-len(i[1])) for i in zip(first, second) if not len(i[0])-len(i[1]) == 0)
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))
