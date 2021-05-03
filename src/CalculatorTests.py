import unittest
from Calculator import Calculator
from csvReader import CsvReader
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) ->None:
        self.calculator =Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.square_root(4), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_add_csv(self):
        test_data_add = CsvReader("csvFiles/Unit Test Addition.csv").data
        for row in test_data_add:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_subtract_csv(self):
        test_data_subtract = CsvReader("csvFiles/Unit Test Subtraction.csv").data
        for row in test_data_subtract:
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_multiply_csv(self):
        test_data_multiply = CsvReader("csvFiles/Unit Test Multiplication.csv").data
        for row in test_data_multiply:
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_divide_csv(self):
        test_data = CsvReader("csvFiles/Unit Test Division.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 2'], row['Value 1']), round(float(row['Result']), 9))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))

    def test_square_csv(self):
        test_data = CsvReader("csvFiles/Unit Test Square.csv").data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square_root_csv(self):
        test_data = CsvReader('./src/tests/square_root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(row['Value 1']), round(float(row['Result']), 9))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 9))

    if __name__ == '__main__':
        unittest.main()