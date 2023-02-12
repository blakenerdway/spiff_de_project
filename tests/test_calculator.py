from unittest import TestCase

import pytest
import calculator as calc
import os


class CommissionCalculatorTest(TestCase):
    def test_valid_commissions(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        products = calc.read_file_as_json(os.path.join(dir_path, 'data/products.json'))
        deals = calc.read_file_as_json(os.path.join(dir_path, 'data/deals.json'))
        commission_calc = calc.CommissionCalculator(deals, products)
        print('Calculating commission for Ian')
        commission = commission_calc.calculate_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-4-30")
        self.assertEqual(commission, 55350.00)

        print('Calculating commission for David')
        commission = commission_calc.calculate_commission(sales_rep_name="David", start_date="2023-04-01", end_date="2023-06-30")
        self.assertEqual(commission, 89540.00)

        print('Calculating commission for Poppy')
        commission = commission_calc.calculate_commission(sales_rep_name="Poppy", start_date="2023-03-01", end_date="2023-5-30")
        self.assertEqual(commission, 118190.00)
