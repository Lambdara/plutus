from db import get_db, close_db

from flask import Flask, request, jsonify, abort, render_template
import re


app = Flask(__name__)
app.config['DATABASE'] = 'database'

@app.route("/")
def index():
    return "Hello world!"
