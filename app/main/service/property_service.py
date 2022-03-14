from main.repository.property_repository import *


class PropertyService():
    def __init__(self,repository = None) -> None:
        if repository is not None:
            self.repository = repository
        else:
            self.repository = PropertyRepository()

    def get_properties(self, filters={}):
        properties = self.repository.get_properties(filters=filters)
        return properties
