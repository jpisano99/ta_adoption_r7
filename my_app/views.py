from my_app import app
from my_app.main import get_customer
from flask import render_template, url_for, request, jsonify
from my_app.pre_run_file_checks import pre_run_file_checks


@app.route('/', methods=['GET', 'POST'])
def index():
    # Go run this script when this route is called
    cust_name = get_customer()
    print('here i am')
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


@app.route('/stan', methods=['GET', 'POST'])
def doit():
    print('Processing Starting')
    pre_run_file_checks()
    return 'DONE with PreRunFileChecks !'