from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
api = Api(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
CORS(app)

# Import resource classes and add routes here

if __name__ == '__main__':
    app.run(port=5000, debug=True)
