from flask import Flask
from flask_cors import CORS
from loaders import conextion
from psycopg2 import connect

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = conextion()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = connect(conextion())