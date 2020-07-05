from flask import Flask
import os

SECRET_KEY = os.urandom(48)

app = Flask(__name__)

app.config["SECRET_KEY"] = SECRET_KEY

from app import views, forms, calculate