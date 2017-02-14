"""Creating and configure Flask server"""

from flask import Flask

app = Flask(__name__)

# Fake database
def database():
    return {
        "exponential" : {
            "name" : "Exponential.io",
            "city" : "Palo Alto"
        },
        "deerwalk": {
            "name": "Deerwalk Inc.",
            "city": "Boston MA"
        }
    }

# Routes
from api.companies import read_company
from api.companies import read_companies
from api.companies import create_company
from api.companies import update_company
from api.companies import delete_company