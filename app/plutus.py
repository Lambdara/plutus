from db import get_db, close_db
from persons import *
from payments import *
from balances import *

from flask import Flask, request, jsonify, abort, render_template
import re


app = Flask(__name__)
app.config['DATABASE'] = 'database'

def using_json():
    return request.headers.get('accept') == 'application/json'


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/persons/', methods=['GET', 'POST', 'DELETE'])
def manage_persons():
    if request.method == 'GET':
        persons = get_persons()
        if using_json():
            return jsonify(persons)
        else:
            return render_template(
                'persons.html',
                persons = persons
            )
    elif request.method == 'POST':
        name = request.get_json(force=True).get('name')
        post_person(name)
        return ('', 201)
    elif request.method == 'DELETE':
        delete_persons()
        return ('', 204)


@app.route('/persons/<int:person_id>', methods=['GET', 'DELETE'])
def manage_person(person_id):
    if request.method == 'GET':
        person = get_person(person_id)
        return jsonify(person_id)
    elif request.method == 'DELETE':
        delete_person(person_id)
        return ('',204)


@app.route('/payments/', methods=['GET', 'POST', 'DELETE'])
def manage_payments():
    if request.method == 'GET':
        payments = get_payments()
        if using_json():
            return jsonify(payments)
        else:
            return render_template(
                'payments.html',
                payments = payments
            )
    elif request.method == 'POST':
        request_data = request.get_json(force=True)

        description = request_data.get('description')
        amount = request_data.get('amount')
        payer_id = request_data.get('payer_id')
        payee_ids = request_data.get('payee_ids')

        post_payment(description, amount, payer_id, payee_ids)
        return ('', 201)
    elif request.method == 'DELETE':
        delete_payments()
        return ('', 204)


@app.route('/payments/<int:payment_id>', methods=['GET', 'DELETE'])
def manage_payment(payment_id):
    if request.method == 'GET':
        payment = get_payment(payment_id)
        return jsonify(payment)
    elif request.method == 'DELETE':
        delete_payment(payment_id)
        return ('',204)


@app.route('/balances', methods=['GET'])
def get_balances():
    return render_template(
        'balances.html',
        balances = calculate_balances(),
        transactions = resolve_transactions()
    )
