import pytest
from main.repository.property_repository import *

repository = PropertyRepository()


def test_get_properties_should_be_list():
    """
    should return list properties
    """
    result = repository.get_properties()
    assert type(result) == list


def test_map_properties_should_return_json():
    """
    should return properties json
    """
    properties = [(3, 'diagonal 23 #28-21', 'bogota', 270000000, 'Apartamento con hermosas vistas',
                   2018, 12, 3, 5, None, 5, 'vendido', 'Inmueble vendido')]
    result = list(map(repository.map_properties, properties))
    assert type(result[0]) == dict
