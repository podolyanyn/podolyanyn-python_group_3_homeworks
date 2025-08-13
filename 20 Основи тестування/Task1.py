import unittest
import math

def safe_log(x, base=math.e):
    """Обчислює логарифм числа x за основою base.
    Повертає None, якщо x <= 0 або base <= 0 або base == 1.
    """
    if x <= 0 or base <= 0 or base == 1:
        return None
    return math.log(x, base)

class TestLogFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(safe_log(1), 0)
        self.assertAlmostEqual(safe_log(math.e), 1)
        self.assertAlmostEqual(safe_log(8, 2), 3)

    def test_invalid_x(self):
        self.assertIsNone(safe_log(0))
        self.assertIsNone(safe_log(-5))

    def test_invalid_base(self):
        self.assertIsNone(safe_log(10, 0))
        self.assertIsNone(safe_log(10, 1))
        self.assertIsNone(safe_log(10, -2))

    def test_custom_base(self):
        self.assertAlmostEqual(safe_log(27, 3), 3)
        self.assertAlmostEqual(safe_log(16, 2), 4)


if __name__ == "__main__":
    unittest.main()
