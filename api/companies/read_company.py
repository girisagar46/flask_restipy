from api import app
from api import database
from flask import jsonify

@app.route('/companies/<string:company_id>', methods=['GET'])
def read_company(company_id):
    db = database()
    company = db[company_id]

    return jsonify(company)