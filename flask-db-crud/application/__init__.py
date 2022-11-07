from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

