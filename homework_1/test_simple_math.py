import unittest
# Импортируем класс SimpleMath из созданного ранее файла
from simple_math import SimpleMath


class TestSimpleMath(unittest.TestCase):

    def setUp(self):
        """Инициализация объекта класса перед каждым тестом."""
        self.math = SimpleMath()

    def test_square_positive(self):
        """Тест метода square с положительным числом."""
        self.assertEqual(self.math.square(2), 4)

    def test_square_negative(self):
        """Тест метода square с отрицательным числом."""
        self.assertEqual(self.math.square(-5), 25)

    def test_square_zero(self):
        """Тест метода square с нулем."""
        self.assertEqual(self.math.square(0), 0)

    def test_cube_positive(self):
        """Тест метода cube с положительным числом."""
        self.assertEqual(self.math.cube(3), 27)

    def test_cube_negative(self):
        """Тест метода cube с отрицательным числом."""
        self.assertEqual(self.math.cube(-3), -27)

    def test_cube_zero(self):
        """Тест метода cube с нулем."""
        self.assertEqual(self.math.cube(0), 0)


if __name__ == '__main__':
    unittest.main()
