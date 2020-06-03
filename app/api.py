from app import app
from flask import jsonify, request

import app.b3_requests as B3


@app.route('/empresa/<regex("[A-Za-z0-9]"):letra>', methods=['GET'])
def get_companies(letra):

    companies = B3.get_companies_by_letter(letra)

    return jsonify(companies)


@app.route('/busca', methods=['GET'])
def search_companies():

    search = request.args.get('q')
    companies = B3.search_companies(search)

    return jsonify(companies)
