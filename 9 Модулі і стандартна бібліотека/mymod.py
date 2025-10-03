import os
def count_lines(name):
    with open(name, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def count_chars(name):
    with open(name, 'r', encoding='utf-8') as f:
        return len(f.read())

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)
    print(f"\n{name} має {lines} рядків та {chars} символів.\n")

user_input = input("Введи ім'я файлу або шлях до нього: ").strip()

if os.path.isfile(user_input):
    file_path = os.path.abspath(user_input)
else:

    filename_to_find = user_input
    project_root = os.path.dirname(os.path.abspath(__file__))
    file_path = None

    for dirpath, dirnames, filenames in os.walk(project_root):
        if filename_to_find in filenames:
            file_path = os.path.join(dirpath, filename_to_find)
            break


if file_path and os.path.isfile(file_path):
    print(" Файл знайдено:", file_path)
    test(file_path)
else:
    print(f" Не вдалося знайти файл за ім'ям/шляхом: {user_input}")