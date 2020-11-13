from flask import request, jsonify
from flask import Blueprint
from flask_cors import CORS, cross_origin

import postcodes_uk

app = Blueprint('uk_postcodes', __name__)


@app.route('/validate', methods=['GET'])
def validate_postcode():
    if request.method == 'GET':
        postcode = request.args.get("postcode")
        valid_postcode = postcodes_uk.validate(postcode)

        return jsonify({
            'valid_postcode': valid_postcode
        })


@app.route('/format', methods=['GET'])
def format_postcode():
    if request.method == 'GET':
        params = request.args

        area = params.get("area")
        district = params.get("district")
        sector = params.get("sector")
        unit = params.get("unit")

        postcode = postcodes_uk.Postcode(area=area, district=district, sector=int(sector), unit=unit)
        return jsonify({
            'result_postcode': str(postcode)
        })
