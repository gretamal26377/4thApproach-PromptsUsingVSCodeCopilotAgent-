import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../backend/app')))

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the backend!"

@app.route('/data', methods=['GET'])
def get_data():
    data = {
        "name": "John Doe",
        "age": 30
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)