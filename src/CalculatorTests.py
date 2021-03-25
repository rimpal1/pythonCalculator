import unittest
from Calculator import Calculator
from csvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result, 0)

    def test_addition(self):
        add_test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in add_test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        add_test_data.clear()

    def test_subtraction(self):
        subtract_test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in subtract_test_data:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        subtract_test_data.clear()

    def test_multiply_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(3, 2), 6)
        self.assertEqual(calculator.result, 6)

    def test_divide_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.result, 3)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(2), 4)
        self.assertEqual(calculator.result, 4)

    def test_sqrroot_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(16), 4)
        self.assertEqual(calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
