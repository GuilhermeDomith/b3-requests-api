from flask import Flask, jsonify, request
from url_converters import RegexConverter
import b3_requests as B3

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter


@app.route('/empresa/<regex("[A-Za-z0-9]"):letra>', methods=['GET'])
def get_companies(letra):

    companies = B3.get_companies_by_letter(letra)

    return jsonify(companies)


@app.route('/busca', methods=['GET'])
def search_companies():

    search = request.args.get('q')
    companies = B3.search_companies(search)

    return jsonify(companies)


if __name__ == '__main__':
    app.run(host='localhost', port=3030)
