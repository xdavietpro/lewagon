# app/__init__.py
from flask import Flask, request

def create_app():
    app = Flask(__name__)

    from app.main.controllers import main # Relative is possible from .main.controllers import main
    app.register_blueprint(main)

    return app
