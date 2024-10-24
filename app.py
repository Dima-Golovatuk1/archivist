"""
Цей модуль керує основними функціями додатку.
"""

class Letter:
    """
    Клас Letter представляє окрему букву з певною міткою.
    """

    def __init__(self, mark, symbol):
        """
        mark: числове значення, яке відповідає маркеру
        symbol: символ, який представляє букву
        """
        self.mark = mark
        self.symbol = symbol

    def add_list(self, lis):
        """
        Додає мітку і символ до переданого списку.
        lis: список, до якого додаються значення
        """
        lis.append(str(self.mark) + self.symbol)  # Додаємо в список lis


def coder(content):
    """
    Кодує вміст файлу.
    content: вміст файлу для кодування
    """
    num = 1
    repetition = {}
    current_sequence = ''
    k = 0
    lis = []

    for i in content:
        if current_sequence + i in repetition:
            current_sequence += i
            k = repetition[current_sequence]
        else:
            repetition[current_sequence + i] = num
            letter = Letter(k, i)
            letter.add_list(lis)
            num += 1
            current_sequence = ''
            k = 0
    if current_sequence:
        letter = Letter(k, ' ')
        letter.add_list(lis)
    result_string = "'".join(lis)
    with open('coder_file.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(result_string)

    return lis


def decode(encoded_list):
    """
    Декодує текст.
    encoded_list: список закодованих даних
    """
    repetition = {}
    num = 1
    decode_list = []

    for i in encoded_list:
        if i == "0":
            i = "0'"
        mark = i[:-1]
        symbol = i[-1]
        if mark == '0':
            repetition[num] = symbol
            decode_list.append(symbol)
        else:
            symboll = repetition[int(mark)]
            h = symboll + symbol
            repetition[num] = h
            decode_list.append(h)
        num += 1
    text = ''.join(decode_list)
    return text
