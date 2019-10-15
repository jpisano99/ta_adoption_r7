from my_app import app
from my_app.main import get_customer
from my_app.settings import app_cfg
from flask import render_template, url_for, request, jsonify


@app.route('/', methods=['GET', 'POST'])
def index():
    # Go run this script when this route is called
    cust_name = get_customer()
    if request.method == 'POST':
        some_json = request.get_json()
        print('type', type(some_json))
        print('json:', some_json)
        type_of_url = 'POSTED Version 2.0'
    else:
        type_of_url = 'GET Version 1.0 ' + cust_name
    # return jsonify({'about': type_of_url}), 201
    return render_template('login.html', cust_name=cust_name)
    # return render_template('index.html', type_of_url=type_of_url, cust_name=cust_name)
