# app/main/controllers.py
from flask import Blueprint
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello from a Blueprint!"

