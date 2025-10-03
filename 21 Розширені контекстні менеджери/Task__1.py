from datetime import datetime
class FileManager:
    open_count = 0

    def __init__(self, path, mode="r", encoding=None, log_path="file_manager.log"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.log_path = log_path
        self.file = None

    def _log(self, message):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as lf:
            lf.write(f"{ts} | {message}\n")

    def __enter__(self):
        self.file = open(self.path, self.mode, encoding=self.encoding)
        FileManager.open_count += 1
        self._log(f"OPEN  path='{self.path}' mode='{self.mode}' open_count={FileManager.open_count}")
        return self.file

    def __exit__(self, exc_type, exc, tb):
        try:
            if self.file and not self.file.closed:
                self.file.close()
        finally:
            if FileManager.open_count > 0:
                FileManager.open_count -= 1

        if exc_type is not None:
            self._log(f"ERROR path='{self.path}' type={exc_type.__name__} msg={exc} open_count={FileManager.open_count}")
            return False  # НЕ пригнічуємо виняток — як стандартний open
        else:
            self._log(f"CLOSE path='{self.path}' open_count={FileManager.open_count}")
            return False