from flask import Flask, jsonify, request, session
from config import app, db
from flask_login import LoginManager, login_manager

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def root():
    return '<h1>Welcome to en demos</h1>'


if __name__ == "__main__":
    app.run(port=5555, debug=True)