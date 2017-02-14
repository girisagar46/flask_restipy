from api import app
from api import database
from flask import jsonify
from flask import request

"""
curl -X PUT -H "Content-Type: application/json" \
-d '{"name": "Exponential.io", "city": "Mountain View"}' \
http://localhost:5000/companies/exponential
"""

@app.route("/companies/<string:company_id>", methods=['PUT'])
def update_company(company_id):
    company = request.get_json()
    db = database()
    db[company_id] = company
    return jsonify({company_id: db[company_id]})