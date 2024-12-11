# -*- coding: utf-8 -*-

""" Домашнее задание по теме "Оператор "with" """
import re


class WordsFinder:
    """Объект этого класса должен принимать при создании неограниченного количество названий файлов
       и записывать их в атрибут file_names в виде списка или кортежа.
    """
    def __init__(self, *strings):
        self.file_names = [file for string in strings for file in string.split(', ')]

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            words = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    words.extend(re.sub(r"[',.=!?;:]", '', line.lower().replace(' - ', '')).split())
            all_words[file_name] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_[file_name] = words.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for file_name, words in self.get_all_words().items():
            count = 0
            count += words.count(word.lower())
            dict_[file_name] = count
        return dict_


# finder2 = WordsFinder('file1.txt, file2.txt', 'file3.txt')
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
