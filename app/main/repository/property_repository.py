from main.utils.database import *
from main.utils.sql_raw_strings import get_properties_sql
from main.model.property import Property


class PropertyRepository():
    """
    Class to get info about properties
    """

    def __init__(self):
        self.database_connection = Database().get_connection()

    def get_properties(self, filters={}):
        filters_string = get_properties_sql
        filters_keys = filters.keys()

        if('price_lower_than' in filters_keys and 'price_greater_than' in filters_keys and filters['price_lower_than'] != '' and filters['price_greater_than'] != ''):
            filters_string += f" AND p.price between {filters['price_greater_than']} and {filters['price_lower_than']}"
        else:
            if('price_lower_than' in filters_keys and filters['price_lower_than'] != ''):
                filters_string += f"AND p.price < {filters['price_lower_than']}"

            elif('price_greater_than' in filters_keys and filters['price_greater_than'] != ''):
                filters_string += f" AND p.price > {filters['price_greater_than']}"

        if('year' in filters_keys and filters['year'] != ''):
            filters_string += f" AND p.year = {filters['year']}"

        if('city' in filters_keys and filters['city'] != ''):
            filters_string += f" AND p.city = '{filters['city']}'"

        if('status' in filters_keys and filters['status'] != ''):
            filters_string += f" AND s.name = '{filters['status']}'"

        if('price' in filters_keys and filters['price'] != ''):
            filters_string += f" AND p.price = '{filters['price']}'"

        result = self.database_connection.execute(filters_string + ';')
        result = list(map(self.map_properties, result))
        return result

    def map_properties(self, data):
        return Property(data[0], data[1], data[2], data[11], data[3], data[4], data[5]).to_json()
