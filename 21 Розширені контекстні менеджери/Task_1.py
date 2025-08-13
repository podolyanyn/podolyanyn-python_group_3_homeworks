from datetime import datetime

class LoggedOpen:
    open_count = 0

    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        LoggedOpen.open_count += 1
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Відкрито файл: {self.filename}")
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Закрито файл: {self.filename}")
        return False

if __name__ == "__main__":

    with LoggedOpen("example.txt", "w") as f:
        f.write("Привіт, світ!")


    with LoggedOpen("example.txt", "r") as f:
        content = f.read()
        print("Зміст файлу:", content)

    print("Файли відкривались:", LoggedOpen.open_count)