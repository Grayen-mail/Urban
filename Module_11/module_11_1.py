# -*- coding: utf-8 -*-
# Домашнее задание по теме "Обзор сторонних библиотек Python"

# Для выполнения требуется распакованный файл опроса Kaggle 2022
# https://www.kaggle.com/datasets/abhishekshaw020/kaggle-survey-responses-2022

import requests
import os.path
import pandas as pd
import matplotlib.pyplot as plt


# requests
print('Пример использования библиотеки requests:')
print('https://wttr.in/')
city = 'Москва'
opt = '0'  # 0 - текущая, 1 - текущая + 1 день, 2 - текущая + 2 дня
lang = 'ru'
response = requests.get(f'https://wttr.in/{city}?{opt}&lang={lang}')
if response.status_code == 200:
    print(response.text)
else:
    print(f'Ошибка: {response}')

input('Для продолжения нажмите Enter')

# pandas
print('Пример использования библиотеки pandas:')
print('Ответы на опрос Kaggle 2022:')
if not os.path.isfile('kaggle_survey_2022_responses.csv'):
    print(f'Файл "kaggle_survey_2022_responses.csv" не найден')
else:
    data = pd.read_csv('kaggle_survey_2022_responses.csv', low_memory=False)
    print('Количество респондентов по возрастным группам:\n', data.Q2.value_counts(), '\n\n')

    input('Для продолжения нажмите Enter')

    woman_data = data[
        data['Q4'].str.contains('Russia') &         # из России
        data['Q5'].str.contains('No')               # не студент
        ].Q3.value_counts(normalize=True)['Woman']
    print('Доля женщин среди русских респондентов,'
          'которые уже не студенты -', '\033[4m', woman_data.round(2), '\033[0m')

    data.drop(0, inplace=True)
    data['Duration (in seconds)'] = data['Duration (in seconds)'].astype(int)
    print('Среднее время заполнения опроса в минутах:', '\033[4m',
          round(data['Duration (in seconds)'].mean()/60, 2), '\033[0m\n')

    q12_col = [col for col in data.columns if col.startswith('Q12')]
    data_DS = data.query('Q23 =="Data Scientist"')
    print('Топ-5 языков программирования, которые регулярно используют Data Scientists в своей работе:\033[4m',
          *data_DS[q12_col].melt(None, q12_col)['value'].value_counts()[:5].index, '\033[0m', sep='\n')

    input('Для продолжения нажмите Enter')

# matplotlib
    print('Пример использования библиотеки matplotlib:')
    data_age = data.Q2.value_counts(normalize=True).round(3)
    fig, ax = plt.subplots(dpi=200)
    wedges, texts, autotexts = ax.pie(data_age.values,
                                      autopct='%.1f',
                                      explode=[0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                      labels=None)
    ax.legend(wedges, list(data_age.index), loc="lower left",
              bbox_to_anchor=(-0.1, 0.07, 0., 0.), fontsize='x-small')
    plt.setp(autotexts, size='xx-small', weight='normal', style='normal')
    _ = ax.set_title('Возраст респондента')
    plt.show()
