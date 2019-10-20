from my_app import app
from my_app.main import get_customer
from flask import render_template, url_for, request, jsonify
from my_app.pre_run_file_checks import pre_run_file_checks
from my_app.build_customers_r1 import main
from my_app.import_updates_to_sql import import_updates_to_sql


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
        type_of_url = 'GET Version 1.0 '
    # return jsonify({'about': type_of_url}), 201
    # return render_template('login.html', cust_name=cust_name)
    return render_template('index.html', type_of_url=type_of_url, cust_name=cust_name)


@app.route('/pre_check', methods=['GET', 'POST'])
def pre_check():
    print('Processing Starting')
    pre_run_file_checks()
    return 'DONE with PreRunFileChecks !'


@app.route('/build_it', methods=['GET', 'POST'])
def build_it():
    print('Processing Starting')
    main()
    return 'DONE with Building Dashboard !'


@app.route('/load_db', methods=['GET', 'POST'])
def load_db():
    print('Loading DB')
    import_updates_to_sql()
    return 'DONE with Loading Database !'


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print('Uploading')
    if request.method == "POST":
        print(request.files)
        # if request.files:
        #     pass

    return render_template('upload.html')
