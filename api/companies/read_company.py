from api import app
from api import database
from flask import jsonify

# Read one company with @company_id
@app.route('/companies/<string:company_id>', methods=['GET'])
def read_company(company_id):

    # define database
    db = database()

    # find company based on companu_id provided
    company = db[company_id]

    # return json
    return jsonify(company)