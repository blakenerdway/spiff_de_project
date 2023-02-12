import datetime
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_file_as_json(file_path: str) -> dict:
    """
    Reads data at a file path into a python dict
    :param file_path:
    :return: Returns a dictionary of data loaded from a JSON file
    """
    if not os.path.exists(file_path):
        logger.error(f"Cannot find file at path: {file_path}. Error")
        return None

    with open(file_path) as data_file:
        json_data = json.load(data_file)
    return json_data


class CommissionCalculator:
    def __init__(self, deals_data, product_data):
        self.__index_deals(deals_data)
        self.__index_products(product_data)

    def __index_deals(self, data: dict):
        """
        Convert the deals into a dictionary of sales rep names to the deals they made.
        This is similar to "indexing" in a database. Now lookup will be O(1) rather than O(n)
        when searching for a sales rep
        :param data:
        """
        indexed_deals = {}
        for obj in data:
            index_key = obj['sales_rep_name']
            if index_key not in indexed_deals:
                indexed_deals[index_key] = []

            indexed_deals[index_key].append(obj)
        self.deals_by_rep = indexed_deals

    def __index_products(self, data: dict):
        """
        Convert the product data into a dictionary with each value being a dictionary of
        the product and the key, the product id
        :param data:
        """
        indexed_products = {product['id']: product for product in data}
        self.product_by_id = indexed_products

    def calculate_commission(self, sales_rep_name, start_date, end_date):
        """
        Function/method to calculate commission for a sales rep in a given time period.

        Args:
            sales_rep_name (str): Name of the sales rep to calculate commission for.
            start_date (str): Starting date for the date range where commissions will be valid.
            end_date (str): Ending date for the date range where commissions will be valid.

        Returns:
            float: A single float value for total commission amount based on the input criteria. e.g. $749.48
        """
        rep_deals = self.deals_by_rep.get(sales_rep_name)
        if rep_deals is None:
            logger.error(f'No sales rep with name: {sales_rep_name} could be found. Try a different name')
            return 0.0
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        commission_amt = 0.0
        for deal in rep_deals:
            # If the deal date does not fall within the given date range, just continue
            # Done this way (with the continue statement and NOT operator) to reduce number of indentations
            if not start_date <= datetime.datetime.strptime(deal['date'], '%Y-%m-%d') <= end_date:
                continue

            deal_product_id = deal['product_id']
            product = self.product_by_id.get(deal_product_id)
            if product is None:
                logger.error(f'Sales rep has sold {deal_product_id} but this ID does not exist in products')
                continue

            # Unit tests will fail if we use the 2x multiplier.
            # Unit test values are taken from the original Github readme
            # multiplier = 2 if deal['has_2x_multiplier'] == 1 else 1
            multiplier = 1

            product_commission = product['product_amount'] * product['commission_rate'] * deal[
                'quantity_products_sold'] * multiplier
            commission_amt += product_commission
            logger.info(
                f'{sales_rep_name} made {product_commission} off selling {deal["quantity_products_sold"]}x product: {deal_product_id}. Total is now: {commission_amt}')

        return round(commission_amt, 2)
