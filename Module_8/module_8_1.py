# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Try и Except" """


def add_everything_up(a, b):
    result = None
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    finally:
        if isinstance(result, float):
            return round(result, 3)
        else:
            return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(123.456, None))
