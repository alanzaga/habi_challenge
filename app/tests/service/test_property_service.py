import pytest
from unittest.mock import Mock
from main.service.property_service import *


def test_get_properties():
    property_repository = Mock()

    property_repository.get_properties.return_value = [
    {
        "address": "calle 23 #45-67",
        "city": "bogota",
        "description": "Hermoso apartamento en el centro de la ciudad",
        "id": 1,
        "price": 120000000,
        "status": "pre_venta"
    }]

    service = PropertyService(repository=property_repository)
    result = service.get_properties()
    assert type(result) == list
