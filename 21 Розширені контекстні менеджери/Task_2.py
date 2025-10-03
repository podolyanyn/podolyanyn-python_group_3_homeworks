from datetime import datetime
import os
import io
import shutil
import tempfile
import unittest

class FileManager:
    open_count = 0

    def __init__(self, path, mode="r", encoding=None, log_path="file_manager.log"):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.log_path = log_path
        self.file = None
        self._entered = False

    def _log(self, message: str) -> None:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_path, "a", encoding="utf-8") as lf:
            lf.write(f"{ts} | {message}\n")

    def __enter__(self):
        try:
            if "b" in self.mode:
                self.file = open(self.path, self.mode)
            else:
                self.file = open(self.path, self.mode, encoding=self.encoding)
            FileManager.open_count += 1
            self._entered = True
            self._log(f"OPEN  path='{self.path}' mode='{self.mode}' open_count={FileManager.open_count}")
            return self.file
        except Exception as e:
            self._log(f"ERROR path='{self.path}' type={type(e).__name__} msg={e} open_count={FileManager.open_count}")
            raise

    def __exit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None:
                self._log(f"ERROR path='{self.path}' type={exc_type.__name__} msg={exc} open_count={FileManager.open_count}")

            if self.file and not self.file.closed:
                try:
                    self.file.flush()
                finally:
                    self.file.close()
        finally:
            if self._entered:
                FileManager.open_count = max(0, FileManager.open_count - 1)
            self._log(f"CLOSE path='{self.path}' mode='{self.mode}' open_count={FileManager.open_count}")
            self.file = None
            self._entered = False

        return False


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix="fm_tests_")
        self.log_path = os.path.join(self.tmpdir, "file_manager.log")
        self.txt_path = os.path.join(self.tmpdir, "demo.txt")
        FileManager.open_count = 0

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def read_log(self):
        if not os.path.exists(self.log_path):
            return ""
        with io.open(self.log_path, "r", encoding="utf-8") as f:
            return f.read()

    def test_write_and_read_text(self):
        data = "Привіт, світ!\n"
        with FileManager(self.txt_path, "w", encoding="utf-8", log_path=self.log_path) as f:
            f.write(data)
            self.assertEqual(FileManager.open_count, 1)  # під час with
        self.assertEqual(FileManager.open_count, 0)      # після with
        with FileManager(self.txt_path, "r", encoding="utf-8", log_path=self.log_path) as f:
            content = f.read()
            self.assertEqual(content, data)

        log = self.read_log()
        self.assertIn("OPEN", log)
        self.assertIn("CLOSE", log)
        self.assertNotIn("ERROR", log)

    def test_nested_contexts_and_open_count(self):
        with FileManager(self.txt_path, "w", encoding="utf-8", log_path=self.log_path) as f1:
            f1.write("A")
            self.assertEqual(FileManager.open_count, 1)
            with FileManager(self.txt_path, "r", encoding="utf-8", log_path=self.log_path) as f2:
                self.assertEqual(f2.read(), "A")
                self.assertEqual(FileManager.open_count, 2)
            self.assertEqual(FileManager.open_count, 1)
        self.assertEqual(FileManager.open_count, 0)

    def test_log_contains_path_and_mode(self):
        with FileManager(self.txt_path, "w", encoding="utf-8", log_path=self.log_path) as f:
            f.write("log me")
        log = self.read_log()
        self.assertIn(self.txt_path, log)
        self.assertIn("mode='w'", log)

    def test_file_is_closed_after_context(self):
        with FileManager(self.txt_path, "w", encoding="utf-8", log_path=self.log_path) as f:
            f.write("X")
            self.assertFalse(f.closed)
        self.assertTrue(f.closed)
        self.assertEqual(FileManager.open_count, 0)

    def test_read_missing_file_raises_and_logged(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager(os.path.join(self.tmpdir, "no_such.txt"),
                             "r", encoding="utf-8", log_path=self.log_path) as f:
                _ = f.read()
        self.assertEqual(FileManager.open_count, 0)
        self.assertIn("ERROR", self.read_log())

    def test_exception_inside_with_not_suppressed(self):
        class Boom(Exception):
            pass

        with self.assertRaises(Boom):
            with FileManager(self.txt_path, "w", encoding="utf-8", log_path=self.log_path) as f:
                f.write("some")
                raise Boom("boom")

        self.assertEqual(FileManager.open_count, 0)
        log = self.read_log()
        self.assertIn("OPEN", log)
        self.assertIn("ERROR", log)
        self.assertIn("CLOSE", log)


if __name__ == "__main__":
    unittest.main(verbosity=2)