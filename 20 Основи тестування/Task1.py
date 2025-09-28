import os
from datetime import datetime

class SmartFile:
    opened_files_count = 0
    log_dir = "logs"

    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
        self.start_time = None
        os.makedirs(self.log_dir, exist_ok=True)

    def __enter__(self):
        SmartFile.opened_files_count += 1
        self.start_time = datetime.now()
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self._log_event("OPENED")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()

        self._log_event("CLOSED")

        if exc_type:
            self._log_event(f"ERROR: {exc_type.__name__} - {exc_val}")
            return False  # False = помилка підніметься далі

    def _log_event(self, event):
        log_path = os.path.join(self.log_dir, "file_log.txt")
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{event} | File: {self.filename} | Mode: {self.mode} "
                f"| Total opened: {SmartFile.opened_files_count}\n"
            )
with SmartFile("test.txt", "w") as f:
    f.write("Привіт, світ!\n")

with SmartFile("test.txt", "r") as f:
    print(f.read())