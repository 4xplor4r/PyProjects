# -*- coding: utf-8 -*-
# python v 3.10.2
'''Скрипт для обучения модели, создания классического словаря. Поддерживается
возможность использования подобия интерфейса через argparse в консоли,
достаточно написать "python ./train.py --path your_file".
Подробную инструкцию можно найти в README.txt'''
from sys import stdin
import argparse
import pickle
import re


class Education():
    '''Класс для обучения модели'''

    def __init__(self, materials):
        '''Получение внешних данных'''
        try:
            s = open(materials, encoding='utf-8').readlines()
            self.materials = ''.join(s)
        except OSError:
            self.materials = materials

    def train(self):
        for simbol in '#$";:…«»—*/':
            '''Очищение строки'''
            self.materials = self.materials.replace(simbol, '')
        self.materials = self.materials.lower().replace('\n', ' ')
        # конец любого предложения обозначается точкой
        self.materials = self.materials.replace(',', '.').replace('!', '.')
        self.materials = self.materials.replace('?', '.')

        # множество всех возможных слов
        data = set(self.materials.replace('.', '').split(' '))
        # инициализация модели
        self.model = dict()

        for word in data:
            '''Поиск продолжений после слова'''
            # поиск всех слов после "word"
            res = re.findall(word + r" (\w+)", self.materials)
            if res == []:
                continue
            else:
                self.model[word] = res

    def fit(self):
        '''Записывается сериализованный объект в файл'''
        with open('model.pkl', 'wb') as f:
            pickle.dump(self.model, f)


def parse():
    '''Работа с консолью'''

    path_help_text = 'Задайте путь к файлу с текстом, в формате "./your_file.txt". \
Обратите внимание программа работает только с файлами расширением ".txt"'

    # если вызывается данный файл, срабатывает поиск аргументов в консоли
    parser1 = argparse.ArgumentParser()
    parser1.add_argument('--path', type=str, help=path_help_text)
    args = parser1.parse_args()

    # если аргументы не найдены, данные поступают из потокового ввода
    if args.path:
        text = args.path
    else:
        text = ''.join([line for line in stdin])
    parser1.exit

    return text


# инициализация
model = Education(parse())
model.train()
# упаковка в ".pkl"
model.fit()
