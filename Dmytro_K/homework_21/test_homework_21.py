import unittest
import os
import logging



class OpenImitator:
    count = 0

    # Create a logger named "OpenImitatorLogger" that records messages.
    # Use FileHandler to save logs to a file, with time and level formatting.

    logger = logging.getLogger("OpenImitatorLogger")
    logger.setLevel(logging.INFO)

    log_path = os.path.abspath("open_imitator.log")
    handler = logging.FileHandler(log_path, mode='a')
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(handler)


    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        OpenImitator.count += 1
        OpenImitator.logger.info(f"Opening file: {self.filename} in mode: {self.mode}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
       self.file.close()
       OpenImitator.logger.info(f"Closed file: {self.filename}")
       if exc_type:
           OpenImitator.logger.error(f"Exception occurred: {exc_type.__name__} - {exc_val}")
       return False


class TestOpenImitator(unittest.TestCase):
    def setUp(self):
        self.test_file = "test.txt"
        OpenImitator.count = 0

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read(self):
        with OpenImitator(self.test_file, "w") as f:
            f.write("Hello")
        with OpenImitator(self.test_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello")
        self.assertEqual(OpenImitator.count, 2)

    def test_file_closed(self):
        with OpenImitator(self.test_file, "w") as f:
            f.write("Test")
            self.assertFalse(f.closed)
        self.assertTrue(f.closed)

    def test_many_usages(self):
        for _ in range(3000):
            with OpenImitator(self.test_file, "w") as f:
                f.write("x")
        self.assertEqual(OpenImitator.count, 3000)

    def test_error_inside_with(self):
        try:
            with OpenImitator(self.test_file, "w") as f:
                raise ValueError("Boom")
        except ValueError as e:
            self.assertEqual(str(e), "Boom")
        self.assertEqual(OpenImitator.count, 1)

    def test_file_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            with OpenImitator("no_file.txt", "r") as f:
                f.read()

    def test_none_filename(self):
        with self.assertRaises(TypeError):
            with OpenImitator(None, "r") as f:
                pass

    def test_write_in_read_mode(self):
        with OpenImitator(self.test_file, "w") as f:
            f.write("data")
        with OpenImitator(self.test_file, "r") as f:
            with self.assertRaises(OSError):
                f.write("fail")

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            with OpenImitator(self.test_file, "badmode") as f:
                pass

    def test_logging_output(self):
        log_file = "open_imitator.log"
        if os.path.exists(log_file):
            os.remove(log_file)

        OpenImitator.logger.handlers.clear()
        handler = logging.FileHandler(log_file, mode='a')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        OpenImitator.logger.addHandler(handler)

        with OpenImitator(self.test_file, "w") as f:
            f.write("Log test")
        with OpenImitator(self.test_file, "r") as f:
            _ = f.read()

        self.assertTrue(os.path.exists(log_file))

        with open(log_file, "r") as log:
            log_content = log.read()
            self.assertIn("Opening file: test.txt in mode: w", log_content)
            self.assertIn("Closed file: test.txt", log_content)
            self.assertIn("Opening file: test.txt in mode: r", log_content)


if __name__ == "__main__":
    unittest.main()

#test result

# ============================= test session starts ==============================
# collecting ... collected 9 items
#
# homework_21/test_homework_21.py::TestOpenImitator::test_error_inside_with
# homework_21/test_homework_21.py::TestOpenImitator::test_file_closed
# homework_21/test_homework_21.py::TestOpenImitator::test_file_not_exist
# homework_21/test_homework_21.py::TestOpenImitator::test_invalid_mode
# homework_21/test_homework_21.py::TestOpenImitator::test_logging_output
# homework_21/test_homework_21.py::TestOpenImitator::test_many_usages
# homework_21/test_homework_21.py::TestOpenImitator::test_none_filename
# homework_21/test_homework_21.py::TestOpenImitator::test_write_and_read
# homework_21/test_homework_21.py::TestOpenImitator::test_write_in_read_mode
#
# ============================== 9 passed in 1.00s ===============================
# PASSED [ 11%]PASSED [ 22%]PASSED [ 33%]PASSED [ 44%]PASSED [ 55%]PASSED [ 66%]PASSED [ 77%]PASSED [ 88%]PASSED [100%]
# Process finished with exit code 0

    
            
            
            
        
