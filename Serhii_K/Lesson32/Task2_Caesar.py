def Caesar_cipher(key: int, text_string: str) -> str:
    """Функція, що шифрує рядок тексту з використанням алгоритму Цезаря.
    Отримує рядок тексту та ключ (кількість шагів здвигу символа по алфавіту)"""
    alphabet1 = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alphabet = ''
    result = ''

    # Опрацьовуємо кожен символ текстового рядка, який потрібно зашифрувати:
    for char in text_string:
        # Визначаємо до якого алфавіту відноситься символ (кирилиця чи латиниця)
        if char in alphabet1:
            alphabet = alphabet1
        elif char in alphabet2:
            alphabet = alphabet2

        # Індекс входження символу в алфавіт:
        index = alphabet.index(char)
        # Позиція входження в алфавіт зі здвигом (позиція зашиіфрованого символу):
        position = index + key
        # Загальна довжина алфавіту
        length = len(alphabet)
        # Якщо позиція в межах алфавіту - додаємо до рядка результату зашифрований символ:
        if 0 <= position < length:
            result += alphabet[position]
        elif position < 0:
            result += alphabet[length + position]
        elif position >= length:
            result += alphabet[position - length]

    return result


