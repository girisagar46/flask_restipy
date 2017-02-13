from api import app
from api import database
from flask import jsonify
from flask import request

@app.route('/companies', methods=['POST'])
def create_company():
    company = request.get_json()
    db = database()
    db.update(company)
    return jsonify(company), 201