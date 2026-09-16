import unittest
import calculator #import calculator.py

class TestCalculatorFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-2, -2), -4)

    def test_sub(self):
        self.assertEqual(calculator.sub(5, 3), 2)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(-1, -1), -0)

    def test_div(self):
        self.assertEqual(calculator.div(10,2), 5)
        self.assertEqual(calculator.div(10,-2), -5)

    def test_mul(self):
        self.assertEqual(calculator.mul(5,5), 25)
        self.assertEqual(calculator.mul(5,-5), -25)
        self.assertEqual(calculator.mul(-5,-5), 25)
        self.assertEqual(calculator.mul(5,0), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10,0)


if __name__ == '__main__':
    unittest.main()