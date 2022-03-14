class Property():

    def __init__(self, propertyId, address, city, status, price, description, year_of_construction):
        self.propertyId = propertyId
        self.address = address
        self.city = city
        self.status = status
        self.price = price
        self.description = description
        self.year_of_construction = year_of_construction

    def get_id(self):
        return self.propertyId

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_year_of_construction(self):
        return self.year_of_construction

    def to_json(self):
        return {
            'id': self.get_id(),
            'address': self.get_address(),
            'city': self.get_city(),
            'status': self.get_status(),
            'price': self.get_price(),
            'description': self.get_description()
        }
