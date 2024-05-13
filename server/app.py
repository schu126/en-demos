from flask import Flask, jsonify, request
import os, random
from flask_migrate import Migrate;
from flask_cors import CORS

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
app = Flask(__name__)
# this proved unecessary with the jsonify.headers add approach
# cors = CORS(app, resources={r"/": {"origins": "*"}})
# vv This was necessary to allow patch requests
cors = CORS(app);
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


if __name__ == "__main__":
    app.run(port=5555, debug=True)