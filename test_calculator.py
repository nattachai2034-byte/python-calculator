import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add1(self):
        self.assertEqual(self.calc.add(1, 2), 3)


    # Add the following test methods to the TestCalculator class:
    def test_add2(self):
        self.assertEqual(self.calc.add(5, 5), 10)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(10, 7), 3)

    def test_multiply(self):
            self.assertEqual(self.calc.multiply(7, 7), 49)

    def test_multiply2(self):
                self.assertEqual(self.calc.multiply(11, 11), 121)

    def test_divide(self):
                self.assertEqual(self.calc.divide(70, 7), 10)

    def test_divide2(self):
                self.assertEqual(self.calc.divide(96, 8), 12)

    def test_modulo(self):
                self.assertEqual(self.calc.modulo(7, 3), 1)

    def test_modulo2(self):
                    self.assertEqual(self.calc.modulo(7, 7), 0)

    



if __name__ == '__main__':
    unittest.main()