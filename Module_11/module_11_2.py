# -*- coding: utf-8 -*-
# Домашнее задание по теме "Интроспекция"

import inspect
from pprint import pprint

# Для интроспекции модуля и класса
# используется выполненное задание из 6-го модуля
import os.path, requests
if not os.path.isfile('module_6_3.py'):
    with open('module_6_3.py', 'w', encoding='utf-8') as f:
        try:
            r = requests.get(
                'https://raw.githubusercontent.com/Grayen-mail/Urban/refs/heads/main/Module_6/module_6_3.py'
            )
        except:
            pass
        else:
            f.writelines(r.text)

if os.path.isfile('module_6_3.py'):
    import module_6_3 as m
else:
    m = None


def introspection_info(obj):
    """ Функция интроспекции
    """
    info = dict()

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты объекта
    info['attributes'] = dir(obj)

    # Методы объекта
    methods = [name for name in dir(obj) if callable(getattr(obj, name))]
    info['methods'] = methods

    # Модуль, к которому объект принадлежит
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else '__main__'

    # Другие интересные свойства объекта
    if hasattr(obj, '__dict__'):
        info['dict'] = obj.__dict__

    if hasattr(obj, '__doc__'):
        info['docstring'] = obj.__doc__

    return info


# Число 42
number_info = introspection_info(42)
print('Интроспекция числа 42:\n' + '-'*40)
pprint(number_info)

# Словарь
print('\n\nИнтроспекция словаря:\n' + '-'*40)
dict_info = introspection_info(number_info)
pprint(dict_info)

# Модуль и класс из модуля
if m is not None:
    # module
    print('\n\nИнтроспекция модуля:\n' + '-'*40)
    module_info = introspection_info(m)
    pprint(module_info)

    # class
    print('\n\nИнтроспекция класса:\n' + '-'*40)
    class_info = introspection_info(m.Animal)
    pprint(class_info)

# Функция
print('\n\nИнтроспекция функции:\n' + '-'*40)
func_info = introspection_info(introspection_info)
pprint(func_info)
