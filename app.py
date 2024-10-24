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
    repetition = {}  # Для збереження унікальних послідовностей
    current_sequence = ''
    k = 0
    lis = []

    for i in content:
        if current_sequence + i in repetition:  # Якщо поточна послідовність вже зустрічалась
            current_sequence += i
            k = repetition[current_sequence]  # Отримуємо мітку
        else:
            repetition[current_sequence + i] = num  # Додаємо нову послідовність
            letter = Letter(k, i)  # Створюємо новий об'єкт Letter
            letter.add_list(lis)  # Додаємо до списку закодованих значень
            num += 1
            current_sequence = ''  # Очищаємо поточну послідовність
            k = 0
    if current_sequence:  # Якщо залишились непроцесовані символи
        letter = Letter(k, ' ')
        letter.add_list(lis)
    result_string = "'".join(lis)

    return lis  # Повертаємо закодований список


def decode(encoded_list):
    """
    Декодує текст.
    encoded_list: список закодованих даних
    """
    repetition = {}
    num = 1
    decode_list = []

    for item in encoded_list:
        mark = item[:-1]  # Витягуємо мітку
        symbol = item[-1]  # Витягуємо символ

        if mark == '0':  # Якщо мітка '0', це новий символ
            repetition[num] = symbol  # Зберігаємо символ
            decode_list.append(symbol)  # Додаємо до декодованого списку
        else:
            prev_sequence = repetition[int(mark)]  # Отримуємо послідовність за міткою
            new_sequence = prev_sequence + symbol  # Додаємо новий символ до попередньої послідовності
            repetition[num] = new_sequence  # Зберігаємо оновлену послідовність
            decode_list.append(new_sequence)  # Додаємо до результату

        num += 1

    return ''.join(decode_list)  # Повертаємо декодований текст


