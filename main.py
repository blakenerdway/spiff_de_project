import os
import logging
import calculator

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    deals = calculator.read_file_as_json(os.path.join(dir_path, 'data/deals.json'))
    products = calculator.read_file_as_json(os.path.join(dir_path, 'data/products.json'))

    calc = calculator.CommissionCalculator(deals, products)

    commission = calc.calculate_commission('Ian', '2023-01-01', '2023-03-10')
    logger.info(f'Ian commission: {commission}')

    commission = calc.calculate_commission('Poppy', '2023-01-01', '2023-03-10')
    logger.info(f'Poppy commission: {commission}')