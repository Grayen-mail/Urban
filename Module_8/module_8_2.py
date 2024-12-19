# -*- coding utf-8 -*-

""" Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции" """


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {num}")
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        if not isinstance(numbers, (str, list, tuple, set, dict)):
            print("В numbers записан некорректный тип данных")
            return None
        if isinstance(numbers, dict):
            numbers = list(numbers.values())
        sum_result, incorrect_data = personal_sum(numbers)
        return sum_result / len([num for num in numbers if isinstance(num, (int, float))])
    except ZeroDivisionError:
        return 0


# Пример работы программы
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
print(f'Результат 5: {calculate_average({42, 15, 36, 13})}')
print(f"Результат 6: {calculate_average({'one': 42, 'two': 15, 'three': 36, 'four': 13})}")
