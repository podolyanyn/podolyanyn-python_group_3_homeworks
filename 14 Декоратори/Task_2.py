def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator


@stop_words(['пепсі', 'BMW', 'на хрін', 'козел'])  # Стоп-слова які будемо фільтрувати
def format_message(text: str) -> str:
    return text


#  Отримуємо текст від користувача
user_input = input("Введи речення: ")

#   Обробляємо і виводимо
filtered = format_message(user_input)
print("  Відфільтровано:", filtered)