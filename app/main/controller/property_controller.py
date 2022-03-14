from flask_restful import Resource, Api, request
from flask import current_app, Blueprint, jsonify

from main.service.property_service import PropertyService


properties_bp = Blueprint('properties_bp', __name__)
api = Api(properties_bp)


class PropertiesList(Resource):

    def __init__(self) -> None:
        self.service = PropertyService()

    def post(self):
        filters = request.get_json()
        print(filters)
        properties = self.service.get_properties(filters=filters)
        return jsonify(properties)


api.add_resource(PropertiesList, '/')
