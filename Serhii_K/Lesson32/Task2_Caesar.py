def Caesar_cipher(text_string: str, key: int) -> str:
    """Функція, що шифрує рядок тексту з використанням алгоритму Цезаря.
    Отримує рядок тексту та ключ (кількість шагів здвигу символа по алфавіту)"""
    alphabet1 = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alphabet = ''
    result = ''

    for char in text_string:
        if char in alphabet1:
            alphabet = alphabet1
        elif char in alphabet2:
            alphabet = alphabet2

        index = alphabet.index(char)
        position = index + key

        length = len(alphabet)
        if position < 0:
            result += alphabet[length + position]
        elif position < length:
            result += alphabet[position]
        else:
            result += alphabet[position - length]
    return result


