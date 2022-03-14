from flask import Flask
from main.controller.property_controller import properties_bp

def create_app():
    app = Flask(__name__)
    return app

app = create_app()
app.register_blueprint(properties_bp)