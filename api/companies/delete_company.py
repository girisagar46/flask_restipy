from api import app
from api import database
from flask import jsonify
from flask import request

"""
curl -X DELETE -H "Content-Type: application/json" \
http://localhost:5000/companies/exponential
"""


@app.route("/companies/<string:company_id>", methods=['DELETE'])
def delete_company(company_id):
    db = database()
    company = db[company_id]
    del db[company_id]
    return jsonify({company_id: company})