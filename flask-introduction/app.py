from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/home', methods=["GET", "POST"])
def hello_internet():
    if request.method == "POST":
        return "This is a POST request!"
    else:
        return "This is a GET request"

@app.route('/home2/<word>', methods=["GET", "POST"])
def hello_internet2(word):
    if request.method == "POST":
        return "This is a POST request!"
    else:
        return word.upper()

@app.route('/home3/<num>', methods=["GET", "POST"])
def hello_internet3(num):
    if request.method == "POST":
        return "This is a POST request!"
    else:
        return str(num * 2)


@app.route('/accessgoogle')
def accessGoogle():
        return redirect(url_for("hello_internet"))

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)