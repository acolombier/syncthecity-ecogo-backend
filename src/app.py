#!/usr/bin/env python3
# encoding: utf-8
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
app.config.update(
    JSON_AS_ASCII=False,
    DEBUG=True,
    JSONIFY_PRETTYPRINT_REGULAR=False
)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

headers = {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'OK'}), 200, headers


# ~ ===========
# ~ Init
# ~ ===========

if __name__ == '__main__':
    print('starting app with flask')
    app.run(debug=True, host='127.0.0.1', port=8080)
