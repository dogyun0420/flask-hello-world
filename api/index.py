from flask import Flask, jsonify, render_template
import csv

app = Flask(__name__)

df = list(csv.reader(open('data/2019.csv', 'r')))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/countries')
def countries():
    return jsonify(sorted([r[1] for r in df[1:]]))