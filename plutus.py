from db import get_db, close_db

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
        return get_persons()
    elif request.method == 'POST':
        return post_person()
    elif request.method == 'DELETE':
        return delete_persons()

def get_persons():
    db = get_db()
    db_result = db.execute('SELECT * FROM persons')
    persons = [dict(schedule) for schedule in db_result]
    close_db()
    if using_json():
        return jsonify(persons)
    else:
        return render_template(
            'persons.html',
            persons = persons
        )

def post_person():
    request_data = request.get_json(force=True)
    name = request_data.get('name')

    db = get_db()
    db.execute('INSERT INTO persons(name) VALUES(?)',(name,))
    db.commit()
    close_db()
    return ('', 201)

def delete_persons():
    db = get_db()
    db.execute('DELETE FROM persons')
    db.commit()
    return ('', 204)
