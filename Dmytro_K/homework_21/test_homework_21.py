import unittest
import os



class OpenImitator:
    count = 0

    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        OpenImitator.count += 1
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
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

if __name__ == "__main__":
    unittest.main()

        
    
            
            
            
        