import unittest
import tempfile
import os
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


class TestLoggedOpen(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.temp_file.close()

    def tearDown(self):
        if os.path.exists(self.temp_file_name):
            os.remove(self.temp_file_name)

    def test_write_and_read(self):
        text = "Привіт, тест!"
        with LoggedOpen(self.temp_file_name, 'w', encoding='utf-8') as f:
            f.write(text)

        with LoggedOpen(self.temp_file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, text)

    def test_open_count(self):
        initial_count = LoggedOpen.open_count
        with LoggedOpen(self.temp_file_name, 'w'):
            pass
        with LoggedOpen(self.temp_file_name, 'r'):
            pass
        self.assertEqual(LoggedOpen.open_count, initial_count + 2)

    def test_exception_handling(self):
        with self.assertRaises(FileNotFoundError):
            with LoggedOpen("неіснуючий_файл.txt", 'r'):
                pass

if __name__ == '__main__':

    with LoggedOpen("example.txt", "w") as f:
        f.write("Привіт, світ!")

    with LoggedOpen("example.txt", "r") as f:
        content = f.read()
        print("Зміст файлу:", content)

    print("Файли відкривались:", LoggedOpen.open_count)

    unittest.main()