# -*- coding: utf-8 -*-
# python v 3.10.2
'''Универсальный скрипт, использующий train.py, для
обучения моделей, их кодирования и декодирования в формате ".pkl". 
Для получиния случайной последовательности достаточно написать 
"python length_of_sequence --prefix some_word --path ./your_model.pkl" '''
from sys import stdin
from random import choice
import argparse
import pickle


class Creation():
    '''Класс генерации последовательности слов'''

    def __init__(self, model):
        self.model = model

    def generate(self, length, prefix=None):
        '''Создается последовательность'''
        sequence = ''

        for _ in range(length): 
            '''Если подходящее слово находится в словаре, 
            случайно выбирается связанная с ним лексическая еденица'''
            try:
                res = choice(self.model[prefix])
                sequence += res + ' '
                prefix = res
            except KeyError:
                # в случае отсутствия продолжения у данного слова
                # случайно выбирается новый префикс
                sequence += choice(list(self.model.keys())) + ' '

        return sequence


def parse1():
    '''Работа с консолью'''

    path_help_text = 'Задайте путь к файлу, в формате "./your_model.pkl" с обученой \
моделью, или обучите новую при помощи "--learn"'
    learn_help_text = 'Обучите новую модель, задайте путь к файлу, \
в формате "./your_file.txt". Обратите программа работает только с файлами расширением ".txt"'

    # если вызывается данный файл, срабатывает поиск аргументов в консоли
    parser2 = argparse.ArgumentParser()
    parser2.add_argument('length', type=int, help='Длинна последовательности')
    parser2.add_argument('--path', type=str, help=path_help_text)
    parser2.add_argument('--prefix', type=str, help='Первый элемент последовательности')
    parser2.add_argument('--learn', type=str, help=learn_help_text)
    args = parser2.parse_args()

    # строится логика использования аргументов
    if not(args.learn or args.path):
        print('Модель не найдена, пожалуйста воспользуйтесь "--help", для ознакомления \
с возможными вариантами')
        exit()

    # если пользователь предоставил путь к файлу ".pkl"
    elif args.path:
        # распаковка модели
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

    # если пользователь обучает модель
    elif args.learn:
        # если аргументы не найдены, данные поступают из потокового ввода
        if args.learn:
            text = args.learn
        else:
            text = ''.join([line for line in stdin])
        # модель обучается
        model = Education(text).learn()

    # инициализация общих параметров
    length = args.length
    if args.prefix: 
        prefix = args.prefix
    else:
        prefix = ''

    return (model, length, prefix)


# составляется последовательность
value = parse1()
from train import Education
sequence = Creation(value[0])
print(sequence.generate(value[1], value[2]))
