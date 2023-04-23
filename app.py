#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from sprc_connector import get_sparc_result
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/query_sparc', methods=['GET'])
def get_query_records():
    input_string = request.args.get('input_string')
    try:
        query = get_sparc_query(input_string)
        result = get_sparc_result(query)
        return jsonify({'result': result})
    except Exception as err:
        return jsonify({'error': 'data not found', "reason": str(err)})


@app.route('/query_sparc', methods=['POST'])
def post_query_records():
    input_string = request.form.get('query')
    try:
        query = get_sparc_query(input_string)
        result = get_sparc_result(query)
        result = result.replace(",_", "__")
        result = result.replace("_", " ")
        response = jsonify({'result': result})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as err:
        return jsonify({'error': 'data not found', "reason": str(err)})


def get_sparc_query(input_string):

    categories = ['drama', 'crime', 'fantasy', 'scientific', 'fiction', 'story']
    input_string = input_string.lower()

    if 'lost' in input_string and 'book' in input_string:
        return "lost_book_policy(P)"
    elif 'opening' in input_string and 'hours' in input_string and 'weekdays' in input_string:
        return "opening_hours(weekdays,X)"
    elif 'opening' in input_string and 'hours' in input_string and 'weekends' in input_string:
        return "opening_hours(weekends,X)"
    elif 'opening' in input_string and 'hours' in input_string:
        return "opening_hours(Y,X)"
    elif 'ebook' in input_string and 'available' in input_string:
        return "ebook_available(X)"
    elif 'type' in input_string and 'information' in input_string:
        return "information_type(X)"
    elif 'how many' in input_string and 'check out' in input_string:
        return "max_books(X)"
    elif 'how long' in input_string and 'borrow' in input_string:
        return "borrowing_period(X, Y)"
    elif 'return' in input_string and 'check' in input_string:
        return "return_policy(X)"
    elif 'recommend' in input_string or any(word in input_string for word in categories):
        for word in categories:
            if word in input_string:
                return "category({0},X)".format(word)
        return "category(Y,X)"

    else:
        return None

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5001)


