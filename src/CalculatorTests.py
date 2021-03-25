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
        multiply_test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in multiply_test_data:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        multiply_test_data.clear()

    def test_divide_method_calculator(self):
        divide_test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in divide_test_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        divide_test_data.clear()

    def test_square_method_calculator(self):
        square_test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in square_test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        square_test_data.clear()

    def test_sqrt_method_calculator(self):
        sqrt_test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in sqrt_test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        sqrt_test_data.clear()


if __name__ == '__main__':
    unittest.main()
