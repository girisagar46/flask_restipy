# Flask Restipy
**Flask Restipy** is a a simple Flask REST API client which supports the CRUD operation. These codebase is from tutorial at http://exponential.io/


# Running locally
1. Install [virualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
2. Clone the [repository](git@github.com:girisagar46/flask_restipy.git)
3. `$ cd flask_restipy`
4. `$ pip install -r requirements.txt`
4. `$ python server.py`

**Use REST API client such as [postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) or CURL to test the API.**

# Fake database
```json
{
        "exponential" : {
            "name" : "Exponential.io",
            "city" : "Palo Alto"
        },
        "deerwalk": {
            "name": "Deerwalk Inc.",
            "city": "Boston MA"
        }
    }
```

# API Descriptions
|METHOD|URL|DESCRIPTION|
|------|---|-----------|
|GET|http://localhost:5000| *gets all compay list*|
|GET|http://localhost:5000/company_id| *gets specefic compay name based on company_id*|
|POST|http://localhost:5000|*create a company*|
|PUT|http://localhost:5000/company_id| *updates company with company_id*|
|DELETE|http://localhost:5000/company_id| *deletes the company with company_id*|

# Unit Testing --
Run `$ python -m unittest discover -p '*_test.py'` in your terminal by staying in the peoject root directory to run the unit tests.

> [girisagar46.github.io](https://girisagar46.github.io)
