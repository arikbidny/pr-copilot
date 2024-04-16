# import request
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(port=5000)
