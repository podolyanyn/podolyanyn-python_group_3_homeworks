from math import gcd
from numbers import Integral

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменник не може бути 0")
        if not isinstance(numerator, Integral) or not isinstance(denominator, Integral):
            raise TypeError("Чисельник і знаменник мають бути цілими числами")

        g = gcd(numerator, denominator)
        numerator //= g
        denominator //= g

        if denominator < 0:
            numerator *= -1
            denominator *= -1

        self.n = numerator
        self.d = denominator

    def __repr__(self):
        return f"{self.n}/{self.d}"

    # допоміжний метод для перетворення int у Fraction
    def _coerce(self, other):
        if isinstance(other, Fraction):
            return other
        if isinstance(other, Integral):
            return Fraction(other, 1)
        return NotImplemented

    def __add__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __rsub__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Fraction(other.n * self.d - self.n * other.d, self.d * other.d)

    def __mul__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Fraction(self.n * other.n, self.d * other.d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        if other.n == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return Fraction(self.n * other.d, self.d * other.n)

    def __rtruediv__(self, other):
        other = self._coerce(other)
        if self.n == 0:
            raise ZeroDivisionError("Ділення на нуль")
        return Fraction(other.n * self.d, other.d * self.n)

    def __eq__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return self.n * other.d < other.n * self.d

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
    print(x + 10)   # 3/2
    print(25 - x)   # 3/2
    print(36 * y)   # 3/4
    print(10 / y)   # 4/1
