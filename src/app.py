#!/usr/bin/env python3
# encoding: utf-8
import random

from flask import Flask, jsonify, request
from flask_cors import CORS
from search import SearchService
from carbonfootprint import CarbonFootprintService

import data as stub


app = Flask(__name__)
app.config.update(
    JSON_AS_ASCII=False,
    DEBUG=True,
    JSONIFY_PRETTYPRINT_REGULAR=False
)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

headers = {'Content-Type': 'application/json; charset=utf-8'}

co2Service = CarbonFootprintService()
searchService = SearchService(co2Service)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'OK'}), 200, headers


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    if 'from' not in data or 'to' not in data:
        return jsonify(
            {
                'error': {
                    'code': 400,
                    'message': 'Invalid Request, please include from and to values in post body'
                }
            }
        ), 400, headers

    # Search for Options
    results = searchService.search(data['from']['lat'], data['from']['lon'], data['to']['lat'], data['to']['lon'])
    return jsonify(results), 200, headers


@app.route('/ticket', methods=['POST'])
def ticket():
    data = request.json
    return jsonify(
        {
            'step': random.choice(stub.tickets)
        }
    ), 200, headers


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    searchService = SearchService()
    if 'from' not in data or 'to' not in data:
        return jsonify(
            {
                'error': {
                    'code': 400,
                    'message': 'Invalid Request, please include from and to values in post body'
                }
            }
        ), 400, headers

    print(data)
    # Search for Options
    results = searchService.search(data['from']['lat'], data['from']['lon'], data['to']['lat'], data['to']['lon'])
    return jsonify(results, 200, headers)


# ~ ===========
# ~ Init
# ~ ===========

if __name__ == '__main__':
    print('starting app with flask')
    app.run(debug=True, host='0.0.0.0', port=8080)
